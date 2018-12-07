package org.interannette.day6;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class Coordinate {
    int x;
    int y;

    public Coordinate(String line) {
        String[] parts = line.split(", ");
        this.x = Integer.parseInt(parts[0]);
        this.y = Integer.parseInt(parts[1]);
    }

    public int distance(Coordinate c) {
        return Math.abs(x - c.x) + Math.abs(y - c.y);
    }
}
