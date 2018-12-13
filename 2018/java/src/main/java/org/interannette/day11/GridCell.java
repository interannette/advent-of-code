package org.interannette.day11;

import lombok.Data;

@Data
public class GridCell {

    int x,y;

    public GridCell(int x, int y) {
        this.x = x;
        this.y = y;
    }

}
