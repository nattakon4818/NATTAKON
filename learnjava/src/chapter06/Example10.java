package chapter06;

import javax.swing.JOptionPane;
import javax.swing.JTextArea;
import java.awt.Font;

public class Example10 {
    int scores[][] = { { 77, 68, 86, 73 },
                       { 96, 87, 89, 81 },
                       { 70, 90, 86, 81 } };
    int student, exam;
    String output;
    JTextArea outputArea;

    public Example10() {
        student = scores.length;
        exam = scores[0].length;
        outputArea = new JTextArea();
        output = "The array is:\n";
        buildString();
        output += "\n\nLowest grade : " + minimum() +
                "\nHighest grade : " + maximum() + "\n";
        for (int index = 0; index < student; index++)
            output += "\nAverage for student " + index + " is " +
                    average(scores[index]);

        outputArea.setFont(new Font("Consolas", Font.BOLD, 14));
        outputArea.setText(output);
        JOptionPane.showMessageDialog(null, outputArea);
    }

    public int minimum() {
        int lowGrade = scores[0][0];
        for (int row = 0; row < student; row++)
            for (int column = 0; column < exam; column++)
                if (scores[row][column] < lowGrade)
                    lowGrade = scores[row][column];
        return lowGrade;
    }

    public int maximum() {
        int highGrade = scores[0][0];
        for (int row = 0; row < student; row++)
            for (int column = 0; column < exam; column++)
                if (scores[row][column] > highGrade)
                    highGrade = scores[row][column];
        return highGrade;
    }

    public double average(int setOfGrades[]) {
        int total = 0;
        for (int count = 0; count < setOfGrades.length; count++)
            total += setOfGrades[count];
        return (double) total / setOfGrades.length;
    }

    public void buildString() {
        output += "          ";
        for (int index = 0; index < exam; index++)
            output += "[" + index + "]  ";
        for (int row = 0; row < student; row++) {
            output += "\ngrades[" + row + "] ";
            for (int column = 0; column < exam; column++)
                output += scores[row][column] + "  ";
        }
    }

    public static void main(String[] args) {
        new Example10();
    }
}
