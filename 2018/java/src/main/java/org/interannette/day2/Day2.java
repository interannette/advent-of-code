package org.interannette.day2;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Day2 {
    public static String INPUT_STRING ="";
    public static void main(String args[]) {
        Day2 day2 = new Day2(INPUT_STRING);
        System.out.println("Checksum is: " + day2.solveStar1());
    }

    private List<String> ids;

    public Day2(String idList) {
        this.ids = Arrays.asList(idList.split("\n"));
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
}
