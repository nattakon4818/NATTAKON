package learn_JAVA.Assign;

import java.util.Scanner;

public class Assing05 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter weight (kg) : ");
        double weight = scanner.nextDouble();
        System.out.print("Enter height (cm) : ");
        double height = scanner.nextDouble() / 100;
        double bmi = weight / (height * height);
        System.out.println("Weight : " + weight + " kg");
        System.out.println("Height : " + height * 100 + " cm");
        System.out.printf("BMI is %.2f\n", bmi);
        String category;

        if (bmi < 18) {
            category = "Underweight";
        } else if (bmi >= 18 && bmi <= 22.9) {
            category = "Normal weight";
        } else if (bmi >= 23 && bmi <= 24.9) {
            category = "Overweight";
        } else if (bmi >= 25 && bmi <= 29.9) {
            category = "Obesity";
        } else {
            category = "Severe Obesity";
        }
        System.out.println(category);
        scanner.close();

        /* 
         * BMI Categories:
         * Underweight = <18
         * Normal weight = 18–22.9
         * Overweight = 23–24.9
         * Obesity = 25–29.9
         * Severe Obesity = 30+
         */
    }
}
