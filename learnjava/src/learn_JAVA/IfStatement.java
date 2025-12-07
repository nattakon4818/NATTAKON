package learn_JAVA;

import java.util.Scanner;

public class IfStatement {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your age : ");
        int age = input.nextInt();

        if (age >= 15 && age <= 19) System.out.println("teenager");
        else if (age >= 20 && age <= 29) System.out.println("youth");
        else if (age >= 30 && age <= 39) System.out.println("working age");
        else if (age >= 40 && age <= 59) System.out.println("middle age");
        else if (age >= 60) System.out.println("old age");
        else System.out.println("child");

        System.out.println("Exit Program...");

        // // AND
        // if (age >= 15 && age <= 19) System.out.println("teenager"); 
        // else System.out.println("not teenager");

        // // OR
        // if (age < 15 || age > 19) System.out.println("teenager");
        // else System.out.println("not teenager");
        
        // // NOT
        // if (!(age >= 15)) System.out.println("not teenager");
        // else System.out.println("teenager");
    }
}
