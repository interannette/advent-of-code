package org.interannette.day12;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class PotTest {
    @Test
    void testParse() {
        Pot start = Pot.parseInput("#.#");

        assertEquals(-2, start.number);
        assertFalse(start.present);
        assertNull(start.previousPot);

        Pot negitiveOne = start.nextPot;
        assertEquals(-1, negitiveOne.number);
        assertFalse(negitiveOne.present);
        assertEquals(start, negitiveOne.previousPot);

        Pot zero = negitiveOne.nextPot;
        assertEquals(0, zero.number);
        assertTrue(zero.present);
        assertEquals(negitiveOne, zero.previousPot);

        Pot one = zero.nextPot;
        assertEquals(1, one.number);
        assertFalse(one. present);
        assertEquals(zero, one.previousPot);

        Pot two = one.nextPot;
        assertEquals(2, two.number);
        assertTrue(two.present);
        assertEquals(one, two.previousPot);
        assertNull(two.nextPot);

    }
}
