/*
    Id : 6806021612428
    Name : Mr. Nattakon Nuwan
    Room : 1 RC
    File Name : Assign04_6806021612428
*/

package chapter06;

import java.util.Scanner;

public class Assign04_6806021612428 {
    Scanner scanner = new Scanner(System.in);

    public void start() {
        System.out.println(">>> Program Fibonacci <<<\n");
        int num;
        while (true) {
            System.out.print("Enter sequence number : ");
            num = scanner.nextInt();
            if (num == -1) {
                System.out.println("Exit Program.\n");
                break;
            }
            System.out.println("Fibonacci sequence " + num + " = " + fibonacci(num) + "\n");
        }
    }

    public int fibonacci(int num) {
        if (num == 0)
            return 0;
        if (num == 1)
            return 1;
        int first = 0, second = 1, next = 0;
        for (int i = 2; i <= num; i++) {
            next = first + second;
            first = second;
            second = next;
        }
        return next;
    }

    public static void main(String[] args) {
        Assign04_6806021612428 obj = new Assign04_6806021612428();
        obj.start();
    }
}
