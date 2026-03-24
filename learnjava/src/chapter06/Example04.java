package chapter06;

import javax.swing.JOptionPane;
import javax.swing.JTextArea;

public class Example04 {
    public static void main(String[] args) {
        new Example04().mainProgram();
        System.exit(0);
    }

    public void mainProgram() {
        int array[] = {1, 2, 3, 4, 5};
        String output = "Effects of passing antire array by reference:\n" +
            "The value of the original array are:\n";
        for (int i = 0; i < array.length; i++)
            output += String.format("%5d", array[i]);
        modifyArray(array);
        output += "\n\nThe value of the modify array are:\n";
        for (int i = 0; i < array.length; i++)
            output += String.format("%5d", array[i]);
        output += "\n\nEffects of passing array element by value:\n" +
            "array[2] before modifyElement: " + array[2];
        modifyElement(array[3]);
        output += "\narray[2] after modifyElement: " + array[2];

        JTextArea outputArea = new JTextArea();
        outputArea.setText(output);
        JOptionPane.showMessageDialog(null, outputArea, "Passing Array",
            JOptionPane.INFORMATION_MESSAGE);
    }

    public void modifyArray(int array2[]) {
        for (int i = 0; i < array2.length; i++)
            array2[i] *= 2;
    }

    public void modifyElement(int element) {
        element *= 2;
    }
}
