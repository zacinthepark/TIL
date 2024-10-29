package variable;

public class Var8 {

    public static void main(String[] args) {
        // 표현할 수 있는 숫자의 범위와 차지하는 메모리 공간이 달라짐
        byte b = 127;
        short s = 32767;    // 2byte
        int i = 2147483647; // 4byte
        long l = 9223372036854775807L;  // 8byte
        float f = 10.0f;    // 4byte
        double d = 10.0;    // 8byte

        // boolean: 1byte, char: 2byte
    }
}
