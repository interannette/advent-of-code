package org.interannette.day12;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Day12 {

    Pot potsHead;
    boolean[] growthArray;

    public static void main(String[] args) throws IOException {
        //Day12 star1 = new Day12(InputGetter.getInput(12));
        //System.out.println("Star 1 sum: " + star1.solveStar1());

        Day12 star2 = new Day12(InputGetter.getInput(12));
        System.out.println("Star 2 sum: " + star2.solveStar2());
    }

    public Day12(String input) {
        String[] lines = input.split("\n");

        potsHead = Pot.parseInput(lines[0]);

        Map<Integer, Boolean> rulesMap = new HashMap<>(lines.length);
        for(int i = 1; i < lines.length; i++) {
            String trimedLine = lines[i].trim();
            if(!trimedLine.isEmpty()) {
                GrowthRule growthRule = GrowthRule.parseRule(trimedLine);
                rulesMap.put(growthRule.startState, growthRule.result);
            }
        }

        growthArray = new boolean[32];
        for(int i = 0; i < 32; i++) {
            growthArray[i] = rulesMap.getOrDefault(i, false);
        }

    }

    public long solveStar2() {
        return findResultForGeneration(50000000000l);
    }

    public long solveStar1() {
        return findResultForGeneration(20l);
    }

    private long findResultForGeneration(long numberOfGenerations) {
        Pot thisGeneration = potsHead;
        long generation = 0;
        System.out.println("Generation " + generation + " " + thisGeneration);

        while(generation < numberOfGenerations) {
            generation++;
            thisGeneration = advanceGeneration(thisGeneration);
            if(generation % 1000 == 0) {
                System.out.println("Generation " + generation);
            }
        }

        return addUpPresentPots(thisGeneration);
    }

    private long addUpPresentPots(Pot head) {

        long total = 0;
        Pot current = head;
        while(current != null) {
            if(current.present) {
                total += current.number;
            }
            current = current.nextPot;
        }
        return total;
    }

    public Pot advanceGeneration(Pot start) {

        Pot currentPot = start;
        Pot nextGenerationCurrentPot = new Pot(start.number, grow(start));

        Pot nextGenerationStart = nextGenerationCurrentPot;
        // if the first pot currently constructed is present, build out two more in case they grow next time
        if(nextGenerationStart.present) {
            Pot leftOne = new Pot(start.number - 1, false);
            leftOne.nextPot = nextGenerationStart;

            Pot leftTwo = new Pot(start.number - 2, false);
            leftTwo.nextPot = leftOne;
            leftOne.previousPot = leftTwo;

            nextGenerationStart = leftTwo;
        }

        int currentState = GrowthRule.getState(currentPot);
        Pot twoRight = currentPot.nextPot.nextPot;

        while(currentPot.nextPot != null) {
            currentPot = currentPot.nextPot;
            twoRight = (twoRight != null) ? twoRight.nextPot : null;

            // mask to 4, shift left, add two right in 1s pos.
            currentState = (currentState & 0b1111) << 1 |
                    ((twoRight != null && twoRight.present ? 1 : 0) << 0);
            boolean grow = growthArray[currentState];

            Pot nextGenerationNextPot = new Pot(currentPot.number, grow);
            nextGenerationCurrentPot.nextPot = nextGenerationNextPot;
            nextGenerationNextPot.previousPot = nextGenerationCurrentPot;

            nextGenerationCurrentPot = nextGenerationNextPot;
        }

        // if the last pot currently constructed is present, build out two more in case they grow next time
        if(nextGenerationCurrentPot.present) {
            Pot rightOne = new Pot(nextGenerationCurrentPot.number + 1, false);
            nextGenerationCurrentPot.nextPot = rightOne;
            rightOne.previousPot = nextGenerationCurrentPot;

            Pot rightTwo = new Pot(nextGenerationCurrentPot.number + 2, false);
            rightTwo.previousPot = rightOne;
            rightOne.nextPot = rightTwo;
        }

        return nextGenerationStart;
    }

    private boolean grow(Pot currentPot) {
        return growthArray[GrowthRule.getState(currentPot)];
    }
}
