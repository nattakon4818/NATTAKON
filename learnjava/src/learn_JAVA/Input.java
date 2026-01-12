package learn_JAVA;

import java.util.Scanner;

public class Input {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name : ");
        String name = scanner.nextLine();
        System.out.println("Hello " + name + " How old are you?");
        int age = scanner.nextInt();
        System.out.println("So you are " + age + " years old!");
        scanner.close();

        /// scanner.nextLine(); อ่านทั้งบรรทัดรวมช่องว่าง
        /// scanner.next(); อ่านคำเดียวไม่รวมช่องว่าง
    }
}
