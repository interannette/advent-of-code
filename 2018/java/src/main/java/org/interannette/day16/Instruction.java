package org.interannette.day16;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Instruction {

    static final Pattern INSTRUCTION_LINE = Pattern.compile("(?<opp>\\d+) (?<input1>\\d+) (?<input2>\\d+) (?<output>\\d+)");

    int opperation;
    int input1;
    int input2;
    int output;

    public Instruction(String input) {
        Matcher instructionMatcher = INSTRUCTION_LINE.matcher(input.trim());
        if(instructionMatcher.matches()) {
            opperation = Integer.valueOf(instructionMatcher.group("opp"));
            input1 = Integer.valueOf(instructionMatcher.group("input1"));
            input2 = Integer.valueOf(instructionMatcher.group("input2"));
            output = Integer.valueOf(instructionMatcher.group("output"));
        } else {
            throw new IllegalArgumentException("FREAK OUT - INSTRUCTION");

        }
    }
}
