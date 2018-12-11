package org.interannette.day9;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.Comparator;
import java.util.Map;
import java.util.function.Function;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Day9 {

    static Pattern INPUT_PATTERN = Pattern.compile("(\\d+) players; last marble is worth (\\d+) points");

    public static void main(String[] args) throws IOException {
        Day9 day9 = new Day9(InputGetter.getInput(9));

        Map.Entry<Integer, Integer> winnerEntry = day9.solveStar1();
        System.out.println("Elf " + winnerEntry.getKey() + " wins with high score " + winnerEntry.getValue());
    }


    int players;
    int marbles;

    Map<Integer, Integer> scoresByPlayer;
    Circle circle = new Circle();

    public Day9(int players, int marbles) {
        this.players = players;
        this.marbles = marbles;
        this.scoresByPlayer = IntStream.rangeClosed(1, players)
                .boxed()
                .collect(Collectors.toMap(Function.identity(), i -> 0));
    }

    public Day9(String input) {
        Matcher m = INPUT_PATTERN.matcher(input.trim());
        if(m.matches()) {
            players = Integer.valueOf(m.group(1));
            marbles = Integer.valueOf(m.group(2));

            scoresByPlayer = IntStream.rangeClosed(1, players)
                    .boxed()
                    .collect(Collectors.toMap(Function.identity(), i -> 0));
        }
    }

    public Map.Entry<Integer, Integer> solveStar1() {
        playGameToCompletion();
        return scoresByPlayer.entrySet()
                .stream()
                .max(Comparator.comparingInt(e -> e.getValue()))
                .get();
    }

    void playGameToCompletion() {
        int currentPlayer = 1;
        for(int i = 1; i <= marbles; i++) {
            if(i % 23 == 0) {
                int newScore = scoresByPlayer.get(currentPlayer) + i;
                newScore += circle.removeAt(-7);
                scoresByPlayer.put(currentPlayer, newScore);
            } else {
                circle.insertAfter(1, i);
            }
            currentPlayer = incrementPlayer(currentPlayer);
        }
    }

    int incrementPlayer(int cur) {
        return (cur  == players) ? 1 : cur + 1;
    }
}
