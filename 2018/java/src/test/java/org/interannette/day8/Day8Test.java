package org.interannette.day8;

import com.google.common.collect.Lists;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day8Test {
    static String TEST_INPUT = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2";

    @Test
    void testTreeBuilding() {

        TreeNode d = new TreeNode(new ArrayList<>(), Lists.newArrayList(99));
        TreeNode c = new TreeNode(Lists.newArrayList(d), Lists.newArrayList(2));
        TreeNode b = new TreeNode(new ArrayList<>(), Lists.newArrayList(10,11,12));
        TreeNode a = new TreeNode(Lists.newArrayList(b,c), Lists.newArrayList(1,1,2));

        Day8 day8 = new Day8(TEST_INPUT);
        assertEquals(a, day8.treeRoot);
    }

    @Test
    void solveStar1() {
        Day8 day8 = new Day8(TEST_INPUT);
        assertEquals((Integer)138, day8.solveStar1());
    }

    @Test
    void solveStar2() {
        Day8 day8 = new Day8(TEST_INPUT);
        assertEquals((Integer)66, day8.solveStar2());
    }
}
