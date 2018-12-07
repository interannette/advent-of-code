package org.interannette.day6;

import lombok.Data;

import java.util.HashSet;
import java.util.Set;

@Data
public class Rectangle {
    int maxX, minX, maxY, minY;
    Set<Coordinate> coordinateSet;

    public Rectangle(int maxX, int minX, int maxY, int minY) {
        this.maxX = maxX;
        this.minX = minX;
        this.maxY = maxY;
        this.minY = minY;

        this.coordinateSet = new HashSet<>((maxX - minX) * (maxY - minY));
        for(int i = minX; i <= maxX; i++) {
            for(int j = minY; j <= maxY; j++) {
                coordinateSet.add(new Coordinate(i,j));
            }
        }
    }

    public boolean onBoundary(Coordinate c) {
        return c.x == minX || c.x == maxX || c.y == minY || c.y == maxY;
    }
}
