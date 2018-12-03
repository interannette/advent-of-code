package org.interannette.day2;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Day2 {

    public static void main(String args[]) throws IOException {
        Day2 day2 = new Day2(InputGetter.getInput(2));
        System.out.println("Checksum is: " + day2.solveStar1());
        System.out.println("Matching characters are: " + day2.solveStar2());
    }

    private List<String> ids;

    public Day2(String idList) {
        this.ids = Arrays.asList(idList.split("\n"));
    }

    public String solveStar2() {
        String s1 = null;
        Integer differencePosition = null;

        for(int i = 0; i < ids.size(); i++) {
            for(int j = i+1; j < ids.size(); j++) {
                List<Integer> differencePositions = differencePos(ids.get(i), ids.get(j));
                if(differencePositions.size() == 1) {
                    s1 = ids.get(i);
                    differencePosition = differencePositions.get(0);
                    break;
                }
            }
        }

        if(differencePosition == null || s1 == null) {
            throw new RuntimeException("No match found");
        }
        return s1.substring(0, differencePosition) + s1.substring(differencePosition + 1);
    }

    protected static List<Integer> differencePos(String s1, String s2) {

        if(s1.length() != s2.length()) {
            throw new IllegalArgumentException("Strings should all be the same size");

        }

        List<Integer> differencePositions = new ArrayList<>(s1.length());
        for(int i = 0; i < s1.length(); i++) {
            if(s1.charAt(i) != s2.charAt(i)) {
                differencePositions.add(i);
            }
        }

        return differencePositions;
    }

    public long solveStar1() {
        long twos = 0;
        long threes = 0;

        for(String id : ids) {
            Map<Long, Long> frequencyCounts = countFrequencies(id);
            if(frequencyCounts.containsKey(2l)) {
                twos++;
            }
            if(frequencyCounts.containsKey(3l)) {
                threes++;
            }
        }

        return twos * threes;
    }

    protected static Map<Long, Long> countFrequencies(String id) {
        Map<String, Long> letterCounts = Arrays.asList(id.split("")).stream()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        Map<Long, Long> countCounts = letterCounts.values().stream()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        return countCounts;
    }

    private static String INPUT_STRING = "";
}
