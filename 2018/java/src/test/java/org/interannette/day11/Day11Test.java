package org.interannette.day11;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day11Test {

    @Test
    void sampleInput1() {
        Day11 day11 = new Day11(18);
        assertEquals(new Grid.SubGrid(33, 45, 3, 29), day11.solveStar1());
    }

    @Test
    void sampleInput2() {
        Day11 day11 = new Day11(42);
        assertEquals(new Grid.SubGrid(21,61, 3, 30), day11.solveStar1());
    }

}
