package org.interannette.day1;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class Day1 {

    private static final String INPUT_STRING = "+1\n" +
            "-2\n" +
            "+3\n" +
            "+1";

    public static void main(String[] args) {

        Day1 testDay = new Day1(INPUT_STRING);
        System.out.println("Total Frequency Shifts: " + testDay.solveStar1());
        System.out.println("First Repeated Frequency: " + testDay.solveStar2());
    }

    private List<Integer> input;

    public Day1(String inputAsString) {
        String[] integersAsStrings = inputAsString.split("\n");
        this.input = Arrays.asList(integersAsStrings).stream().map(Integer::valueOf).collect(Collectors.toList());
    }

    public int solveStar1() {

        return input.stream().mapToInt(Integer::intValue).sum();

    }

    public int solveStar2() {

        Iterator<Integer> circularIteratorOfShifts = new CircularIterator(input);

        Set<Integer> seenFrequencies = new HashSet<>();
        Integer currentFrequency = 0;

        while(!seenFrequencies.contains(currentFrequency)) {
            seenFrequencies.add(currentFrequency);
            currentFrequency = currentFrequency + circularIteratorOfShifts.next();
        }

        return currentFrequency;
    }
}
