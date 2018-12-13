package org.interannette.day11;

import java.util.HashMap;
import java.util.Map;

public class Day11 {

    private static final int GRID_SIZE = 300;
    Map<Integer, Map<Integer, Integer>> powerLevelGrid;
    int serialNumber = 2568;

    public static void main(String[] args) {
        Day11 day11 = new Day11();
        System.out.println("Maximum 3x3 has top left corner: " + day11.solveDay1());
    }

    public Day11() {
        powerLevelGrid = new HashMap<>(GRID_SIZE);
        for(int i = 0; i < GRID_SIZE; i++) {
            Map<Integer, Integer> col = new HashMap<>(GRID_SIZE);
            for(int j = 0; j < GRID_SIZE; j++) {
                col.put(j, powerLevel(i, j));
            }
            powerLevelGrid.put(i, col);
        }
    }

    public Day11(int serialNumber) {
        this.serialNumber = serialNumber;
        powerLevelGrid = new HashMap<>(GRID_SIZE);
        for(int i = 0; i < GRID_SIZE; i++) {
            Map<Integer, Integer> col = new HashMap<>(GRID_SIZE);
            for(int j = 0; j < GRID_SIZE; j++) {
                col.put(j, powerLevel(i, j));
            }
            powerLevelGrid.put(i, col);
        }
    }

    public GridCell solveDay1() {

        GridCell maxCell = null;
        Integer max = null;
        for(int i = 0; i < GRID_SIZE - 2; i++) {
            for(int j = 0; j < GRID_SIZE - 2; j++) {
                int sum = 0;
                for(int x = i; x < i + 3; x++) {
                    for(int y = j; y < j + 3; y++) {
                        sum += powerLevelGrid.get(x).get(y);
                    }
                }
                if(max == null || sum > max) {
                    max = sum;
                    maxCell = new GridCell(i,j);
                }
            }
        }

        return maxCell;
    }


    public int powerLevel(int x, int y) {
        return powerLevel(x,y,this.serialNumber);
    }

    public static int powerLevel(int x, int y, int serialNumber) {
        int rackId = x + 10;
        int powerLevel = rackId * y + serialNumber;
        powerLevel = powerLevel * rackId;
        return hundredsDigit(powerLevel) - 5;
    }

    public static int hundredsDigit(int i) {
        int hundredsDigit = (i % 1000) / 100;
        return hundredsDigit;
    }
}
