package chapter07;

/*  Id   :  68-060216-1242-8
 *  Name :  Nattakon Nuwan
 *  Room :  1 RC
 *  File Name  : Assing05_6806021612428.java
*/

import java.awt.*;
import javax.swing.*;

public class Assign05_6806021612428 {

    public static void main(String[] args) {
        Assign05_6806021612428.mainProgram();
    }

    public static void mainProgram() {
        double[] monthlySales = new double[12];
        boolean dataGenerated = false;
        String menu = "Menu Sale Report\n" +
                      "----------------------------------\n" +
                      "1. Generate Sale\n" +
                      "2. Report Sale\n" +
                      "3. Exit\n" +
                      "Enter choice :";

        while (true) {
            String input = JOptionPane.showInputDialog(null, menu, "Input", JOptionPane.QUESTION_MESSAGE);
            if (input == null) break;

            try {
                int choice = Integer.parseInt(input);
                if (choice == 1) {
                    genSale(monthlySales);
                    dataGenerated = true;
                    JOptionPane.showMessageDialog(null, "Generate Sale finish.", "Message", JOptionPane.INFORMATION_MESSAGE);
                } else if (choice == 2) {
                    if (dataGenerated) {
                        reportSale(monthlySales);
                    } else {
                        JOptionPane.showMessageDialog(null, "Please generate sales data first!", "Warning", JOptionPane.WARNING_MESSAGE);
                    }
                } else if (choice == 3) {
                    JOptionPane.showMessageDialog(null, "Exit Program.", "Message", JOptionPane.INFORMATION_MESSAGE);
                    break;
                }
            } catch (NumberFormatException e) {

            }
        }
    }

    public static void genSale(double[] sales) {
        for (int i = 0; i < sales.length; i++) {

            sales[i] = 100000 + (Math.random() * 800000);
        }
    }

    public static void reportSale(double[] sales) {
        double total = 0;
        for (double s : sales) total += s;

        StringBuilder sb = new StringBuilder();

        sb.append(String.format(" %-5s %11s %17s\n", "No.", "Sales", "Percent"));
        sb.append(" ===================================\n");

        for (int i = 0; i < sales.length; i++) {
            double percent = (sales[i] / total) * 100;

            sb.append(String.format(" %-5d %15.2f %12.2f\n", (i + 1), sales[i], percent));
        }

        sb.append(" ===================================\n");
        sb.append(String.format(" %-5s %16.2f %11.2f", "Total", total, 100.00));


        JTextArea textArea = new JTextArea(sb.toString());
        textArea.setFont(new Font("Monospaced", Font.PLAIN, 13));
        textArea.setEditable(false);
        textArea.setBackground(Color.WHITE); 
        textArea.setOpaque(true);
        textArea.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10)); 

        JOptionPane.showMessageDialog(null, textArea, "Message", JOptionPane.INFORMATION_MESSAGE);
    }
}