package org.interannette.day9;

import lombok.Data;

import java.math.BigInteger;

@Data
public class DoubleLinkedNode {
    BigInteger value;
    DoubleLinkedNode clockwise;
    DoubleLinkedNode counterClockwise;
}
