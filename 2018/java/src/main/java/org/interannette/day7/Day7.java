package org.interannette.day7;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day7 {

    static String LINE_REGEX = "Step (.+) must be finished before step (.+) can begin.";
    static Pattern LINE_PATTERN = Pattern.compile(LINE_REGEX);

    public static void main(String[] args) throws IOException {
//        Day7 printer = new Day7(InputGetter.getInput(7));
//        printer.printGraph();
//
//        Day7 day7Star1 = new Day7(InputGetter.getInput(7));
//        System.out.println("Sequence: " + day7Star1.solveStar1());

        Day7 day7Star2 = new Day7(InputGetter.getInput(7));
        System.out.println("Time to completion: " + day7Star2.solveStar2());
    }

    DirectedGraph directedGraph;
    int workerCount = 5;
    int taskDurationBase = 60;

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

    public void printGraph() {
        List<String> availableNodes = directedGraph.nodesWithoutInbound();
        while(!availableNodes.isEmpty()) {
            System.out.println(availableNodes);
            for(String node : availableNodes) {
                System.out.print(node + " [" + timeToProcess(node) + "] ");
                Set<String> nextNodes = directedGraph.getFromTo().get(node);
                if(nextNodes != null) {
                    for (String nextNode : directedGraph.getFromTo().get(node)) {
                        System.out.print(" (" + node + ", " + nextNode + ") ");
                    }
                }
                System.out.print("\n");
                directedGraph.removeNode(node);
            }
            availableNodes = directedGraph.nodesWithoutInbound();
        }
    }

    public String solveStar1() {

        if(directedGraph.getAll().isEmpty()) {
            throw new IllegalStateException("Day 7 can only be solved once. Graph must be reset");
        }

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

    public Integer solveStar2() {
        if(directedGraph.getAll().isEmpty()) {
            throw new IllegalStateException("Day 7 can only be solved once. Graph must be reset");
        }

        int seconds = -1;
        int totalTasks = directedGraph.getAll().size();
        Map<Integer, WorkerTask> workerTasks = new HashMap(workerCount);

        Set<String> startedTasks = new HashSet<>();

        boolean done = false;
        while(!done) {
            seconds++;
            // Each loop == one second
            for(int i = 0; i < workerCount; i++) {
                WorkerTask task = workerTasks.get(i);
                if(task == null || task.remainingTime == 0) {

                    if(task != null) {
                        directedGraph.removeNode(task.task);
                        workerTasks.remove(i);
                    }

                   for(String nextNode : directedGraph.nodesWithoutInbound()) {
                       if(!startedTasks.contains(nextNode)) {
                           workerTasks.put(i, new WorkerTask(nextNode, timeToProcess(nextNode) - 1));
                           startedTasks.add(nextNode);
                           break;
                       }
                   }

                } else {
                    task.remainingTime--;
                }
            }

            System.out.println("Workers at second " + seconds + ": " + workerTasks );

            boolean allWorkersDone = !workerTasks.values().stream()
                    .filter(t -> t != null)
                    .filter(t -> t.remainingTime > 0)
                    .findAny()
                    .isPresent();
            boolean haveRemainingNodes = (startedTasks.size() < totalTasks);
            done = allWorkersDone && !haveRemainingNodes;
        }

        return seconds;
    }

    Integer timeToProcess(String s) {
        // unicode - 4 = (A = 65)
        return s.charAt(0) - 64 + taskDurationBase;
    }
}
