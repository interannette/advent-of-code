package org.interannette.day11;

public class Day11 {


    Grid grid;
    int serialNumber = 2568;
    int windowSize = 3;

    public static void main(String[] args) {
        Day11 day11 = new Day11();
        System.out.println("Maximum 3x3 has top left corner: " + day11.solveStar1());
        System.out.println("Maximum any size grid is: " + day11.solveStar2());
    }

    public Day11() {
        this.grid = new Grid(2568);
    }

    public Day11(int serialNumber) {
        this.serialNumber = serialNumber;
        this.grid = new Grid(serialNumber);
    }

    public Grid.SubGrid solveStar2() {
        Integer max = null;
        Grid.SubGrid maxSubGrid = null;
        for(int i = 1; i <= Grid.GRID_SIZE; i++) {
            this.windowSize = i;
            Grid.SubGrid subGrid = solveStar1();
            if(max == null || subGrid.value > max) {
                max = subGrid.value;
                maxSubGrid = subGrid;
            }
            System.out.println("After checking size " + windowSize + " maximum is " + maxSubGrid);
        }
        return maxSubGrid;
    }

    public Grid.SubGrid solveStar1() {

        Grid.SubGrid maxCell = null;
        Integer max = null;
        for(int x = 0; x <= Grid.GRID_SIZE - windowSize; x++) {
            for(int y = 0; y <= Grid.GRID_SIZE - windowSize; y++) {
                int value = grid.valueOfSubgrid(x, y, windowSize);
                if(max == null || value > max) {
                    max = value;
                    maxCell = new Grid.SubGrid(x+1,y+1, windowSize, value);
                }
            }
        }

        return maxCell;
    }
}
