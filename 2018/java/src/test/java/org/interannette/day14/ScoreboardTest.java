package org.interannette.day14;

import com.google.common.collect.Lists;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ScoreboardTest {
    @Test
    void sampleWalkthrough() {
        Scoreboard scoreboard = new Scoreboard(10);

        assertEquals(3, scoreboard.getScoreForElf1());
        assertEquals(7, scoreboard.getScoreForElf2());

        scoreboard.addRecipes(Lists.newArrayList(1,0));

        scoreboard.advanceElves();

        assertEquals(3, scoreboard.getScoreForElf1());
        assertEquals(7, scoreboard.getScoreForElf2());
    }
}
