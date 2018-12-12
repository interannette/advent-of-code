package org.interannette.day11;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class GridCellTest {

    @Test
    void hundredsDigit() {
        assertEquals(3, GridCell.hundredsDigit(12345));
        assertEquals(0, GridCell.hundredsDigit(10));
        assertEquals(0, GridCell.hundredsDigit(1000));
    }

    @ParameterizedTest
    @MethodSource("powerLevelTestCases")
    void powerLevel(PowerLevelTestCase powerLevelTestCase) {
        assertEquals(powerLevelTestCase.powerLevel, powerLevelTestCase.gridCell.powerLevel(powerLevelTestCase.serialNumber));
    }

    static Stream<PowerLevelTestCase> powerLevelTestCases() {
        return Stream.of(
                new PowerLevelTestCase(new GridCell(3,5), 8, 4),
                new PowerLevelTestCase(new GridCell(122,79), 57, -5),
                new PowerLevelTestCase(new GridCell(217,196), 39, 0),
                new PowerLevelTestCase(new GridCell(101,153), 71, 4));
    }

    private static class PowerLevelTestCase {
        GridCell gridCell;
        int serialNumber;
        int powerLevel;

        public PowerLevelTestCase(GridCell gridCell, int serialNumber, int powerLevel) {
            this.gridCell = gridCell;
            this.serialNumber = serialNumber;
            this.powerLevel = powerLevel;
        }
    }
}
