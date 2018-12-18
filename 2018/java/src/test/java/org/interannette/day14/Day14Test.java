package org.interannette.day14;

import com.google.common.collect.Lists;
import org.interannette.StarTestCase;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day14Test {
    @Test
    void testCombineRecipes() {
        assertEquals(Lists.newArrayList(1, 0), Day14.combineRecipes(3,7));
        assertEquals(Lists.newArrayList(5), Day14.combineRecipes(2,3));
    }


    @ParameterizedTest
    @MethodSource("star1TestCases")
    void testGetNextTenAfter(StarTestCase<String> testCase) {
        assertEquals(testCase.getExpectedOutput(), Day14.getNextTenAfter(Integer.valueOf(testCase.getInputString())));
    }

    static Stream<StarTestCase<String>> star1TestCases() {
        return Stream.of(
                new StarTestCase<>("9","5158916779"),
                new StarTestCase<>("5","0124515891"),
                new StarTestCase<>("18","9251071085"),
                new StarTestCase<>("2018","5941429882"));
    }

    @ParameterizedTest
    @MethodSource("star2TestCases")
    void testFindFirstInstanceOf(StarTestCase<Integer> testCase) {
        assertEquals(testCase.getExpectedOutput(), Day14.findFirstInstanceOf(testCase.getInputString()));
    }

    static Stream<StarTestCase<Integer>> star2TestCases() {
        return Stream.of(
                new StarTestCase<>("51589",9),
                new StarTestCase<>("01245",5),
                new StarTestCase<>("92510",18),
                new StarTestCase<>("59414",2018));
    }

}
