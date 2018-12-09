package org.interannette.day7;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class WorkerTask {
    String task;
    Integer remainingTime;
}
