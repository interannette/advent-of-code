package org.interannette.day1;

import org.interannette.StarTestCase;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;


public class Day1Test {

    @ParameterizedTest
    @MethodSource("star1TestCases")
    void solveStar1(StarTestCase<Integer> testCase) {
        Day1 testDay = new Day1(testCase.getInputString());
        Assertions.assertEquals(testCase.getExpectedOutput(), testDay.solveStar1());
    }

    @ParameterizedTest
    @MethodSource("star2TestCases")
    void solveStar2(StarTestCase<Integer> testCase) {
        Day1 testDay = new Day1(testCase.getInputString());
        Assertions.assertEquals(testCase.getExpectedOutput(), testDay.solveStar2());
    }


    static Stream<StarTestCase<Integer>> star1TestCases() {
        return Stream.of(
                new StarTestCase<>("+1, -2, +3, +1", 3),
                new StarTestCase<>("+1, +1, +1", 3),
                new StarTestCase<>("+1, +1, -2", 0),
                new StarTestCase<>("-1, -2, -3", -6)
        );
    }


    static Stream<StarTestCase<Integer>> star2TestCases() {
        return Stream.of(
                new StarTestCase<>("+1, -2, +3, +1", 2),
                new StarTestCase<>("+1, -1", 0),
                new StarTestCase<>("+3, +3, +4, -2, -4", 10),
                new StarTestCase<>("-6, +3, +8, +5, -6", 5),
                new StarTestCase<>("+7, +7, -2, -7, -4", 14)
        );
    }

}
