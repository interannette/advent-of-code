package org.interannette.day16;

import com.google.common.collect.Sets;
import org.junit.jupiter.api.Test;

import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day16Test {
    @Test
    void sampleInput() {
        String[] sampleInput = {"Before: [3, 2, 1, 1]",
                "9 2 1 2",
                "After:  [3, 2, 2, 1]"};
        Sample sample = new Sample(sampleInput);

        Set<Operation.Name> matchingOperations = Day16.matchingOperations(sample);
        Set<Operation.Name> expectedMatches = Sets.newHashSet(Operation.Name.MULTR, Operation.Name.ADDI, Operation.Name.SETI);
        assertEquals(expectedMatches, matchingOperations);
    }
}
