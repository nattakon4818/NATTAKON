package chapter02;

public class Condition {
    public static void main(String[] args) {
        /*
                เงื่อนไข        เมื่อเป็นจริง     เมื่อเป็นเท็จ
            (expression1) ? expression2 : expression3
        */

        int result;
        int count = 10;
        result = (count < 5) ? 1 : 2;
        System.out.println(result);
    }
}
