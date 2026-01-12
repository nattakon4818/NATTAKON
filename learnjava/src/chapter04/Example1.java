package chapter04;

public class Example1 {
    public void displayInstance() {
        System.out.println("Hello from Instance.");
    }

    public static void displayStatic() {
        System.out.println("Hello from Static.");
    }

    public static void main(String[] args) {
        System.out.println("Test call static method.");
        Example1.displayStatic();
        Example1 obj = new Example1();
        System.out.println("Test call instance method.");
        obj.displayInstance();
    }
}
