package org.interannette.day14;

import java.util.Arrays;
import java.util.List;

public class Scoreboard {
    int count;
    int[] scoreBoard;
    int elf1Index;
    int elf2Index;

    public Scoreboard(int capacity) {
        scoreBoard = new int[capacity];

        scoreBoard[0] = 3;
        scoreBoard[1] = 7;

        elf1Index = 0;
        elf2Index = 1;

        count = 2;
    }

    public void addRecipes(List<Integer> newRecipes) {
        for(Integer i : newRecipes) {
            scoreBoard[count] = i;
            count++;
        }
    }

    public void addRecipe(int newRecipe) {
        scoreBoard[count] = newRecipe;
        count++;
    }

    public void advanceElves() {

        int steps1 = scoreBoard[elf1Index] + 1;
        elf1Index = (elf1Index + steps1) % count;

        int steps2 = scoreBoard[elf2Index] + 1;
        elf2Index = (elf2Index + steps2) % count;

    }

    public int getScoreForElf1() {
        return scoreBoard[elf1Index];
    }
    public int getScoreForElf2() {
        return scoreBoard[elf2Index];
    }

    public int[] getLastScores(int numberOfScores) {
        return Arrays.copyOfRange(scoreBoard, count - numberOfScores, count);
    }
}
