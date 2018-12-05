package org.interannette.day5;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day5 {

    public static void main(String[] args) throws IOException {
        Day5 day5 = new Day5(InputGetter.getInput(5));
        System.out.println("Star 1: " + day5.solveStar1());
        //System.out.println("Star 2: " + day5.solveStar2());
    }

    List<String> inputChars;

    public Day5(String inputString) {
        this.inputChars = Arrays.asList(inputString.split(""));
    }

    public int solveStar1() {

        List<String> original = inputChars;
        List<String> update = reduceList(inputChars);

        while(original.size() != update.size()) {
            original = update;
            update = reduceList(update);
        }

        return update.size();
    }

    static List<String> reduceList(List<String> characters) {
        List<String> updatedList = new ArrayList<>(characters.size());
        for(int i = 0; i < characters.size(); i++) {
            String thisChar = characters.get(i);
            if(i+1 == characters.size()) {
                // this is the last element, just add it;
                updatedList.add(thisChar);
            } else {
                String nextChar = characters.get(i + 1);
                if (areOppositePolarity(thisChar, nextChar)) {
                    i++; // skip this and the next char
                } else {
                    updatedList.add(thisChar);
                }
            }
        }
        return updatedList;
    }

    static boolean areOppositePolarity(String i, String j) {
        return !i.equals(j) && i.equalsIgnoreCase(j);
    }

    public String solveStar2() {
        return null;
    }
}
