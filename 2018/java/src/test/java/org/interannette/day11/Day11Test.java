package org.interannette.day11;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day11Test {

    @Test
    void hundredsDigit() {
        assertEquals(3, Day11.hundredsDigit(12345));
        assertEquals(0, Day11.hundredsDigit(10));
        assertEquals(0, Day11.hundredsDigit(1000));
    }


    @Test
    void sampleInput1() {
        Day11 day11 = new Day11(18);
        assertEquals(new GridCell(33, 45), day11.solveDay1());
    }

    @Test
    void sampleInput2() {
        Day11 day11 = new Day11(42);
        assertEquals(new GridCell(21,61), day11.solveDay1());
    }

    @ParameterizedTest
    @MethodSource("powerLevelTestCases")
    void powerLevel(PowerLevelTestCase powerLevelTestCase) {
        assertEquals(powerLevelTestCase.powerLevel,
                Day11.powerLevel(powerLevelTestCase.x, powerLevelTestCase.y, powerLevelTestCase.serialNumber));
    }

    static Stream<PowerLevelTestCase> powerLevelTestCases() {
        return Stream.of(
                new PowerLevelTestCase(3,5, 8, 4),
                new PowerLevelTestCase(122,79, 57, -5),
                new PowerLevelTestCase(217,196, 39, 0),
                new PowerLevelTestCase(101,153, 71, 4));
    }

    private static class PowerLevelTestCase {
        int x, y;
        int serialNumber;
        int powerLevel;

        public PowerLevelTestCase(int x, int y, int serialNumber, int powerLevel) {
            this.x = x;
            this.y = y;
            this.serialNumber = serialNumber;
            this.powerLevel = powerLevel;
        }
    }
}
