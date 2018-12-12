package org.interannette.day11;

public class GridCell {
    private static final int GRID_SERIAL_NUMBER = 2568;

    int x,y;

    public GridCell(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int powerLevel() {
        return powerLevel(GRID_SERIAL_NUMBER);
    }

    public int powerLevel(int serialNumber) {
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
