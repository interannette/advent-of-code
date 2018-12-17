package org.interannette.day12;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Day12 {

    Pot potsHead;
    Map<Integer, Boolean> growthRules = new HashMap();

    public static void main(String[] args) throws IOException {
        Day12 day12 = new Day12(InputGetter.getInput(12));
        System.out.println("Star 1 sum: " + day12.solveStar1());
    }

    public Day12(String input) {
        String[] lines = input.split("\n");

        potsHead = Pot.parseInput(lines[0]);

        for(int i = 1; i < lines.length; i++) {
            String trimedLine = lines[i].trim();
            if(!trimedLine.isEmpty()) {
                GrowthRule growthRule = GrowthRule.parseRule(trimedLine);
                growthRules.put(growthRule.startState, growthRule.result);
            }
        }

    }

    public int solveStar1() {
        Pot thisGeneration = potsHead;
        int generation = 0;
        System.out.println("Generation " + generation + " " + thisGeneration);

        while(generation < 20) {
            generation++;
            thisGeneration = advanceGeneration(thisGeneration);
            System.out.println("Generation " + generation + " " + thisGeneration);
        }

        return addUpPresentPots(thisGeneration);
    }

    private int addUpPresentPots(Pot head) {

        int total = 0;
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

        while(currentPot.nextPot != null) {
            currentPot = currentPot.nextPot;

            boolean grow = grow(currentPot);

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
        Pot oneLeft = currentPot.previousPot;
        Pot twoLeft = (oneLeft != null) ? oneLeft.previousPot : null;
        Pot oneRight = currentPot.nextPot;
        Pot twoRight = (oneRight != null) ? oneRight.nextPot : null;

        int state = (int)Math.pow(10, 4) * (twoLeft != null && twoLeft.present ? 1: 0) +
                (int)Math.pow(10, 3) * (oneLeft != null && oneLeft.present ? 1 : 0) +
                (int)Math.pow(10, 2) * (currentPot.present ? 1 : 0) +
                (int)Math.pow(10, 1) * (oneRight != null && oneRight.present ? 1 : 0) +
                (int)Math.pow(10, 0) * (twoRight != null && twoRight.present ? 1 : 0);

        return growthRules.getOrDefault(state, false);
    }
}
