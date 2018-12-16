package org.interannette.day12;

import lombok.Data;

import java.util.ArrayList;
import java.util.List;

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
            startStateAsInt += Math.pow(10, (inputState.length - i - 1)) * (inputState[i] == '#' ? 1 : 0);
        }

        return new GrowthRule(startStateAsInt, parts[1].trim().equals("#"));
    }
}
