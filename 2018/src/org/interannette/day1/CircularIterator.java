package org.interannette.day1;

import java.util.Iterator;
import java.util.List;

public class CircularIterator implements Iterator<Integer> {

    private List<Integer> list;
    private int currentPosition;

    public CircularIterator(List<Integer> list) {
        this.list = list;
        this.currentPosition = 0;
    }

    @Override
    public boolean hasNext() {
        return true;
    }

    @Override
    public Integer next() {
        return list.get((currentPosition++ % list.size()));
    }
}
