package org.interannette.day16;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Sample {
    static final Pattern BEFORE_LINE = Pattern.compile("Before: \\[(\\d), (\\d), (\\d), (\\d)\\]");
    static final Pattern AFTER_LINE = Pattern.compile("After:  \\[(\\d), (\\d), (\\d), (\\d)\\]");

    int[] before = new int[4];
    int[] after = new int[4];

    Instruction instruction;

    public Sample(String[] lines) {

        Matcher beforeMatcher = BEFORE_LINE.matcher(lines[0].trim());
        if(beforeMatcher.matches()) {
            before[0] = Integer.valueOf(beforeMatcher.group(1));
            before[1] = Integer.valueOf(beforeMatcher.group(2));
            before[2] = Integer.valueOf(beforeMatcher.group(3));
            before[3] = Integer.valueOf(beforeMatcher.group(4));
        } else {
            throw new IllegalArgumentException("FREAK OUT - BEFORE");
        }

        instruction = new Instruction(lines[1]);

        Matcher afterMatcher = AFTER_LINE.matcher(lines[2].trim());
        if(afterMatcher.matches()) {
            after[0] = Integer.valueOf(afterMatcher.group(1));
            after[1] = Integer.valueOf(afterMatcher.group(2));
            after[2] = Integer.valueOf(afterMatcher.group(3));
            after[3] = Integer.valueOf(afterMatcher.group(4));
        } else {
            throw new IllegalArgumentException("FREAK OUT - AFTER");
        }

    }
}
