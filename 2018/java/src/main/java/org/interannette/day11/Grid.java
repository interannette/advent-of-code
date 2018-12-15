package org.interannette.day11;

import lombok.Data;

public class Grid {
    public static final int GRID_SIZE = 300;
    int[][] summedAreaTable;
    int serialNumber;

    public Grid(int serialNumber) {
        this.serialNumber = serialNumber;

        this.summedAreaTable = new int[GRID_SIZE][GRID_SIZE];
        for(int x = 0; x < GRID_SIZE; x++) {
            for(int y = 0; y < GRID_SIZE; y++) {
                int summedArea = powerLevel(x+1,y+1, serialNumber);
                if(x > 0 && y == 0) {
                    summedArea += summedAreaTable[x-1][y];
                } else if(x == 0 && y > 0) {
                    summedArea += summedAreaTable[x][y-1];
                } else if(x == 0 && y == 0) {
                    // done
                } else {
                    summedArea += (summedAreaTable[x][y-1] +
                            summedAreaTable[x-1][y] -
                            summedAreaTable[x-1][y-1]);
                }

                summedAreaTable[x][y] = summedArea;
            }
        }
    }

    public int valueOfSubgrid(int x, int y, int windowSize) {
        if( x == 0 && y == 0) {
            return summedAreaTable[x+(windowSize-1)][y+(windowSize-1)];
        } else if(x == 0 && y > 0) {
            return summedAreaTable[x+(windowSize-1)][y+(windowSize-1)]
                    - summedAreaTable[x+(windowSize-1)][y-1];
        } else if(x > 0 && y == 0) {
            return summedAreaTable[x+(windowSize-1)][y+(windowSize-1)]
                    - summedAreaTable[x-1][y+(windowSize-1)];
        } else {
            return summedAreaTable[x+(windowSize-1)][y+(windowSize-1)]
                    - summedAreaTable[x+(windowSize-1)][y-1]
                    - summedAreaTable[x-1][y+(windowSize-1)]
                    + summedAreaTable[x-1][y-1];
        }
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

    @Data
    public static class SubGrid {

        int x,y, size, value;

        public SubGrid(int x, int y, int size, int value) {
            this.x = x;
            this.y = y;
            this.size = size;
            this.value = value;
        }
    }

}
