import java.util.Scanner;

public class Assign1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter weight (kg): ");
        double weight = scanner.nextDouble();
        System.out.print("Enter height (cm): ");
        double height = scanner.nextDouble() / 100;
        double bmi = weight / (height * height);
        System.out.println("Weight: " + weight + " kg");
        System.out.println("Height: " + height * 100 + " cm");
        System.out.printf("BMI is %.2f", bmi);
    }
}
