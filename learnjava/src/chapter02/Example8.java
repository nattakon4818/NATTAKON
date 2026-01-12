package chapter2;

public class Example8 {
    public static void main(String[] args) {
        boolean result = false;
        int number = 5;
        // String color = "red";
        String color = new String("red");

        System.out.println("When number = " + number + ", color = " + color);
        result = (number < 10) && (color == "red");
        System.out.print("result = (number < 10) && (color == \"red\") = ");
        System.out.println(result);
        result = (number < 10) & (color == "red");
        System.out.print("result = (number < 10) & (color == \"red\") = ");
        System.out.println(result);
        result = (number < 10) || (color == "red");
        System.out.print("result = (number < 10) || (color == \"red\") = ");
        System.out.println(result);
        result = (number < 10) | (color == "red");
        System.out.print("result = (number < 10) | (color == \"red\") = ");
        System.out.println(result);
        result = (number < 10) ^ (color == "red");
        System.out.print("result = (number < 10) ^ (color == \"red\") = ");
        System.out.println(result);
        result = !(number < 10);
        System.out.println("result = !(number < 10) = " + result);
        result = !(color == "red");
        System.out.println("result = !(color == \"red\") = " + result);
    }
}
