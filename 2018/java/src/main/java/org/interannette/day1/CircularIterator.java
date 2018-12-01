package org.interannette.day1;

import sun.reflect.generics.reflectiveObjects.NotImplementedException;

import java.util.Iterator;
import java.util.List;

public class CircularIterator implements Iterator<Integer> {

    private List<Integer> list;
    private int currentPosition;

    public CircularIterator(List<Integer> list) {
        this.list = list;
        this.currentPosition = 0;
    }

    public boolean hasNext() {
        return true;
    }

    public Integer next() {
        int posToReturn = currentPosition;
        currentPosition = ++currentPosition % list.size();
        return list.get(posToReturn);
    }

    public void remove() {
        throw new NotImplementedException();
    }
}
