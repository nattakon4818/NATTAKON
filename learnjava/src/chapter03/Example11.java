package chapter3;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Example11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        DecimalFormat twoDigit = new DecimalFormat("0.00");
        int count = 0;
        double value = 0.0, total = 0.0;
        System.out.println(">> Exit input -1 <<");
        while (value != -1.0) {
            System.out.print("Enter floating-point number #" + (count + 1) + " : ");
            value = scanner.nextDouble();
            if (value >= 0.00) {
                total += value;
                count++;
            }
        }
        double average = total / count;
        System.out.println("Total value : " + twoDigit.format(total));
        System.out.println("Average value : " + twoDigit.format(average));
    }
}
