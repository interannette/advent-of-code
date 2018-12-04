package org.interannette.day3;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class Day3 {

    public static void main(String[] args) throws IOException {

        Day3 testDay = new Day3(InputGetter.getInput(3));
        System.out.println("Squares With Overlapping Claims: " + testDay.solveStar1());

    }

    private List<Claim> input;
    private List<List<Set<String>>> gridOfClaims;

    public Day3(String inputAsString) {
        input = Arrays.stream(inputAsString.split("\n"))
                .map(s -> new Claim(s))
                .collect(Collectors.toList());
    }

    public Integer solveStar1() {
        gridOfClaims = buildGridOfClaims(input);

        int totalConflictedArea = gridOfClaims.stream()
                .mapToInt(row ->
                        row.stream().mapToInt(s -> (s.size() > 1) ? 1 : 0).sum())
                .sum();

        return totalConflictedArea;
    }

    static List<List<Set<String>>> buildGridOfClaims(List<Claim> claims) {
        List<List<Set<String>>> gridOfClaims = initEmptyGrid();
        for(Claim claim : claims) {
            for(int i=claim.y; i < claim.y + claim.height; i++) {
                List<Set<String>> row = gridOfClaims.get(i);
                for(int j=claim.x; j < claim.x + claim.width; j++) {
                    row.get(j).add(claim.id);
                }
            }
        }
        return gridOfClaims;
    }

    private static List<List<Set<String>>> initEmptyGrid() {
        List<List<Set<String>>> grid = new ArrayList<>(1000);
        for(int i = 0; i < 1000; i++) {
            List<Set<String>> row = new ArrayList<>(1000);
            for(int j = 0; j < 1000; j++) {
                row.add(new HashSet<>());
            }
            grid.add(row);
        }
        return grid;
    }

}
