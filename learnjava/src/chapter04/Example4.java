package chapter4;

import java.util.Scanner;

public class Example4 {
    public void MainMethod() {
        Scanner input = new Scanner(System.in);
        int num1, num2;
        String output = "";
        System.out.println("Enter valuue 1 : ");
        num1 = Integer.parseInt(input.nextLine());
        System.out.println("Enter valuue 2 : ");
        num2 = Integer.parseInt(input.nextLine());
        output = "brfore call method num1 = " + num1 + ", num2 = " + num2;
        System.out.println(output);
        changeValue(num1, num2);
        output = "brfore call method num1 = " + num1 + ", num2 = " + num2;
        System.out.println(output);
        input.close();
    }

    public void changeValue(int n1 , int n2) {
        n1 = n1 + n2;
        n2 = n2 - 5;
    }

    public static void main(String[] args) {
        new Example4().MainMethod();
    }
}
