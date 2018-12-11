package org.interannette.day9;

import org.interannette.InputGetter;

import java.io.IOException;
import java.math.BigInteger;
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
        Day9 star1 = new Day9(InputGetter.getInput(9));

        Map.Entry<Integer, BigInteger> winnerEntry = star1.solveStar1();
        System.out.println("Star 1: Elf " + winnerEntry.getKey() + " wins with high score " + winnerEntry.getValue());

        Day9 star2 = new Day9(InputGetter.getInput(9));
        winnerEntry = star2.solveStar2();
        System.out.println("Star 2: Elf " + winnerEntry.getKey() + " wins with high score " + winnerEntry.getValue());
    }


    int players;
    long marbles;

    Map<Integer, BigInteger> scoresByPlayer;
    Circle circle = new Circle();

    public Day9(int players, int marbles) {
        this.players = players;
        this.marbles = marbles;
        this.scoresByPlayer = IntStream.rangeClosed(1, players)
                .boxed()
                .collect(Collectors.toMap(Function.identity(), i -> BigInteger.ZERO));
    }

    public Day9(String input) {
        Matcher m = INPUT_PATTERN.matcher(input.trim());
        if(m.matches()) {
            players = Integer.valueOf(m.group(1));
            marbles = Long.valueOf(m.group(2));

            scoresByPlayer = IntStream.rangeClosed(1, players)
                    .boxed()
                    .collect(Collectors.toMap(Function.identity(), i -> BigInteger.ZERO));
        }
    }

    public Map.Entry<Integer, BigInteger> solveStar1() {
        playGameToCompletion();
        return scoresByPlayer.entrySet()
                .stream()
                .max(Comparator.comparing(Map.Entry::getValue))
                .get();
    }

    public Map.Entry<Integer, BigInteger> solveStar2 () {
        marbles = 100 * marbles;
        return solveStar1();
    }

    void playGameToCompletion() {
        int currentPlayer = 1;
        for(long i = 1; i <= marbles; i++) {
            if(i % 23 == 0) {
                BigInteger newScore = scoresByPlayer.get(currentPlayer)
                        .add(BigInteger.valueOf(i))
                        .add(circle.removeAt(-7));
                scoresByPlayer.put(currentPlayer, newScore);
            } else {
                circle.insertAfter(1, BigInteger.valueOf(i));
            }
            currentPlayer = incrementPlayer(currentPlayer);
        }
    }

    int incrementPlayer(int cur) {
        return (cur  == players) ? 1 : cur + 1;
    }
}
