package chapter02;

import java.util.Scanner;

public class Exercise1 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Program change Temperature");
        System.out.print("Enter celsius : ");
        float celsius = scan.nextFloat();
        float fahrenheit = (9 / 5 * celsius) + 32;
        System.out.println("Temperature celsius : " + celsius);
        System.out.println("Temperature fahrenheit : " + fahrenheit);
    }
}
