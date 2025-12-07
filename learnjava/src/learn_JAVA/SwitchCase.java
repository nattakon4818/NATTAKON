package learn_JAVA;

import java.util.Scanner;

public class SwitchCase {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the month number : ");
        int month = scanner.nextInt();

        // วิธีที่ 1

        String monthName;
        switch (month) {
            case 1: monthName = "January"; break;
            case 2: monthName = "February"; break;
            case 3: monthName = "March"; break;
            case 4: monthName = "April"; break;
            case 5: monthName = "May"; break;
            case 6: monthName = "June"; break;
            case 7: monthName = "July"; break;
            case 8: monthName = "August"; break;
            case 9: monthName = "September"; break;
            case 10: monthName = "October"; break;
            case 11: monthName = "November"; break;
            case 12: monthName = "December"; break;
            default: monthName = "Invalid month number"; break;
        }
        System.out.println(monthName);

        // วิธีที่ 2
        
        // switch (month) {
        //     case 1: System.out.println("January"); break;
        //     case 2: System.out.println("February"); break;
        //     case 3: System.out.println("March"); break;
        //     case 4: System.out.println("April"); break;
        //     case 5: System.out.println("May"); break;
        //     case 6: System.out.println("June"); break;
        //     case 7: System.out.println("July"); break;
        //     case 8: System.out.println("August"); break;
        //     case 9: System.out.println("September"); break;
        //     case 10: System.out.println("October"); break;
        //     case 11: System.out.println("November"); break;
        //     case 12: System.out.println("December"); break;
        //     default: System.out.println("Invalid month number"); break;
        // }
    }
}
