package org.interannette.day3;

import org.interannette.StarTestCase;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day3Test {

    @ParameterizedTest
    @MethodSource("star1TestCases")
    void solveStar1(StarTestCase<Integer> testCase) {
        Day3 testDay = new Day3(testCase.getInputString());
        assertEquals(testCase.getExpectedOutput(), testDay.solveStar1());
    }

    static Stream<StarTestCase<Integer>> star1TestCases() {
        return Stream.of(
                new StarTestCase<>(
                        "#1 @ 1,3: 4x4\n" +
                        "#2 @ 3,1: 4x4\n" +
                        "#3 @ 5,5: 2x2",
                        4)
        );
    }

    @ParameterizedTest
    @MethodSource("star2TestCases")
    void solveStar2(StarTestCase<String> testCase) {
        Day3 testDay = new Day3(testCase.getInputString());
        assertEquals(testCase.getExpectedOutput(), testDay.solveStar2());
    }

    static Stream<StarTestCase<String>> star2TestCases() {
        return Stream.of(
                new StarTestCase<>(
                        "#1 @ 1,3: 4x4\n" +
                                "#2 @ 3,1: 4x4\n" +
                                "#3 @ 5,5: 2x2",
                        "3")
        );
    }
}
