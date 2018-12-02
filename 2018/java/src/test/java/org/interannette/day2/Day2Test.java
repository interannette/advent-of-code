package org.interannette.day2;

import lombok.Data;
import org.interannette.StarTestCase;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.Map;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day2Test {

    @ParameterizedTest
    @MethodSource("star1TestCases")
    void solveStar1(StarTestCase<Long> testCase) {
        Day2 testDay = new Day2(testCase.getInputString());
        assertEquals(testCase.getExpectedOutput(), (Long)testDay.solveStar1());
    }

    static Stream<StarTestCase<Long>> star1TestCases() {
        return Stream.of(
                new StarTestCase<>("abcdef, bababc, abbcde, abcccd, aabcdd, abcdee, ababab", 12l)
        );
    }

    @ParameterizedTest
    @MethodSource("frequencyCounterTestCases")
    void countFrequencies(FrequencyCounterTestCase frequencyCounterTestCase) {
        Map<Long, Long> frequecyMap = Day2.countFrequencies(frequencyCounterTestCase.string);
        assertEquals(frequencyCounterTestCase.twos, frequecyMap.getOrDefault(2l, 0l));
        assertEquals(frequencyCounterTestCase.threes, frequecyMap.getOrDefault(3l, 0l));
    }

    static Stream frequencyCounterTestCases() {
        return Stream.of(
                new FrequencyCounterTestCase("abcdef", 0l, 0l)
        );
    }

    private static class FrequencyCounterTestCase {
        String string;
        Long twos;
        Long threes;

        public FrequencyCounterTestCase(String string, Long twos, Long threes) {
            this.string = string;
            this.twos = twos;
            this.threes = threes;
        }
    }
}
