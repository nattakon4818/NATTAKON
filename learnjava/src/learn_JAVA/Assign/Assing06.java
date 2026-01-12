package learn_JAVA.Assign;

import java.util.Scanner;

public class Assing06 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter amount (THB) : ");
        int money = scanner.nextInt();
        System.out.println("Amount : " + money + " THB");

        if (money >= 1000) {
            System.out.println("1000 THB : " + (money / 1000) + " bills");
            money %= 1000;
        }
        if (money >= 500) {
            System.out.println("500 THB : " + (money / 500) + " bills");
            money %= 500;
        }
        if (money >= 100) {
            System.out.println("100 THB : " + (money / 100) + " bills");
            money %= 100;
        }
        if (money >= 50) {
            System.out.println("50 THB : " + (money / 50) + " bills");
            money %= 50;
        }
        if (money >= 20) {
            System.out.println("20 THB : " + (money / 20) + " bills");
            money %= 20;
        }
        if (money >= 10) {
            System.out.println("10 THB : " + (money / 10) + " coins");
            money %= 10;
        }
        scanner.close();
    }
}

/*
 * โปรแกรมแลกธนบัตร 1000 > 500 > 100 > 50 > 20 บาท
 * 
 * เช่น
 * 2000 ได้แบงค๋ 1000 2 ใบ
 * 1500 ได้แบงค๋ 1000 1 ใบ, 500 1 ใบ
 * 1800 ได้แบงค๋ 1000 1 ใบ, 500 1 ใบ, 100 3 ใบ
 * 100 ได้แบงค๋ 100 1 ใบ
 * 90 ได้แบงค๋ 50 1 ใบ, 20 2 ใบ
 * 70 ได้แบงค๋ 50 1 ใบ, 20 1 ใบ
 */