package org.interannette.day4;

import org.junit.jupiter.api.Test;

import java.time.LocalDate;

import java.time.LocalDateTime;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day4Test {

    static final String TEST_INPUT = "[1518-11-01 00:00] Guard #10 begins shift\n" +
            "[1518-11-01 00:05] falls asleep\n" +
            "[1518-11-01 00:25] wakes up\n" +
            "[1518-11-01 00:30] falls asleep\n" +
            "[1518-11-01 00:55] wakes up\n" +
            "[1518-11-01 23:58] Guard #99 begins shift\n" +
            "[1518-11-02 00:40] falls asleep\n" +
            "[1518-11-02 00:50] wakes up\n" +
            "[1518-11-03 00:05] Guard #10 begins shift\n" +
            "[1518-11-03 00:24] falls asleep\n" +
            "[1518-11-03 00:29] wakes up\n" +
            "[1518-11-04 00:02] Guard #99 begins shift\n" +
            "[1518-11-04 00:36] falls asleep\n" +
            "[1518-11-04 00:46] wakes up\n" +
            "[1518-11-05 00:03] Guard #99 begins shift\n" +
            "[1518-11-05 00:45] falls asleep\n" +
            "[1518-11-05 00:55] wakes up";

    @Test
    void dateParser() {
        LocalDateTime localDateTime = Day4.parseDateFromLine("[1518-11-01 00:00] Guard #10 begins shift");
        assertEquals(LocalDateTime.of(1518, 11, 1, 0,0), localDateTime);
    }

    @Test
    void solveStar1() {
        Day4 day4 = new Day4(TEST_INPUT);
        assertEquals(240, day4.solveStar1());
    }

    @Test
    void solveStar2() {
        Day4 day4 = new Day4(TEST_INPUT);
        assertEquals(4455, day4.solveStar2());
    }

    @Test
    void testShiftConstructor() {
        List<Shift> shifts = new LinkedList();
        shifts.add(Shift.builder()
                .guard("10")
                .sleepingMinutes(IntStream.rangeClosed(5,24).boxed().collect(Collectors.toList()))
                .sleepingMinutes(IntStream.rangeClosed(30,54).boxed().collect(Collectors.toList()))
                .date(LocalDate.of(1518, 11,1))
                .build());
        shifts.add(Shift.builder()
                .guard("99")
                .sleepingMinutes(IntStream.rangeClosed(40,49).boxed().collect(Collectors.toList()))
                .date(LocalDate.of(1518, 11,2))
                .build());
        shifts.add(Shift.builder()
                .guard("10")
                .sleepingMinutes(IntStream.rangeClosed(24,28).boxed().collect(Collectors.toList()))
                .date(LocalDate.of(1518, 11,3))
                .build());
        shifts.add(Shift.builder()
                .guard("99")
                .sleepingMinutes(IntStream.rangeClosed(36,45).boxed().collect(Collectors.toList()))
                .date(LocalDate.of(1518, 11,4))
                .build());
        shifts.add(Shift.builder()
                .guard("99")
                .sleepingMinutes(IntStream.rangeClosed(45,54).boxed().collect(Collectors.toList()))
                .date(LocalDate.of(1518, 11,5))
                .build());

        Day4 day4 = new Day4(TEST_INPUT);
        assertEquals(shifts, day4.shifts);
    }
}
