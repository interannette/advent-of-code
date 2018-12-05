package org.interannette.day5;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Objects;
import java.util.Queue;
import java.util.Stack;

public class Day5 {

    public static void main(String[] args) throws IOException {
        Day5 day5 = new Day5(InputGetter.getInput(5).replace("\n",""));
        System.out.println("Star 1: " + day5.solveStar1());
        System.out.println("Star 2: " + day5.solveStar2());
    }

    Queue<Character> inputChars;
    String inputString;

    public Day5(String inputString) {
        this.inputString = inputString;
        this.inputChars = new LinkedList<>();
        for(char c : inputString.toCharArray()) {
            inputChars.add(c);
        }
    }

    public Integer solveStar1() {
        Stack<Character> resultChars = new Stack<>();

        Character previous = null;
        Character next = inputChars.poll();
        while(next != null) {
            if(areOppositePolarity(previous, next)) {
                previous = !resultChars.isEmpty() ? resultChars.pop() : null;
                next = inputChars.poll();
            } else {
                if(previous != null) {
                    resultChars.push(previous);
                }
                previous = next;
                next = inputChars.poll();
            }
        }

        if(previous != null) {
            resultChars.push(previous);
        }

        return resultChars.size();
    }


    static boolean areOppositePolarity(Character i, Character j) {
        if(i == null || j == null) {
            return false;
        }
        return !Objects.equals(i,j)  && Character.toUpperCase(i) == Character.toUpperCase(j);
    }

    public Integer solveStar2() {
        Map<Character,Integer> resultByLetterRemoved = new HashMap<>(26);

        for (char alphabet = 'A'; alphabet <= 'Z'; alphabet++) {
            String updatedInput = inputString.replace(Character.toString(alphabet),"");
            updatedInput = updatedInput.replace(Character.toString(Character.toLowerCase(alphabet)),"");
            Day5 day5 = new Day5(updatedInput);
            Integer result = day5.solveStar1();
            resultByLetterRemoved.put(alphabet, result);
        }

        return resultByLetterRemoved.values().stream().min(Comparator.comparingInt(e -> e)).get();
    }

}
