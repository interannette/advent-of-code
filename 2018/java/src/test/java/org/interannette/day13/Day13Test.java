package org.interannette.day13;

import com.google.common.collect.Lists;
import org.junit.jupiter.api.Test;

import java.util.Collections;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

public class Day13Test {

    @Test
    void testSampleStar1() {
        String sample = "/->-\\        \n" +
                "|   |  /----\\\n" +
                "| /-+--+-\\  |\n" +
                "| | |  | v  |\n" +
                "\\-+-/  \\-+--/\n" +
                "  \\------/   ";

        // 7,3
        Day13 day13 = new Day13(sample);
        try {
            for (int i = 0; i <= 14; i++) {
                day13.advanceTick();
            }
            fail();
        } catch(CollisionException e) {
            assertEquals(3, e.row);
            assertEquals(7, e.col);
            assertEquals(14, e.tick);
        }
    }

    @Test
    void testAdvance() throws CollisionException {
        String sample = "/->-\\        \n" +
                "|   |  /----\\\n" +
                "| /-+--+-\\  |\n" +
                "| | |  | v  |\n" +
                "\\-+-/  \\-+--/\n" +
                "  \\------/   ";

        Day13 day13 = new Day13(sample);

        Cart cart1, cart2;
        cart1 = new Cart(0, 2, Cart.Direction.RIGHT);
        cart2 = new Cart(3, 9, Cart.Direction.DOWN);
        List<Cart> expectedCarts = Lists.newArrayList(cart1, cart2);
        assertEquals(expectedCarts, day13.carts);

        /*
/-->\
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \->--/
  \------/  */
        cart1.col += 1;
        cart2.row += 1;
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);
        /*
/---v
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+>-/
  \------/
        */
        cart1.col += 1;
        cart2.col += 1;
        cart2.direction = Cart.Direction.RIGHT;
        cart2.nextTurn = Cart.Turn.STRAIGHT;
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);

        /*
/---\
|   v  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+->/
  \------/
        */
        cart1.row += 1;
        cart1.direction = Cart.Direction.DOWN;
        cart2.col += 1;
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);
        /*
/---\
|   |  /----\
| /->--+-\  |
| | |  | |  |
\-+-/  \-+--^
  \------/
         */
        cart1.row += 1;
        cart2.col += 1;
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);
    /*
/---\
|   |  /----\
| /-+>-+-\  |
| | |  | |  ^
\-+-/  \-+--/
  \------/
     */
        cart1.col += 1;
        cart1.nextTurn = Cart.Turn.STRAIGHT;
        cart1.direction = Cart.Direction.RIGHT;
        cart2.direction = Cart.Direction.UP;
        cart2.row -= 1;
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);
    /*
/---\
|   |  /----\
| /-+->+-\  ^
| | |  | |  |
\-+-/  \-+--/
  \------/
     */
        cart1.col+=1;
        cart2.row-=1;
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);
/*
/---\
|   |  /----<
| /-+-->-\  |
| | |  | |  |
\-+-/  \-+--/
  \------/
 */
        cart1.col+=1;
        cart2.row-=1;
        Collections.sort(expectedCarts);
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);
/*
/---\
|   |  /---<\
| /-+--+>\  |
| | |  | |  |
\-+-/  \-+--/
  \------/
 */
        cart1.col+=1;
        cart1.nextTurn = Cart.Turn.RIGHT;
        cart2.col-=1;
        cart2.direction = Cart.Direction.LEFT;
        Collections.sort(expectedCarts);
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);

        /*
/---\
|   |  /--<-\
| /-+--+-v  |
| | |  | |  |
\-+-/  \-+--/
  \------/
         */
        cart1.col+=1;
        cart2.col-=1;
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);
        /*
/---\
|   |  /-<--\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/
         */
        cart1.row+=1;
        cart1.direction = Cart.Direction.DOWN;
        cart2.col-=1;
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);
        /*
/---\
|   |  /<---\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-<--/
  \------/
         */
        cart1.row+=1;
        cart2.col-=1;
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);
        /*
/---\
|   |  v----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \<+--/
  \------/
         */
        cart1.col-=1;
        cart1.direction = Cart.Direction.LEFT;
        cart1.nextTurn = Cart.Turn.LEFT;
        cart2.col-=1;
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);
        /*
/---\
|   |  /----\
| /-+--v-\  |
| | |  | |  |
\-+-/  ^-+--/
  \------/
         */
        cart1.col-=1;
        cart2.row+=1;
        cart2.direction = Cart.Direction.DOWN;
        day13.advanceTick();
        assertEquals(expectedCarts, day13.carts);
    }
}
