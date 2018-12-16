package org.interannette.day12;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class GrowthRuleTest {

    @Test
    void testNegativeParse() {
        GrowthRule rule = GrowthRule.parseRule("..#.. => .");
        assertEquals(100, rule.startState);
        assertFalse(rule.result);
    }

    @Test
    void testPositiveParse() {
        GrowthRule rule = GrowthRule.parseRule(".##.# => #");
        assertEquals(1101, rule.startState);
        assertTrue(rule.result);
    }
}
