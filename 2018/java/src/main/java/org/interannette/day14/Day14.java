package org.interannette.day14;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Day14 {

    public static void main(String[] args) {
        System.out.println("Next 10 for star 1: " + getNextTenAfter(633601));
        System.out.println("First instance of for star 2: " + findFirstInstanceOf("633601"));
    }

    public static List<Integer> combineRecipes(int r1, int r2) {
        Integer total = r1 + r2;
        return Arrays.stream(total.toString().split(""))
                .map(s -> Integer.valueOf(s))
                .collect(Collectors.toList());
    }

    public static String getNextTenAfter(int recipeCount) {
        int capacity = recipeCount + 10;
        Scoreboard scoreboard = new Scoreboard(capacity);

        boolean capaciyReached = false;

        while(!capaciyReached) {
            List<Integer> nextRecipes = combineRecipes(scoreboard.getScoreForElf1(), scoreboard.getScoreForElf2());
            if(nextRecipes.size() + scoreboard.count == capacity) {
                scoreboard.addRecipes(nextRecipes);
                capaciyReached = true;
            } else if(nextRecipes.size() + scoreboard.count == capacity + 1) {
                scoreboard.addRecipes(nextRecipes.subList(0,1));
                capaciyReached = true;
            } else {
                scoreboard.addRecipes(nextRecipes);
                scoreboard.advanceElves();
            }
        }

        int[] lastTenScores = scoreboard.getLastScores(10);
        return Arrays.stream(lastTenScores).boxed().map(i -> i.toString()).reduce((s1,s2) -> s1 + s2).get();
    }

    public static Integer findFirstInstanceOf(String listOfIntsAsString) {

        int[] sequence = new int[listOfIntsAsString.length()];
        for(int i = 0; i < listOfIntsAsString.length(); i++) {
            sequence[i] = Character.getNumericValue(listOfIntsAsString.charAt(i));
        }

        Scoreboard scoreboard = new Scoreboard(100000000);

        boolean found = false;
        while(!found) {
            List<Integer> nextRecipes = combineRecipes(scoreboard.getScoreForElf1(), scoreboard.getScoreForElf2());
            for(int nextReceipe : nextRecipes) {
                scoreboard.addRecipe(nextReceipe);
                if(scoreboard.count >= sequence.length) {
                    if (Arrays.equals(sequence,scoreboard.getLastScores(sequence.length))) {
                        found = true;
                        break;
                    }
                }
            }
            scoreboard.advanceElves();
        }

        return scoreboard.count - sequence.length;
    }

}
