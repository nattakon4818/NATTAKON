package learn_JAVA.Assign;

import java.util.Scanner;

public class Assing03 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer : ");
        int num = scanner.nextInt();

        // วิธีที่ 1
        if (num % 2 == 0) {
            System.out.println("Number " + num + " is Even."); // เลขคู่
        } else {
            System.out.println("Number " + num + " is Odd."); // เลขคี่
        }

        // วิธีที่ 2
        String result = "";

        if (num % 2 == 0) {
            result = "Even"; // เลขคู่
        } else {
            result = "Odd"; // เลขคี่
        }
        System.out.println("Number " + num + " is " + result + ".");

        /////////////////////////////////////////////////////
        
        // การใช้เงื่อนไขแบบลดรูป (Ternary Operator)
        result = (num % 2 == 0) ? num + " - Even" : num + " - Odd";
        System.out.println(result);
        scanner.close();
    }
}
