package chapter5;

import java.util.Scanner;

public class Example1 {
    public static void main(String[] args) {
        double value;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter floating number : ");
        value = scanner.nextDouble();
        System.out.println("\nCeliing            of " + value + " is " + Math.ceil(value));
        System.out.println("Floor              of " + value + " is " + Math.floor(value));
        System.out.println("Square root        of " + value + " is " + Math.sqrt(value));
        System.out.println("Exponential        of " + value + " is " + Math.exp(value));
        System.out.println("Absolute           of " + value + " is " + Math.abs(value));
        System.out.println("Natural logarithm  of " + value + " is " + Math.log(value));
        System.out.println("logarithm 10       of " + value + " is " + Math.log10(value));
        System.out.println("Power three        of " + value + " is " + Math.pow(value, 3));
        System.out.println("Random value       of " + value + " is " + Math.random());
        System.out.println("PI value           of " + value + " is " + Math.PI);
        System.out.println("Exponential value  of " + value + " is " + Math.E);
        scanner.close();
    }
}
