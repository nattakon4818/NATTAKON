package chapter03;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Example7 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        DecimalFormat twoDigit = new DecimalFormat("0.00");
        final int PER_LINE = 5;
        System.out.print("Enter frist number : ");
        int frist = input.nextInt();
        System.out.print("Enter second number : ");
        int second = input.nextInt();
        int sum = 0, count = 0;
        String result = "";
        for (int num = frist; num <= second; num++) {
            sum += num;
            result += "\t" + num;
            if (++count % PER_LINE == 0)
                result += "\n";
        }
        result += "\nSummation of " + frist + " to " + second + " = " + sum + "\n";
        result += "Average : " + twoDigit.format((float) sum / count);
        System.out.println(result);
    }
}
