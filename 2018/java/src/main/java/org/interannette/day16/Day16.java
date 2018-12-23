package org.interannette.day16;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

public class Day16 {

    public static void main(String[] args) throws IOException {
        Day16 day16 = new Day16(InputGetter.getInput(16));
        System.out.println("Samples matching more than 3: " + day16.solveStar1());
        System.out.println("Result after applying instructions: " + day16.solveStar2());
    }

    Set<Sample> samples = new HashSet<>();
    List<Instruction> instructions = new ArrayList();
    Map<Integer, Operation.Name> operationsByNumber = new HashMap<>(Operation.Name.values().length);

    public Day16(String input) {
        String[] lines = input.split("\n");
        int startOfInstructions = 0;
        for(int i = 0; i < lines.length; i = (i + 4)) {
            if(lines[i].startsWith("Before")) {
                samples.add(new Sample(Arrays.copyOfRange(lines, i, i+3)));
            } else {
                startOfInstructions = i;
                break;
            }
        }

        for(int i = startOfInstructions; i < lines.length; i++) {
            if(!lines[i].isEmpty()) {
                instructions.add(new Instruction(lines[i].trim()));
            }
        }
    }

    public int solveStar1() {
        int samplesWithMoreThan3 = 0;
        for(Sample sample : samples) {
            if(matchingOperations(sample).size() > 2) {
                samplesWithMoreThan3++;
            }
        }
        return samplesWithMoreThan3;
    }

    public static Set<Operation.Name> matchingOperations(Sample sample) {
        Set<Operation.Name> matches = new HashSet<>();
        for(Operation.Name name : Operation.Name.values()) {
            if(Operation.matches(name, sample)) {
                matches.add(name);
            }
        }
        return matches;
    }

    public int solveStar2() {
        determineOperations();
        int[] register = {0,0,0,0};
        for(Instruction instruction : instructions) {
            register = doInstruction(register, instruction);
        }

        return register[0];
    }

    public int[] doInstruction(int[] register, Instruction instruction) {
        Operation.Name operation = operationsByNumber.get(instruction.opperation);
        return Operation.performOperation(operation, instruction.input1, instruction.input2, instruction.output, register);
    }

    public void determineOperations() {
        Map<Integer, Set<Operation.Name>> possibleOperations = new HashMap<>(Operation.Name.values().length);
        for(Sample sample : samples) {
            Set<Operation.Name> matchingOperations = matchingOperations(sample);
            Set<Operation.Name> existingOperations = possibleOperations.get(sample.instruction.opperation);
            if(existingOperations != null) {
                existingOperations.retainAll(matchingOperations);
            } else {
                existingOperations = matchingOperations;
            }
            possibleOperations.put(sample.instruction.opperation, existingOperations);
        }

        while(operationsByNumber.keySet().size() < Operation.Name.values().length) {
            List<Map.Entry<Integer, Set<Operation.Name>>> sortedPossibleMatches = possibleOperations.entrySet().stream()
                    .sorted(Comparator.comparing(e -> e.getValue().size()))
                    .collect(Collectors.toList());

            for(Map.Entry<Integer, Set<Operation.Name>> matches : sortedPossibleMatches) {
                if(matches.getValue().size() == 1) {
                    operationsByNumber.put(matches.getKey(), matches.getValue().iterator().next());
                    possibleOperations.remove(matches.getKey());
                } else {
                    matches.getValue().removeAll(operationsByNumber.values());
                    possibleOperations.put(matches.getKey(), matches.getValue());
                }
            }
        }

        if(operationsByNumber.values().stream().collect(Collectors.toSet()).size() != Operation.Name.values().length) {
            throw new IllegalArgumentException("Unable to determine operations");
        }
    }
}
