package org.interannette.day15;

import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Day15 {
    static DistanceComparator distanceComparator = new DistanceComparator();
    Position[][] positions;
    List<Fighter> fighters;

    public Day15(String input) {
        String[] lines = input.split("\n");
        int rows = lines.length;
        int cols = lines[0].length();

        positions = new Position[rows][cols];

        for(int i = 0; i < lines.length; i++) {
            String currentLine = lines[i];
            for(int j = 0; j < currentLine.length(); j++) {
                char currentChar = currentLine.charAt(j);
                if(currentChar == '#') {
                    positions[i][j] = Position.WALL;
                } else if(currentChar == '.') {
                    positions[i][j] = Position.EMPTY;
                } else if(currentChar == 'E') {
                    positions[i][j] = Position.ELF;
                    fighters.add(Fighter.elf(i, j));
                } else if(currentChar == 'G') {
                    positions[i][j] = Position.GOBLIN;
                    fighters.add(Fighter.goblin(i, j));
                }
            }
        }
    }

    public void doRound() throws Exception {
        Collections.sort(fighters);
        for(Fighter fighter : fighters) {
            List<Fighter> targets = findTargets(fighter);
            if(targets.isEmpty()) {
                throw new Exception("out of targets");
            }


        }
    }

    private List<Fighter> findTargets(Fighter fighter) {
        return fighters.stream()
                .filter(f -> f.team != fighter.team)
                .sorted(distanceComparator)
                .collect(Collectors.toList());
    }

    enum Position {
        WALL, ELF, GOBLIN, EMPTY
    }


}
