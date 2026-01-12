package chapter2;

public class Example10 {
    final double PI = 3.1416;
    String message;
    double area;

    public Example10(double radius) {
        message = "Circle";
        area = PI * radius * radius;
    }

    public Example10(double width, double height) {
        message = "Rectangle";
        area = width * height;
    }

    public static void main(String[] args) {
        Example10 circle = new Example10(10.0);
        System.out.print("Calculate Area " + circle.message);
        System.out.println(" = " + circle.area);
        
        Example10 rectangle = new Example10(12.0, 20.0);
        System.out.print("Calculate Area " + rectangle.message);
        System.out.println(" = " + rectangle.area);
    }
}
