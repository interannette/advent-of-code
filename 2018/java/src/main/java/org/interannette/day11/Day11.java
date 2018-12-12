package org.interannette.day11;

import java.util.HashMap;
import java.util.Map;

public class Day11 {

    Map<Integer, Map<Integer, Integer>> powerLevelGrid;

    public Day11() {
        powerLevelGrid = new HashMap<>(300);
        for(int i = 0; i < 300; i++) {
            Map<Integer, Integer> col = new HashMap<>(300);
            for(int j = 0; j < 300; j++) {
                col.put(j, GridCell.powerLevel(i, j));
            }
            powerLevelGrid.put(i, col);
        }
    }

    public void solveDay1() {
        Map<Integer, Map<Integer, Integer>> threeByThreePowerBlocks = new HashMap<>(300);
        for(int i = 0; i < 300 - 2; i++) {
            Map<Integer, Integer> col = new HashMap<>(300);
            for(int j = 0; j < 300 - 2; j++) {
                int sum = 0;
                for(int x = i; x < i + 3; x++) {
                    for(int y = j; y < j + 3; j++) {
                        sum += powerLevelGrid.get(x).get(y);
                    }
                }
                col.put(j, sum);
            }
            threeByThreePowerBlocks.put(i, col);
        }
    }
}
