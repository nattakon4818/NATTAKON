package chapter05;

import java.util.Scanner;

public class Example4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String name;
        System.out.print("ENter name : ");
        name = scanner.nextLine();
        if (!name.isEmpty()) {
            for (int index = 0; index < name.length(); index++) {
                System.out.print("Character : " + name.charAt(index));
                System.out.print(" is ascil value : ");
                System.out.println((byte) name.charAt(index));
            }
        } else
            System.out.println("No data input");
        scanner.close();
    }
}
