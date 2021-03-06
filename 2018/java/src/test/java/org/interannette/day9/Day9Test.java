package org.interannette.day9;

import org.interannette.StarTestCase;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import java.math.BigInteger;
import java.util.Map;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day9Test {
    @Test
    void testInput() {
        Day9 day9 = new Day9(9, 25);
        Map.Entry<Integer, BigInteger> winnerEntry = day9.solveStar1();
        assertEquals((Integer)5, winnerEntry.getKey());
        assertEquals(BigInteger.valueOf(32), winnerEntry.getValue());
    }

    @ParameterizedTest
    @MethodSource("star1TestCases")
    void solveStar1(StarTestCase<BigInteger> testCase) {
        Day9 day9 = new Day9(testCase.getInputString());
        assertEquals(testCase.getExpectedOutput(), day9.solveStar1().getValue());
    }

    static Stream<StarTestCase<BigInteger>> star1TestCases() {
        return Stream.of(
                new StarTestCase<>("10 players; last marble is worth 1618 points", BigInteger.valueOf(8317)),
                new StarTestCase<>("13 players; last marble is worth 7999 points", BigInteger.valueOf(146373)),
                new StarTestCase<>("17 players; last marble is worth 1104 points", BigInteger.valueOf(2764)),
                new StarTestCase<>("21 players; last marble is worth 6111 points", BigInteger.valueOf(54718)),
                new StarTestCase<>("30 players; last marble is worth 5807 points", BigInteger.valueOf(37305))
        );
    }
}
