package org.interannette.day16;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class SampleTest {
    @Test
    void testConstructor() {
        String[] sampleInput = {"Before: [3, 2, 1, 1]",
                "9 2 1 2",
                "After:  [3, 2, 2, 1]"};

        int[] expectedBefore = {3, 2, 1, 1};
        int[] expectedAfter = {3, 2, 2, 1};

        Sample sample = new Sample(sampleInput);
        assertTrue(Arrays.equals(expectedBefore, sample.before));
        assertTrue(Arrays.equals(expectedAfter, sample.after));
        assertEquals(9, sample.instruction.opperation);
        assertEquals(2, sample.instruction.input1);
        assertEquals(1, sample.instruction.input2);
        assertEquals(2, sample.instruction.output);
    }
}
