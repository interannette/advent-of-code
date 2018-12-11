package org.interannette.day9;

import lombok.Data;

@Data
public class DoubleLinkedNode {
    int value;
    DoubleLinkedNode clockwise;
    DoubleLinkedNode counterClockwise;
}
