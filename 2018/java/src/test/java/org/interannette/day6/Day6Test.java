package org.interannette.day6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day6Test {

    @Test
    void solveStar1() {
        Day6 day6 = new Day6("1, 1\n" +
                "1, 6\n" +
                "8, 3\n" +
                "3, 4\n" +
                "5, 5\n" +
                "8, 9\n");
        assertEquals(17, (int)day6.solveStar1());
    }

    @Test
    void solveStar2() {
        Day6 day6 = new Day6("1, 1\n" +
                "1, 6\n" +
                "8, 3\n" +
                "3, 4\n" +
                "5, 5\n" +
                "8, 9\n");
        day6.maxDistanceStar2 = 32;
        assertEquals(16l, day6.solveStar2());
    }
}
