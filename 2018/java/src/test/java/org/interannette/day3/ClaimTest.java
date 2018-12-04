package org.interannette.day3;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ClaimTest {

    @Test
    void constructorParsing() {
        //#1 @ 1,3: 4x4
        String input = "#123 @ 3,2: 5x4";
        Claim claim = new Claim(input);

        assertEquals("123", claim.id);
        assertEquals(3, claim.x);
        assertEquals(2, claim.y);
        assertEquals(5, claim.width);
        assertEquals(4, claim.height);
    }
}
