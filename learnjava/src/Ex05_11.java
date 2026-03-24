import javax.swing.JOptionPane;
import java.util.Random;

public class Ex05_11 {
    public static int randomInt() {
        Random random = new Random();
        int num = random.nextInt(1000) + 1;
        JOptionPane.showMessageDialog(null, "Random number is " + num,
                "Message", JOptionPane.INFORMATION_MESSAGE);
        return num;
    }
    
    public static boolean isPrime() {
        int number = Integer
                .parseInt(JOptionPane.showInputDialog(null, "Enter number to check prime number: ", "Message",
                        JOptionPane.INFORMATION_MESSAGE));
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                JOptionPane.showMessageDialog(null, number + " is not Prime number",
                        "Message", JOptionPane.INFORMATION_MESSAGE);
                return false;
            }
        }
        JOptionPane.showMessageDialog(null, number + " is Prime number",
                "Message", JOptionPane.INFORMATION_MESSAGE);
        return true;
    }
    
    public static void convertDecimalToBinary() {
        int number = Integer
                .parseInt(JOptionPane.showInputDialog(null, "Enter number to convert decimal to binary: ", "Message",
                        JOptionPane.INFORMATION_MESSAGE));
        String binary = "";
        while (number > 0) {
            binary = (number % 2) + binary;
            number /= 2;
        }
        JOptionPane.showMessageDialog(null, "Binary number is " + binary,
                "Message", JOptionPane.INFORMATION_MESSAGE);
    }
    
    public static void normalPyramid() {
        StringBuilder result = new StringBuilder();
        int rows = Integer.parseInt(JOptionPane.showInputDialog(null,
                "Enter number to print normal pyramid: ", "Message", JOptionPane.INFORMATION_MESSAGE));
    
        for (int i = 1; i <= rows; i++) {
            for (int j = rows - i; j > 0; j--) {
                result.append(" ");
            }
    
            for (int j = 1; j <= i; j++) {
                result.append("*");
            }
    
            result.append("\n");
        }
    
        JOptionPane.showMessageDialog(null, result.toString(), "Normal Pyramid", JOptionPane.INFORMATION_MESSAGE);
    }
    
    public static void invertedPyramid() {
        StringBuilder result = new StringBuilder();
        int rows = Integer.parseInt(JOptionPane.showInputDialog("Enter number of rows for inverted pyramid:"));
    
        for (int i = rows; i >= 1; i--) {
            for (int j = rows - i; j > 0; j--) {
                result.append(" ");
            }
    
            for (int j = 1; j <= i; j++) {
                result.append("A");
            }
    
            result.append("\n");
        }
    
        JOptionPane.showMessageDialog(null, result.toString(), "Inverted Pyramid", JOptionPane.INFORMATION_MESSAGE);
    }
    
    public static void numberPyramid() {
        StringBuilder result = new StringBuilder();
        int rows = Integer.parseInt(JOptionPane.showInputDialog(null,
                "Enter number to print number pyramid: ", "Message", JOptionPane.INFORMATION_MESSAGE));
    
        for (int i = 1; i <= rows; i++) {
            for (int j = rows - i; j > 0; j--) {
                result.append(" ");
            }
    
            for (int k = 1; k <= (2 * i - 1); k++) {
                result.append(i);
            }
    
            result.append("\n");
        }
    
        JOptionPane.showMessageDialog(null, result.toString(), "Number Pyramid", JOptionPane.INFORMATION_MESSAGE);
    }
    
    public static void letterPyramid() {
        StringBuilder result = new StringBuilder();
        int rows = Integer.parseInt(JOptionPane.showInputDialog(null,
                "Enter number to print letter pyramid: ", "Message", JOptionPane.INFORMATION_MESSAGE));
        char letter = 'A';
    
        for (int i = 1; i <= rows; i++) {
            for (int j = rows - i; j > 0; j--) {
                result.append(" ");
            }
    
            for (int k = 1; k <= (2 * i - 1); k++) {
                result.append(letter);
                letter++;
            }
    
            result.append("\n");
        }
    
        JOptionPane.showMessageDialog(null, result.toString(), "Letter Pyramid", JOptionPane.INFORMATION_MESSAGE);
    }
    
    public static void main(String[] args) {
        String choiceStr, strMenu;
        boolean done = true;
        strMenu = ">>  Main Menu  <<\n";
        strMenu += " 1. Random Integer Number(1 - 1000)\n";
        strMenu += " 2. Check Prime Number\n";
        strMenu += " 3. Convert Decimal to Binary\n";
        strMenu += " 4. Normal Pyramid\n";
        strMenu += " 5. Inverted Pyramid\n";
        strMenu += " 6. Number Pyramid\n";
        strMenu += " 7. Letter Pyramid\n";
        strMenu += " 0. Exit\n";
        strMenu += "Enter your choice: ";
    
        while (done) {
            choiceStr = JOptionPane.showInputDialog(strMenu);
            if (choiceStr != null && choiceStr.length() > 0) {
                if (choiceStr.equals("1")) {
                    randomInt();
                } else if (choiceStr.equals("2")) {
                    isPrime();
                } else if (choiceStr.equals("3")) {
                    convertDecimalToBinary();
                } else if (choiceStr.equals("4")) {
                    normalPyramid();
                } else if (choiceStr.equals("5")) {
                    invertedPyramid();
                } else if (choiceStr.equals("6")) {
                    numberPyramid();
                } else if (choiceStr.equals("7")) {
                    letterPyramid();
                } else if (choiceStr.equals("0")) {
                    done = false;
                } else {
                    JOptionPane.showMessageDialog(null, "No this choice",
                            "Message", JOptionPane.ERROR_MESSAGE);
                }
            } else {
                JOptionPane.showMessageDialog(null, "Exit Program!",
                        "Message", JOptionPane.ERROR_MESSAGE);
                break;
            }
        }
    
        if (!done) {
            JOptionPane.showMessageDialog(null, "Exit Program!",
                    "Message", JOptionPane.INFORMATION_MESSAGE);
            System.exit(0);
        }
    }
    
}

