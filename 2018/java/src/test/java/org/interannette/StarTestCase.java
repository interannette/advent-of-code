package org.interannette;

public class StarTestCase<T> {

    private String inputString;
    private T expectedOutput;

    public StarTestCase(String inputString, T expectedOutput) {
        this.inputString = inputString.replace(", ", "\n");
        this.expectedOutput = expectedOutput;
    }

    public String getInputString() {
        return inputString;
    }

    public void setInputString(String inputString) {
        this.inputString = inputString;
    }

    public T getExpectedOutput() {
        return expectedOutput;
    }

    public void setExpectedOutput(T expectedOutput) {
        this.expectedOutput = expectedOutput;
    }
}
