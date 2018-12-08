package org.interannette.day7;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day7 {

    static String LINE_REGEX = "Step (.+) must be finished before step (.+) can begin.";
    static Pattern LINE_PATTERN = Pattern.compile(LINE_REGEX);

    public static void main(String[] args) throws IOException {
        Day7 day7 = new Day7(InputGetter.getInput(7));
        System.out.println("Path to completion: " + day7.solveStar1());
    }

    DirectedGraph directedGraph;

    public Day7(String input) {
        String[] lines = input.split("\n");
        directedGraph = new DirectedGraph();

        Arrays.stream(lines).forEach(l -> {
                Matcher m = LINE_PATTERN.matcher(l);
                if(m.matches()) {
                    String from = m.group(1);
                    String to = m.group(2);
                    directedGraph.addRelationship(from, to);
                }
            }
        );
    }

    public String solveStar1() {
        /*
        Your first goal is to determine the order in which the steps should be completed.
        If more than one step is ready, choose the step which is first alphabetically.
         */

        StringBuilder result = new StringBuilder();
        List<String> availableNodes = directedGraph.nodesWithoutInbound();
        while(!availableNodes.isEmpty()) {
            availableNodes.sort(Comparator.naturalOrder());
            String nextNode = availableNodes.get(0);
            result.append(nextNode);
            directedGraph.removeNode(nextNode);
            availableNodes = directedGraph.nodesWithoutInbound();
        }

        return result.toString();
    }
}
