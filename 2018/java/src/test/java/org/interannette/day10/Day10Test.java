package org.interannette.day10;

import com.google.common.collect.Sets;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day10Test {

    private static final String TEST_INPUT = "position=< 9,  1> velocity=< 0,  2>\n"+
            "position=< 7,  0> velocity=<-1,  0>\n"+
            "position=< 3, -2> velocity=<-1,  1>\n"+
            "position=< 6, 10> velocity=<-2, -1>\n"+
            "position=< 2, -4> velocity=< 2,  2>\n"+
            "position=<-6, 10> velocity=< 2, -2>\n"+
            "position=< 1,  8> velocity=< 1, -1>\n"+
            "position=< 1,  7> velocity=< 1,  0>\n"+
            "position=<-3, 11> velocity=< 1, -2>\n"+
            "position=< 7,  6> velocity=<-1, -1>\n"+
            "position=<-2,  3> velocity=< 1,  0>\n"+
            "position=<-4,  3> velocity=< 2,  0>\n"+
            "position=<10, -3> velocity=<-1,  1>\n"+
            "position=< 5, 11> velocity=< 1, -2>\n"+
            "position=< 4,  7> velocity=< 0, -1>\n"+
            "position=< 8, -2> velocity=< 0,  1>\n"+
            "position=<15,  0> velocity=<-2,  0>\n"+
            "position=< 1,  6> velocity=< 1,  0>\n"+
            "position=< 8,  9> velocity=< 0, -1>\n"+
            "position=< 3,  3> velocity=<-1,  1>\n"+
            "position=< 0,  5> velocity=< 0, -1>\n"+
            "position=<-2,  2> velocity=< 2,  0>\n"+
            "position=< 5, -2> velocity=< 1,  2>\n"+
            "position=< 1,  4> velocity=< 2,  1>\n"+
            "position=<-2,  7> velocity=< 2, -2>\n"+
            "position=< 3,  6> velocity=<-1, -1>\n"+
            "position=< 5,  0> velocity=< 1,  0>\n"+
            "position=<-6,  0> velocity=< 2,  0>\n"+
            "position=< 5,  9> velocity=< 1, -2>\n"+
            "position=<14,  7> velocity=<-2,  0>\n"+
            "position=<-3,  6> velocity=< 2, -1>";

    private static Set<Star> TEST_STARS =  Sets.newHashSet(new Star(9,  1, 0,  2),
            new Star(7,  0,-1,  0),
            new Star(3, -2,-1,  1),
            new Star(6, 10,-2, -1),
            new Star(2, -4, 2,  2),
            new Star(-6, 10, 2, -2),
            new Star(1,  8, 1, -1),
            new Star(1,  7, 1,  0),
            new Star(-3, 11, 1, -2),
            new Star(7,  6,-1, -1),
            new Star(-2,  3, 1,  0),
            new Star(-4,  3, 2,  0),
            new Star(10, -3,-1,  1),
            new Star(5, 11, 1, -2),
            new Star(4,  7, 0, -1),
            new Star(8, -2, 0,  1),
            new Star(15,  0,-2,  0),
            new Star(1,  6, 1,  0),
            new Star(8,  9, 0, -1),
            new Star(3,  3,-1,  1),
            new Star(0,  5, 0, -1),
            new Star(-2,  2, 2,  0),
            new Star(5, -2, 1,  2),
            new Star(1,  4, 2,  1),
            new Star(-2,  7, 2, -2),
            new Star(3,  6,-1, -1),
            new Star(5,  0, 1,  0),
            new Star(-6,  0, 2,  0),
            new Star(5,  9, 1, -2),
            new Star(14,  7,-2,  0),
            new Star(-3,  6, 2, -1));

    @Test
    void buildStars() {
        Day10 day10 = new Day10(TEST_INPUT);
        assertEquals(TEST_STARS, day10.stars);
    }

    @Test
    void showTestInput() {
        Day10 day10 = new Day10(TEST_INPUT);
        day10.visualize(1);
    }
}
