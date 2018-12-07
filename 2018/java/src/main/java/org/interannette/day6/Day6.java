package org.interannette.day6;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Day6 {
    public static void main(String[] args) throws IOException {
        Day6 day6 = new Day6(InputGetter.getInput(6));
        System.out.println("Maximum finite area: " + day6.solveStar1());
    }

    List<Coordinate> coordinateList;

    public Day6(String input) {
        String[] lines = input.split("\n");
        this.coordinateList = Arrays.stream(lines).map(line -> new Coordinate(line)).collect(Collectors.toList());
    }

    public Integer solveStar1() {
        int maxX, minX, maxY, minY;

        maxX = coordinateList.stream().mapToInt(c -> c.x).max().getAsInt();
        minX = coordinateList.stream().mapToInt(c -> c.x).min().getAsInt();
        maxY = coordinateList.stream().mapToInt(c -> c.y).max().getAsInt();
        minY = coordinateList.stream().mapToInt(c -> c.y).min().getAsInt();

        System.out.println("X Range " + minX + " to " + maxX +
                ". Y Range " + minY + " to " + maxY);

        Set<Coordinate> relevantGrid = makeRelevantGrid(minX, maxX, minY, maxY);

        System.out.println("Relevant grid size " + relevantGrid.size());

        Map<Coordinate, Optional<Coordinate>> relevantGridWithClosestPoint = relevantGrid.stream()
                .collect(Collectors.toMap(Function.identity(), c -> findClosestPoint(c)));

        // which ones are infinite?
        Set<Optional<Coordinate>> pointsWithInfiniteAreas = relevantGrid.stream()
                .filter(c -> c.x == minX || c.x == maxX || c.y == minY || c.y == maxY)
                .map(c -> relevantGridWithClosestPoint.get(c))
                .collect(Collectors.toSet());

        Map<Coordinate, Long> coordinateAreas = relevantGridWithClosestPoint.entrySet().stream()
                .filter(e -> e.getValue().isPresent())
                .filter(e -> !pointsWithInfiniteAreas.contains(e.getValue()))
                .map(e -> e.getValue().get())
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

         Optional<Map.Entry<Coordinate, Long>> maxEntry = coordinateAreas.entrySet()
                .stream()
                .max(Comparator.comparing(e -> e.getValue()));

         System.out.println("Coordinate " + maxEntry.get().getKey()+ " has area " + maxEntry.get().getValue());
         return maxEntry.get().getValue().intValue();
    }

    Optional<Coordinate> findClosestPoint(Coordinate c) {
        Map<Coordinate, Integer> pointsWithDistances = coordinateList.stream()
                .collect(Collectors.toMap(Function.identity(), p -> p.distance(c)));

        Optional<Map.Entry<Coordinate, Integer>> optionalMin = pointsWithDistances.entrySet()
                .stream()
                .min(Comparator.comparing(e -> e.getValue()));

        if(optionalMin.isPresent() &&
                Collections.frequency(pointsWithDistances.values(), optionalMin.get().getValue()) == 1) {
            return Optional.of(optionalMin.get().getKey());
        } else {
            return Optional.empty();
        }
    }

    Set<Coordinate> makeRelevantGrid(int minX, int maxX, int minY, int maxY) {

        /*
           We can draw a "relevant grid" based on the outer points. We need to extend a buffer
           around the outer points to account for situations like a point one in from the outer edge.
           Eventually, once you are far enough away, the outer edge point will be closer, but it can take
           up to another "side" of the rectangle.
         */


        int buffer = Math.max(Math.abs(maxX - minX), Math.abs(maxY - minY));
        Set<Coordinate> grid = new HashSet<>((maxX - minX + 2 * buffer) * (maxY - minY + 2* buffer));
        for(int i = minX - buffer; i <= maxX + buffer; i++) {
            for(int j = minY - buffer; j <= maxY + buffer; j++) {
                grid.add(new Coordinate(i,j));
            }
        }
        return grid;
    }
}
