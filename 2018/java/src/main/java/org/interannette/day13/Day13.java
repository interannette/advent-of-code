package org.interannette.day13;

import org.interannette.InputGetter;

import java.awt.*;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public class Day13 {

    char[][] map;
    List<Cart> carts;
    int currentTick = 0;

    public static void main(String[] args) throws IOException {
        Day13 star1 = new Day13(InputGetter.getInput(13));
        System.out.println("First collision is at " + star1.solveStar1());

        Day13 star2 = new Day13(InputGetter.getInput(13));
        System.out.println("Remaining cart location " + star1.solveStar2());

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

    public void advanceTick(boolean continueAfterColision) throws CollisionException {
        List<Cart> cartsToRemove = new ArrayList<>();
        for(Cart cart : carts) {
            if(cartsToRemove.contains(cart)) {
                continue;
            }

            char currentTrack = map[cart.row][cart.col];
            cart.advance(currentTrack);

            // check if crash
            Optional<Cart> colidingCart = carts.stream()
                    .filter(c -> c != cart)
                    .filter(c -> c.compareTo(cart) == 0)
                    .findAny();

            if(colidingCart.isPresent()) {
                if(!continueAfterColision) {
                    throw new CollisionException(cart.row, cart.col, ++currentTick);
                } else {
                    System.out.println("Removing carts on tick " + (currentTick + 1));
                    cartsToRemove.add(cart);
                    cartsToRemove.add(colidingCart.get());
                }
            }
        }

        currentTick++;

        carts = carts.stream().filter(c -> !cartsToRemove.contains(c)).sorted().collect(Collectors.toList());
    }

    public String solveStar1() {
        boolean collision = false;
        while(!collision) {
            try {
                advanceTick(false);
                System.out.println("Tick " + currentTick);
            } catch (CollisionException e) {
                collision = true;
                return e.col + "," + e.row;
            }
        }
        return null;
    }

    public String solveStar2() {
        while(carts.size() > 1) {
            try {
                advanceTick(true);
                System.out.println("Tick " + currentTick);
            } catch (CollisionException e) {
                // wont happen
            }
        }

        if(carts.size() == 0) {
            return "even number of carts, none left";
        } else {
            Cart lastCart = carts.get(0);
            return lastCart.col + "," + lastCart.row;
        }
    }
}
