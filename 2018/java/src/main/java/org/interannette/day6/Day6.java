package org.interannette.day6;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
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
        System.out.println("Region size: " + day6.solveStar2());
    }

    int maxDistanceStar2 = 10000;
    List<Coordinate> coordinateList;
    Rectangle relevantRectangle;

    public Day6(String input) {
        String[] lines = input.split("\n");
        this.coordinateList = Arrays.stream(lines).map(line -> new Coordinate(line)).collect(Collectors.toList());

        int maxX, minX, maxY, minY;

        maxX = coordinateList.stream().mapToInt(c -> c.x).max().getAsInt();
        minX = coordinateList.stream().mapToInt(c -> c.x).min().getAsInt();
        maxY = coordinateList.stream().mapToInt(c -> c.y).max().getAsInt();
        minY = coordinateList.stream().mapToInt(c -> c.y).min().getAsInt();

        this.relevantRectangle = new Rectangle(maxX, minX, maxY, minY);
    }

    public Integer solveStar1() {

        Map<Coordinate, Optional<Coordinate>> relevantGridWithClosestPoint = relevantRectangle.coordinateSet.stream()
                .collect(Collectors.toMap(Function.identity(), c -> findClosestPoint(c)));

        // which ones are infinite? the ones that are taking up the boundary of the rectangle
        Set<Optional<Coordinate>> pointsWithInfiniteAreas = relevantRectangle.coordinateSet.stream()
                .filter(c -> relevantRectangle.onBoundary(c))
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

    public long solveStar2() {
        return relevantRectangle.coordinateSet.stream()
                .map(c -> sumDistances(c))
                .filter(d -> d < maxDistanceStar2)
                .count();
    }

    Integer sumDistances(Coordinate c) {
        return coordinateList.stream().map(p -> p.distance(c)).mapToInt(i -> i.intValue()).sum();
    }
}
