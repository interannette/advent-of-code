package org.interannette.day3;

import lombok.Data;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

@Data
public class Claim {

    static final String INPUT_REGEX = "#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)";
    static final Pattern INPUT_PATTERN = Pattern.compile(INPUT_REGEX);
    String id;
    int x;
    int y;
    int width;
    int height;

    public Claim(String inputString) {
        Matcher m = INPUT_PATTERN.matcher(inputString);
        if(m.matches()) {
            this.id = m.group(1);
            this.x = Integer.valueOf(m.group(2));
            this.y = Integer.valueOf(m.group(3));
            this.width = Integer.valueOf(m.group(4));
            this.height = Integer.valueOf(m.group(5));
        }
    }
}
