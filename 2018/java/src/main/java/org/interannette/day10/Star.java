package org.interannette.day10;

import lombok.Data;

import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

@Data
public class Star {
    int x, y, deltaX, deltaY;

    public Star(int x, int y, int deltaX, int deltaY) {
        this.x = x;
        this.y = y;
        this.deltaX = deltaX;
        this.deltaY = deltaY;
    }

    public void move() {
        x += deltaX;
        y += deltaY;
    }

    public static boolean print(Collection<Star> stars) {
        int minX  = stars.stream().mapToInt(s -> s.x).min().getAsInt();
        int maxX = stars.stream().mapToInt(s -> s.x).max().getAsInt();
        int xRange = Math.abs(maxX-minX);

        List<Integer> sortedYValues = stars.stream().map(s -> s.y).distinct().sorted().collect(Collectors.toList());
        int yRange = Math.abs(sortedYValues.get(sortedYValues.size()-1) - sortedYValues.get(0));

        if(xRange * yRange > 20 * stars.size()) {
            //System.out.println("Too spread out");
            return false;
        }

        for(int i = 0; i < sortedYValues.size() - 1; i++) {
            if(sortedYValues.get(i)+1 != sortedYValues.get(i+1)) {
                //System.out.println("Gap in rows");
                return false;
            }
        }

        Map<Integer, Set<Integer>> yx = new HashMap<>(sortedYValues.size());
        for(Star star : stars) {
            yx.computeIfAbsent(star.y, y -> new HashSet<>()).add(star.x);
        }

        StringBuilder builder = new StringBuilder();
        for(int i = sortedYValues.get(0); i <= sortedYValues.get(sortedYValues.size() - 1); i++) {
            Set<Integer> row = yx.get(i);
            if(row == null) {
                //System.out.println("Missing row");
                return false;
            }

            for(int j = minX; j <= maxX; j++) {
                builder.append(row.contains(j) ? "#" : ".");
            }

            builder.append("\n");
        }
        System.out.print(builder.toString());
        return true;
    }
}
