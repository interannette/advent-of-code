package org.interannette.day9;

import java.math.BigInteger;

public class Circle {
    DoubleLinkedNode currentNode;

    public Circle() {
        currentNode = new DoubleLinkedNode();
        currentNode.setValue(BigInteger.ZERO);
        currentNode.setCounterClockwise(currentNode);
        currentNode.setClockwise(currentNode);
    }

    void insertAfter(int stepsFromCurrent, BigInteger value) {
        for(int i = 0; i < Math.abs(stepsFromCurrent); i++) {
            if(stepsFromCurrent > 0) {
                currentNode = currentNode.clockwise;
            } else {
                currentNode = currentNode.counterClockwise;
            }
        }

        DoubleLinkedNode newNode = new DoubleLinkedNode();
        newNode.setValue(value);
        newNode.setCounterClockwise(currentNode);
        newNode.setClockwise(currentNode.clockwise);

        currentNode.setClockwise(newNode);
        newNode.clockwise.setCounterClockwise(newNode);

        currentNode = newNode;
    }

    BigInteger removeAt(int stepsFromCurrent) {
        for(int i = 0; i < Math.abs(stepsFromCurrent); i++) {
            if(stepsFromCurrent > 0) {
                currentNode = currentNode.clockwise;
            } else {
                currentNode = currentNode.counterClockwise;
            }
        }

        BigInteger value = currentNode.value;

        currentNode.counterClockwise.setClockwise(currentNode.clockwise);
        currentNode.clockwise.setCounterClockwise(currentNode.counterClockwise);

        currentNode = currentNode.clockwise;

        return value;
    }

    @Override
    public String toString() {
        DoubleLinkedNode copyOfFirstNode = currentNode;
        DoubleLinkedNode nodeBeingPrinted = currentNode;
        int i = 0;
        StringBuilder builder = new StringBuilder("Current node: " + nodeBeingPrinted.value.intValue());
        nodeBeingPrinted = nodeBeingPrinted.clockwise;

        while(nodeBeingPrinted != copyOfFirstNode) {
            builder.append(" -> ");
            builder.append(nodeBeingPrinted.value.intValue());
            nodeBeingPrinted = nodeBeingPrinted.clockwise;
        }

        return builder.toString();
    }
}
