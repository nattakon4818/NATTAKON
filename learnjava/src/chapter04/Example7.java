package chapter4;

import java.util.Scanner;

public class Example7 {
    public long factorial (long n) {
        if (n > 1) return(n* factorial(n-1));
        else return(1);
    }

    public static long factorialStatic (long n) {
        long fac = 1;
        if (n > 0) {
            for (int x = 1 ; x <= n ; x++)
                fac *= x;
            return fac;
        }
        else return(fac);
    }

    public void test() {
        long n;
        Scanner scan = new Scanner(System.in);
        Example7 obj = new Example7();
        System.out.print("Enter number : ");
        n = scan.nextInt();
        System.out.println("Factorial of " + n + " is " + obj.factorial(n));
        System.out.print("FactorialStatic of " + n + " is ");
        System.out.println(Example7.factorialStatic(n));
        scan.close();
    }

    public static void main(String[] args) {
        new Example7().test();
    }
}
