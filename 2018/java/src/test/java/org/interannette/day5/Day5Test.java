package org.interannette.day5;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class Day5Test {

    @Test
    void polarityTest() {
        assertTrue(Day5.areOppositePolarity("a", "A"));
        assertFalse(Day5.areOppositePolarity("a","B"));
        assertFalse(Day5.areOppositePolarity("a","a"));
    }

    @Test
    void reduceListTest() {
        assertEquals(Arrays.asList("dabAaCBAcaDA".split("")),
                Day5.reduceList(Arrays.asList("dabAcCaCBAcCcaDA".split(""))));
        assertEquals(Arrays.asList("dabCBAcaDA".split("")),
                Day5.reduceList(Arrays.asList("dabAaCBAcaDA".split(""))));
        assertEquals(Arrays.asList("dabCBAcaDA".split("")),
                Day5.reduceList(Arrays.asList("dabCBAcaDA".split(""))));
    }

    @Test
    void solveStar1() {
        Day5 day5 = new Day5("dabAcCaCBAcCcaDA");
        assertEquals(10, day5.solveStar1());
    }


}
