package org.interannette.day16;

import java.util.Arrays;

public class Operation {

    enum Type { ADD, MULT, BAN, BOR, SET, GT, EQ }
    enum Name {

        ADDR(false, false, Type.ADD), ADDI(false, true, Type.ADD),
        MULTR(false, false, Type.MULT), MULTI(false, true, Type.MULT),
        BANR(false, false, Type.BAN), BANI(false, true, Type.BAN),
        BORR(false, false, Type.BOR), BORI(false, true, Type.BOR),
        SETR(false, false, Type.SET), SETI(true, false, Type.SET),
        GTIR(true, false, Type.GT), GTRI(false, true, Type.GT), GTRR(false, false, Type.GT),
        EQIR(true, false, Type.EQ), EQRI(false, true, Type.EQ), EQRR(false, false, Type.EQ);

        boolean immediateLeft, immediateRight;
        Type type;

        Name(boolean immediateLeft, boolean immediateRight, Type type) {
            this.immediateLeft = immediateLeft;
            this.immediateRight = immediateRight;
            this.type = type;
        }
    }

    public static int[] performOperation(Name operation, int input1, int input2, int output, int[] start){
        int[] result = new int[start.length];
        for(int i = 0; i < start.length; i++) {
            if(i == output) {
                int a = operation.immediateLeft ? input1 : start[input1];
                int b = operation.immediateRight ? input2 : start[input2];
                int value = -1;
                switch (operation.type) {
                    case ADD:
                        value = a + b;
                        break;
                    case MULT:
                        value = a * b;
                        break;
                    case BAN:
                        value = a & b;
                        break;
                    case BOR:
                        value = a | b;
                        break;
                    case SET:
                        value = a;
                        break;
                    case GT:
                        value = (a > b) ? 1 : 0;
                        break;
                    case EQ:
                        value = (a == b) ? 1 : 0;
                        break;
                }
                result[i] = value;
            } else {
                result[i] = start[i];
            }
        }
        return result;
    }

    public static boolean matches(Name operation, Sample sample) {
        int[] result = performOperation(operation,
                sample.instruction.input1, sample.instruction.input2,
                sample.instruction.output, sample.before);
        return Arrays.equals(result, sample.after);
    }
}
