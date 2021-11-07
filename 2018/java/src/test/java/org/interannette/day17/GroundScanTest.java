package org.interannette.day17;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class GroundScanTest {

    @Test
    void sampleInput() {
        GroundScan scan = new GroundScan("x=495, y=2..7\n" +
                "y=7, x=495..501\n" +
                "x=501, y=3..7\n" +
                "x=498, y=2..4\n" +
                "x=506, y=1..2\n" +
                "x=498, y=10..13\n" +
                "x=504, y=10..13\n" +
                "y=13, x=498..504");

        String output = "......+.......\n" +
                "............#.\n" +
                ".#..#.......#.\n" +
                ".#..#..#......\n" +
                ".#..#..#......\n" +
                ".#.....#......\n" +
                ".#.....#......\n" +
                ".#######......\n" +
                "..............\n" +
                "..............\n" +
                "....#.....#...\n" +
                "....#.....#...\n" +
                "....#.....#...\n" +
                "....#######...\n";

        assertEquals(output, scan.format());
    }
}
