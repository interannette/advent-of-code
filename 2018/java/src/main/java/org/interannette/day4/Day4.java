package org.interannette.day4;

import org.interannette.InputGetter;

import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.SortedMap;
import java.util.TreeMap;
import java.util.function.Function;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Day4 {

    private static final String LINE_REGEX = "^\\[(.*)\\].*$";
    private static final Pattern LINE_PATTERN = Pattern.compile(LINE_REGEX);

    private static final String GUARD_REGEX = "^.*Guard #(\\d+) begins shift";
    private static final Pattern GUARD_PATTERN = Pattern.compile(GUARD_REGEX);

    private static final String SLEEP_REGEX = ".*falls asleep.*";
    private static final String WAKE_REGEX = ".*wakes up.*";

    private static final DateTimeFormatter DATE_TIME_FORMATTER = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm", Locale.ENGLISH);

    public static void main(String[] args) throws IOException {
        Day4 day4 = new Day4(InputGetter.getInput(4));
        System.out.println("Strategy 1 finds: " + day4.solveStar1());
        System.out.println("Strategy 2 finds: " + day4.solveStar2());
    }

    List<Shift> shifts;

    static LocalDateTime parseDateFromLine(String l) {
        Matcher m = LINE_PATTERN.matcher(l);

        if(!m.matches()) {
            throw new RuntimeException("Could not parse " + l);
        }

        String dateAsString = m.group(1);
        return DATE_TIME_FORMATTER.parse(dateAsString, LocalDateTime::from);
    }

    public Day4(String inputString) {
        String[] lines = inputString.split("\n");

        // this will break if we have duplicate times
        Map<LocalDateTime, String> linesByDate = Arrays.stream(lines).collect(Collectors.toMap(
                Day4::parseDateFromLine,
                Function.identity()));

        SortedMap<LocalDateTime, String> linesInOrderByDate = new TreeMap<>(linesByDate);

        shifts = new LinkedList<>();


        // This will break if they don't go: (begin, (asleep, wake)*)*
        Shift.ShiftBuilder inProgressShift = null;
        Map.Entry<LocalDateTime, String> previousEntry = null;
        for(Map.Entry<LocalDateTime, String> lineWithDate : linesInOrderByDate.entrySet()) {

            String currentLine = lineWithDate.getValue();

            // handle the first line
            if(inProgressShift == null) {
                Matcher guardMatcher = GUARD_PATTERN.matcher(lineWithDate.getValue());
                if(guardMatcher.matches()) {
                    inProgressShift = Shift.builder().guard(guardMatcher.group(1));
                }
            } else if(currentLine.matches(SLEEP_REGEX)) {
                // Cheating, just look at previous on the wake
            } else if(currentLine.matches(WAKE_REGEX)) {

                inProgressShift.sleepingMinutes(IntStream.range(
                        previousEntry.getKey().getMinute(),
                        lineWithDate.getKey().getMinute())
                        .boxed()
                        .collect(Collectors.toList()));

            } else {

                // sometimes they start early so we need to get the date of the shift from the last entry
                shifts.add(inProgressShift
                        .date(previousEntry.getKey().toLocalDate())
                        .build());

                Matcher guardMatcher = GUARD_PATTERN.matcher(lineWithDate.getValue());
                if(guardMatcher.matches()) {
                    inProgressShift = Shift.builder().guard(guardMatcher.group(1));
                }
            }

            previousEntry = lineWithDate;
        }

        // close out last shift
        shifts.add(inProgressShift
                .date(previousEntry.getKey().toLocalDate())
                .build());
    }

    public int solveStar1() {
        Map<String, Integer> guardsWithSleepingMinutes = shifts.stream()
                .filter(s -> s.sleepingMinutes.size() > 0)
                .collect(Collectors.toMap(
                s -> s.guard,
                s -> s.sleepingMinutes.size(),
                (n,e) -> n + e));

        Optional<Map.Entry<String, Integer>> maxSleepEntry = guardsWithSleepingMinutes.entrySet().stream()
                .max(Comparator.comparingInt(e -> e.getValue()));

        String sleepiestGuardId = maxSleepEntry.get().getKey();

        List<Shift> shiftsMatchingGuard = shifts.stream().filter(s -> sleepiestGuardId.equals(s.guard)).collect(Collectors.toList());

        Map.Entry<Integer, Long> minutesWithHighestSleepTotal = mostCommonSleepingMinuteAndTotal(shiftsMatchingGuard);


        return minutesWithHighestSleepTotal.getKey() * Integer.valueOf(sleepiestGuardId);
    }

    static Map.Entry<Integer, Long> mostCommonSleepingMinuteAndTotal(Collection<Shift> shiftsToCount) {
        Optional<Map.Entry<Integer, Long>> minutesWithHighestSleepTotal = shiftsToCount.stream().flatMap(s -> s.sleepingMinutes.stream())
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
                .entrySet()
                .stream()
                .max(Comparator.comparing(e -> e.getValue()));

        return minutesWithHighestSleepTotal.get();
    }

    public int solveStar2() {

        Map<String, Set<Shift>> shiftsByGuardId = shifts.stream()
                .filter(s -> s.sleepingMinutes.size() > 0)
                .collect(Collectors.groupingBy(s->s.guard, Collectors.toSet()));
        Map<String, Map.Entry<Integer, Long>> guardWithMostCommonSleepingMinuteAndTotal = shiftsByGuardId.entrySet()
                .stream()
                .collect(Collectors.toMap(e -> e.getKey(), e -> mostCommonSleepingMinuteAndTotal(e.getValue())));
        Map.Entry<String, Map.Entry<Integer, Long>> sleepiestGuardEntry = guardWithMostCommonSleepingMinuteAndTotal.entrySet().stream()
                .max(Comparator.comparing(e -> e.getValue().getValue()))
                .get();

        return Integer.valueOf(sleepiestGuardEntry.getKey()) * sleepiestGuardEntry.getValue().getKey().intValue();
    }
}
