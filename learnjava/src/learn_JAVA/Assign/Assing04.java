package learn_JAVA.Assign;

import java.util.Scanner;

public class Assing04 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number (B.E.) : ");
        int beYear = scanner.nextInt();
        int result1 = beYear - 543;
        System.out.println("The year in A.D. is : " + result1);

        System.out.print("Enter a number (A.D.) : ");
        int adYear = scanner.nextInt();
        int result2 = adYear + 543;
        System.out.println("The year in B.E. is : " + result2);
    }
}
