package org.interannette.day13;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Optional;

public class Day13 {

    char[][] map;
    List<Cart> carts;
    int currentTick = 0;

    public static void main(String[] args) throws IOException {
        Day13 day13 = new Day13(InputGetter.getInput(13));
        System.out.println("First collision is at " + day13.solveStar1());
    }

    public Day13(String input) {
        String[] lines = input.split("\n");
        int rows = lines.length;
        int cols = lines[0].length();

        map = new char[rows][cols];
        carts = new ArrayList<>();

        for(int i = 0; i < lines.length ; i++) {
            char[] lineAsArray = lines[i].toCharArray();
            for(int j = 0; j < lineAsArray.length; j++) {
                Cart.Direction direction = Cart.Direction.parse(lineAsArray[j]);
                if(direction != null) {
                    carts.add(new Cart(i, j, direction));
                    if(direction == Cart.Direction.LEFT || direction == Cart.Direction.RIGHT) {
                        map[i][j] = '-';
                    } else {
                        map[i][j] = '|';
                    }
                } else {
                    map[i][j] = lineAsArray[j];
                }
            }
        }

        Collections.sort(carts);
    }

    public void advanceTick() throws CollisionException {
        for(Cart cart : carts) {
            char currentTrack = map[cart.row][cart.col];
            cart.advance(currentTrack);

            // check if crash
            Optional<Cart> colidingCart = carts.stream()
                    .filter(c -> c != cart)
                    .filter(c -> c.compareTo(cart) == 0)
                    .findAny();

            if(colidingCart.isPresent()) {
                throw new CollisionException(cart.row, cart.col, ++currentTick);
            }
        }

        currentTick++;

        Collections.sort(carts);
    }

    public String solveStar1() {
        boolean collision = false;
        while(!collision) {
            try {
                advanceTick();
                System.out.println("Tick " + currentTick);
            } catch (CollisionException e) {
                collision = true;
                return e.col + "," + e.row;
            }
        }
        return null;
    }
}
