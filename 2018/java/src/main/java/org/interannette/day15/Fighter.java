package org.interannette.day15;

import lombok.Data;

import java.util.Comparator;

@Data
public class Fighter implements Comparable<Fighter>{
    Team team;
    int row, col;
    int hitPoints = 200;
    int attackStrength = 3;

    public Fighter(Team team, int row, int col) {
        this.team = team;
        this.row = row;
        this.col = col;
    }

    public static Fighter goblin(int row, int col) {
        return new Fighter(Team.GOBLIN, row, col);
    }

    public static Fighter elf(int row, int col) {
        return new Fighter(Team.ELF, row, col);
    }

    @Override
    public int compareTo(Fighter o) {
        if(row != o.row) {
            return o.row - row;
        } else {
            return o.col - col;
        }
    }

    enum Team {
        ELF,GOBLIN
    }
}
