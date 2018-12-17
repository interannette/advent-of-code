package org.interannette.day12;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

public class Day12Test {

    @Test
    void testSampleInputSolve() {
        Day12 day12 = new Day12("initial state: #..#.#..##......###...###\n" +
                "\n" +
                "...## => #\n" +
                "..#.. => #\n" +
                ".#... => #\n" +
                ".#.#. => #\n" +
                ".#.## => #\n" +
                ".##.. => #\n" +
                ".#### => #\n" +
                "#.#.# => #\n" +
                "#.### => #\n" +
                "##.#. => #\n" +
                "##.## => #\n" +
                "###.. => #\n" +
                "###.# => #\n" +
                "####. => #");

        assertEquals(325, day12.solveStar1());
    }

    @Test
    void testAdvancing() {
        Day12 day12 = new Day12("initial state: #..#.#..##......###...###\n" +
                "\n" +
                "...## => #\n" +
                "..#.. => #\n" +
                ".#... => #\n" +
                ".#.#. => #\n" +
                ".#.## => #\n" +
                ".##.. => #\n" +
                ".#### => #\n" +
                "#.#.# => #\n" +
                "#.### => #\n" +
                "##.#. => #\n" +
                "##.## => #\n" +
                "###.. => #\n" +
                "###.# => #\n" +
                "####. => #");

        String sample = "...#...#....#.....#..#..#..#...........\n" +
                "...##..##...##....#..#..#..##..........\n" +
                "..#.#...#..#.#....#..#..#...#..........\n" +
                "...#.#..#...#.#...#..#..##..##.........\n" +
                "....#...##...#.#..#..#...#...#.........\n" +
                "....##.#.#....#...#..##..##..##........\n" +
                "...#..###.#...##..#...#...#...#........\n" +
                "...#....##.#.#.#..##..##..##..##.......\n" +
                "...##..#..#####....#...#...#...#.......\n" +
                "..#.#..#...#.##....##..##..##..##......\n" +
                "...#...##...#.#...#.#...#...#...#......\n" +
                "...##.#.#....#.#...#.#..##..##..##.....\n" +
                "..#..###.#....#.#...#....#...#...#.....\n" +
                "..#....##.#....#.#..##...##..##..##....\n" +
                "..##..#..#.#....#....#..#.#...#...#....\n" +
                ".#.#..#...#.#...##...#...#.#..##..##...\n" +
                "..#...##...#.#.#.#...##...#....#...#...\n" +
                "..##.#.#....#####.#.#.#...##...##..##..\n" +
                ".#..###.#..#.#.#######.#.#.#..#.#...#..\n" +
                ".#....##....#####...#######....#.#..##.\n";
        String[] linesFromSample = sample.split("\n");

        List<Pot> expectedGeneations = new ArrayList<>(linesFromSample.length);
        for(int i = 0; i < linesFromSample.length; i++) {
            expectedGeneations.add(parseInput(linesFromSample[i]));
        }

        Pot actualGeneration = day12.potsHead;
        int i = 1;
        for(Pot expectedGeneration : expectedGeneations) {
            actualGeneration = day12.advanceGeneration(actualGeneration);
            assertState(expectedGeneration, actualGeneration);
            System.out.println("Generation " + i++ + " passes");
        }
    }

    void assertState(Pot expected, Pot actual) {
        while(actual != null || expected != null) {
            if(actual == null && expected != null) {
                while(expected != null) {
                    if(expected.present) {
                        fail("Actual is null. Expected " + expected.number + " is present");
                    } else {
                        expected = expected.nextPot;
                    }
                }
            } else if(actual != null && expected == null) {
                while(actual != null) {
                    if(actual.present) {
                        fail("Expected is null. Actual " + actual.number + " is present");
                    } else {
                        actual = actual.nextPot;
                    }
                }
            } else {
                assertEquals(actual.present, expected.present);
                assertEquals(actual.number, expected.number);
                actual = actual.nextPot;
                expected = expected.nextPot;
            }
        }
    }

    public static Pot parseInput(String input) {
        char[] intialStateChars = input.replace("initial state: ", "").trim().toCharArray();

        Pot head = new Pot(-3, intialStateChars[0]);

        Pot currentPot = head;
        for(int i = 1; i < intialStateChars.length; i++) {

            Pot nextPot = new Pot(i-3, intialStateChars[i]);
            nextPot.previousPot = currentPot;

            currentPot.nextPot = nextPot;

            currentPot = nextPot;
        }

        return head;
    }
}
