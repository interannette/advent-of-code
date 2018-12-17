package org.interannette.day12;

import lombok.Data;

@Data
public class GrowthRule {
    int startState;
    boolean result;

    public GrowthRule(int startState, boolean result) {
        this.startState = startState;
        this.result = result;
    }

    public static GrowthRule parseRule(String line) {
        String[] parts = line.split("=>");

        char[] inputState = parts[0].trim().toCharArray();

        int startStateAsInt = 0;
        for(int i = 0; i < inputState.length; i++) {
            startStateAsInt += Math.pow(2, (inputState.length - i - 1)) * (inputState[i] == '#' ? 1 : 0);
        }

        return new GrowthRule(startStateAsInt, parts[1].trim().equals("#"));
    }

    public static int getState(Pot currentPot) {
        Pot oneLeft = currentPot.previousPot;
        Pot twoLeft = (oneLeft != null) ? oneLeft.previousPot : null;
        Pot oneRight = currentPot.nextPot;
        Pot twoRight = (oneRight != null) ? oneRight.nextPot : null;

        return  (twoLeft != null && twoLeft.present ? 1: 0) << 4 |
                (oneLeft != null && oneLeft.present ? 1 : 0) << 3 |
                (currentPot.present ? 1 : 0) << 2 |
                (oneRight != null && oneRight.present ? 1 : 0) << 1 |
                (twoRight != null && twoRight.present ? 1 : 0) << 0;
    }
}
