package org.interannette.day13;

import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode
public class Cart implements Comparable<Cart> {
    int row;
    int col;
    Direction direction;
    Turn nextTurn = Turn.LEFT;

    public Cart(int row, int col, Direction direction) {
        this.row = row;
        this.col = col;
        this.direction = direction;
    }

    public void advance(char c) {
        if(c == '|' || c == '-') {
            moveStraight();
        } else if(c == '/') {
            rightCurve();
        } else if(c == '\\'){
            leftCurve();
        } else if(c == '+') {
            intersection();
        }
    }

    public void moveStraight() {
        switch (direction) {
            case UP:
                row--;
                break;
            case DOWN:
                row++;
                break;
            case LEFT:
                col--;
                break;
            case RIGHT:
                col++;
                break;
        }
    }

    // '/'
    public void rightCurve() {
        switch (direction){
            case LEFT:
                direction = Direction.DOWN;
                break;
            case RIGHT:
                direction = Direction.UP;
                break;
            case DOWN:
                direction = Direction.LEFT;
                break;
            case UP:
                direction = Direction.RIGHT;
                break;
        }
        moveStraight();
    }

    // '\'
    public void leftCurve() {
        switch (direction){
            case LEFT:
                direction = Direction.UP;
                break;
            case RIGHT:
                direction = Direction.DOWN;
                break;
            case DOWN:
                direction = Direction.RIGHT;
                break;
            case UP:
                direction = Direction.LEFT;
                break;
        }
        moveStraight();
    }

    public void intersection() {
        switch (nextTurn) {
            case RIGHT:
                switch (direction){
                    case LEFT:
                        direction = Direction.UP;
                        break;
                    case RIGHT:
                        direction = Direction.DOWN;
                        break;
                    case DOWN:
                        direction = Direction.LEFT;
                        break;
                    case UP:
                        direction = Direction.RIGHT;
                        break;
                }
                moveStraight();
                nextTurn = Turn.LEFT;
                break;
            case LEFT:
                switch (direction){
                    case LEFT:
                        direction = Direction.DOWN;
                        break;
                    case RIGHT:
                        direction = Direction.UP;
                        break;
                    case DOWN:
                        direction = Direction.RIGHT;
                        break;
                    case UP:
                        direction = Direction.LEFT;
                        break;
                }
                moveStraight();
                nextTurn = Turn.STRAIGHT;
                break;
            case STRAIGHT:
                moveStraight();
                nextTurn = Turn.RIGHT;
                break;
        }
    }

    @Override
    public int compareTo(Cart o) {
        if(this.row != o.row) {
            return Integer.compare(this.row, o.row);
        }

        if(this.col != o.col) {
            return Integer.compare(this.col, o.col);
        }

        return 0;
    }



    public enum Turn {
        LEFT, RIGHT, STRAIGHT;
    }

    public enum Direction {
        UP('^'), DOWN('v'), LEFT('<'), RIGHT('>');

        char represation;

        Direction(char represation) {
            this.represation = represation;
        }

        public static Direction parse(char represation) {
            if(represation == UP.represation) {
                return  UP;
            } else if(represation == DOWN.represation) {
                return DOWN;
            } else if(represation == LEFT.represation) {
                return LEFT;
            } else if(represation == RIGHT.represation) {
                return RIGHT;
            } else {
                return null;
            }
        }
    }


}
