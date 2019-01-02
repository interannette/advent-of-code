package org.interannette.day17;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class GroundScan {
    static final Pattern X_START_PATTERN = Pattern.compile("x=(\\d+), y=(\\d+)\\.\\.(\\d+)");
    static final Pattern Y_START_PATTERN = Pattern.compile("y=(\\d+), x=(\\d+)\\.\\.(\\d+)");

    enum Material {

        SAND('.'), CLAY('#'), WATER('~');

        Character symbol;

        Material(Character symbol) {
            this.symbol = symbol;
        }
    }

    Map<Integer, Map<Integer, Material>> scan = new HashMap<>();
    int yMax, yMin;

    public GroundScan(String input) {

        Map<Integer, Material> xCol = new HashMap<>();
        xCol.put(0, Material.WATER);
        scan.put(500, xCol);

        String[] lines = input.split("\n");
        for(String line : lines) {
            Matcher xMatcher = X_START_PATTERN.matcher(line);
            if(xMatcher.matches()) {

                int xVal = Integer.valueOf(xMatcher.group(1));
                int yStartVal = Integer.valueOf(xMatcher.group(2));
                int yEndVal = Integer.valueOf(xMatcher.group(3));

                xCol = scan.computeIfAbsent(xVal, x -> new HashMap<>());

                for(int y = yStartVal; y <= yEndVal; y++) {
                    xCol.put(y, Material.CLAY);
                }

            } else {
                Matcher yMatcher = Y_START_PATTERN.matcher(line);
                if(yMatcher.matches()) {
                    int yVal = Integer.valueOf(yMatcher.group(1));
                    int xStartVal = Integer.valueOf(yMatcher.group(2));
                    int xEndVal = Integer.valueOf(yMatcher.group(3));

                    for(int x = xStartVal; x <= xEndVal; x++) {
                        xCol = scan.computeIfAbsent(x, i -> new HashMap<>());
                        xCol.put(yVal, Material.CLAY);
                    }
                }
            }
        }


        yMax = scan.values().stream()
                .flatMap(m -> m.keySet().stream())
                .mapToInt(i -> i.intValue())
                .max()
                .getAsInt();

        yMin = scan.values().stream()
                .flatMap(m -> m.keySet().stream())
                .mapToInt(i -> i.intValue())
                .min()
                .getAsInt();

    }

    public void advanceWater() {

    }

    public String format() {
        Map<Integer, Map<Integer, Character>> yxScan = new HashMap<>(yMax - yMin);
        for(Map.Entry<Integer, Map<Integer, Material>> e : scan.entrySet()) {
            int x = e.getKey();
            Map<Integer, Material> yValues = e.getValue();
            for(int y = yMin; y <= yMax; y++) {
                Material material = yValues.getOrDefault(y, Material.SAND);
                Map<Integer, Character> yRow = yxScan.computeIfAbsent(y, i -> new HashMap<>());
                yRow.put(x, material.symbol);
            }
        }

        int xMax = yxScan.values().stream()
                .flatMap(m -> m.keySet().stream())
                .mapToInt(i -> i.intValue())
                .max()
                .getAsInt();

        int xMin = yxScan.values().stream()
                .flatMap(m -> m.keySet().stream())
                .mapToInt(i -> i.intValue())
                .min()
                .getAsInt();


        StringBuilder stringBuilder = new StringBuilder();
        for(int y = yMin; y <= yMax; y++) {
            Map<Integer, Character> yRow = yxScan.getOrDefault(y, new HashMap<>());
            for(int x = xMin-1; x <= xMax+1; x++) {
                stringBuilder.append(yRow.getOrDefault(x, Material.SAND.symbol));
            }
            stringBuilder.append("\n");
        }

        return stringBuilder.toString();
    }
}
