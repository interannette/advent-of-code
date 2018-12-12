package org.interannette.day10;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day10 {

    private static final Pattern INPUT_LINE_PATTERN = Pattern.compile("position=<\\s*(-?\\d+),\\s*(-?\\d+)> velocity=<\\s*(-?\\d+),\\s*(-?\\d+)>");

    public static void main(String[] args) throws IOException {
        Day10 day10 = new Day10(InputGetter.getInput(10));
        day10.visualize(1000);
    }

    Set<Star> stars;

    public Day10(String input) {
        String[] lines = input.split("\n");

        stars = new HashSet<>(lines.length);

        for(String line : lines) {
            Matcher m = INPUT_LINE_PATTERN.matcher(line);
            if(m.matches()) {
                stars.add(new Star(Integer.valueOf(m.group(1)),
                        Integer.valueOf(m.group(2)),
                        Integer.valueOf(m.group(3)),
                        Integer.valueOf(m.group(4))));
            }
        }
    }

    public void visualize(int stoppedTreshold) {
        int i = 1;
        boolean started = false;
        int stoppedFor = 0;
        while(stoppedFor < stoppedTreshold) {
            stars.stream().forEach(s -> s.move());
            if (Star.print(stars)) {
                started = true;
                System.out.println(i);
            } else {
                if(started) {
                    stoppedFor++;
                }
            }
            i++;
        }
    }
}
