package org.interannette.day4;

import lombok.Builder;
import lombok.Data;
import lombok.Singular;

import java.time.LocalDate;
import java.util.List;

@Data
@Builder
public class Shift {
    final String guard;
    final LocalDate date;
    @Singular
    final List<Integer> sleepingMinutes;
}
