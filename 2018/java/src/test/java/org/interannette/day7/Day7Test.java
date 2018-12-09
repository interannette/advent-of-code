package org.interannette.day7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day7Test {

    static String EXAMPLE_INPUT = "Step C must be finished before step A can begin.\n" +
            "Step C must be finished before step F can begin.\n" +
            "Step A must be finished before step B can begin.\n" +
            "Step A must be finished before step D can begin.\n" +
            "Step B must be finished before step E can begin.\n" +
            "Step D must be finished before step E can begin.\n" +
            "Step F must be finished before step E can begin.";

    @Test
    void parsing() {

        DirectedGraph directedGraph = new DirectedGraph();
        directedGraph.addRelationship("C","A");
        directedGraph.addRelationship("C","F");
        directedGraph.addRelationship("A","B");
        directedGraph.addRelationship("A","D");
        directedGraph.addRelationship("B","E");
        directedGraph.addRelationship("D","E");
        directedGraph.addRelationship("F","E");

        Day7 day7 = new Day7(EXAMPLE_INPUT);

        assertEquals(directedGraph, day7.directedGraph);
    }

    @Test
    void solveStar1() {
        Day7 day7 = new Day7(EXAMPLE_INPUT);
        assertEquals("CABDFE", day7.solveStar1());
    }

    @Test
    void solveStar2() {
        Day7 day7 = new Day7(EXAMPLE_INPUT);
        day7.workerCount = 2;
        day7.taskDurationBase = 0;
        assertEquals((Integer)15, day7.solveStar2());
    }

    @Test
    void charToSecondsTestInput() {
        Day7 day7 = new Day7(EXAMPLE_INPUT);
        day7.taskDurationBase = 0;
        assertEquals((Integer)1, day7.timeToProcess("A"));
        assertEquals((Integer)26, day7.timeToProcess("Z"));
    }

    @Test
    void charToSecondsStandardInput() {
        Day7 day7 = new Day7(EXAMPLE_INPUT);
        assertEquals((Integer)61, day7.timeToProcess("A"));
        assertEquals((Integer)86, day7.timeToProcess("Z"));
    }
}
