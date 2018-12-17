package org.interannette.day13;

public class CollisionException extends Exception {
    int row;
    int col;
    int tick;

    public CollisionException(int row, int col, int tick) {
        this.row = row;
        this.col = col;
        this.tick = tick;
    }
}
