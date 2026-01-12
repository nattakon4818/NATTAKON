package chapter3;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Exercise1 {
    public static void main(String[] args) {
        DecimalFormat twoDigit = new DecimalFormat("0.00");
        Scanner scanner = new Scanner(System.in);
        System.out.println(">> Program Calculate Commission <<\n");
        System.out.print("Enter sale amount : ");
        int amount = scanner.nextInt();
        if (amount <= 0) {
            System.out.println("\nError sale amount, no calculate commission.");
        }
        else {
            System.out.println("\nYour total sale : " + twoDigit.format(amount));
            double rate = 0;
            if (amount > 100000) rate = 10;
            else if (amount >= 80001) rate = 9;
            else if (amount >= 60001) rate = 7;
            else if (amount >= 40001) rate = 5;
            else if (amount >= 20001) rate = 2.75;
            else if (amount >= 10001) rate = 1.5;
            System.out.println("You got commission rate = " + rate);
            System.out.println("You got commission : " + twoDigit.format(((rate/100) * amount)));
        }
        scanner.close();
    }
}
