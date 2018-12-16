package org.interannette.day12;

public class Pot {
    boolean present;
    int number;
    Pot nextPot;
    Pot previousPot;

    public Pot(int number, boolean present) {
        this.present = present;
        this.number = number;
    }

    public Pot(int number, char state) {
        this.number = number;
        this.present = state == '#';
    }

    public static Pot parseInput(String input) {
        char[] intialStateChars = input.replace("initial state: ", "").trim().toCharArray();

        Pot head = new Pot(-3, false);
        Pot negitiveTwo = new Pot(-2, false);
        Pot negitiveOne = new Pot(-1, false);
        head.nextPot = negitiveTwo;
        negitiveTwo.previousPot = head;

        negitiveTwo.nextPot = negitiveOne;
        negitiveOne.previousPot = negitiveTwo;

        Pot currentPot = negitiveOne;
        for(int i = 0; i < intialStateChars.length; i++) {

            Pot nextPot = new Pot(i, intialStateChars[i]);
            nextPot.previousPot = currentPot;

            currentPot.nextPot = nextPot;

            currentPot = nextPot;
        }

        return head;
    }

    @Override
    public String toString() {
        return "Pot{" +
                "present=" + present +
                ", number=" + number +
                ", nextPot=" + nextPot +
                ", previousPot=" + previousPot +
                '}';
    }
}
