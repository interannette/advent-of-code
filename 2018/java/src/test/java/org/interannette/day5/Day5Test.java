package org.interannette.day5;

import org.interannette.StarTestCase;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class Day5Test {

    @Test
    void polarityTest() {
        assertTrue(Day5.areOppositePolarity('a', 'A'));
        assertFalse(Day5.areOppositePolarity('a','B'));
        assertFalse(Day5.areOppositePolarity('a','a'));
    }

    @ParameterizedTest
    @MethodSource("star1TestCases")
    void solveStar1(StarTestCase<Integer> testCase) {
        Day5 day5 = new Day5(testCase.getInputString());
        assertEquals(testCase.getExpectedOutput(), day5.solveStar1());
    }

    static Stream<StarTestCase<Integer>> star1TestCases() {
        return Stream.of(
                new StarTestCase<>("dabAcCaCBAcCcaDA", 10),
                new StarTestCase<>("dDa", 1),
                new StarTestCase<>("aA", 0),
                new StarTestCase<>("abBA", 0),
                new StarTestCase<>("abAB", 4),
                new StarTestCase<>("aabAAB", 6)
        );
    }
}
