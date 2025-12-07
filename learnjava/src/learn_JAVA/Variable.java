package learn_JAVA;

public class Variable {
    public static void main(String[] args) {
        /// นิยามค่าตัวแปรแบบไม่ระบุค่าเริ่มต้น

        // int number1;
        // boolean status;
        // char alphabet;
        // float number2;
        // double number3;

        ///////////////////////////////////
        /// นิยามค่าตัวแปรแบบระบุค่าเริ่มต้น

        // int number1 = 10;
        // float number2 = 20.5f;
        // char alphabet = 'A';
        // boolean status = true;

        ///////////////////////////////////
        /// หลายบรรทัดในครั้งเดียว

        // int a = 0, b = 1, c = 2;

        ///////////////////////////////////
        /// ค่าที่สามารถเปลี่ยนแปลงได้

        // int num1 = 10;
        // int num2 = 20;
        // num1 = 100;
        // System.out.println("The numerical value of 1 is " + num1);
        // System.out.println("The numerical value of 2 is " + num2);

        ///////////////////////////////////
        /// ค่าคงที่

        // final int NUM1 = 10;
        // final int NUM2 = 20;
        // System.out.println("The numerical value of 1 is " + NUM1);
        // System.out.println("The numerical value of 2 is " + NUM2);

        ///////////////////////////////////
        /// Global Variable
        
        // int a = 10;
        // System.out.println(a);

        /// Local Variable 
        // {
        //     int c = 20;
        //     System.out.println(c);
        // }

        //////////////////////////////////
        /// การแปลงชนิดข้อมูล
        /// เล็กเป็นใหญ่ (Implicit Conversion)
        
        // int num1 = 10;
        // double num2 = num1;
        // System.out.println(num2);

        /// ใหญ่เป็นเล็ก (Explicit Conversion)
        
        // double num3 = 20.5;
        // int num4 = (int) num3;
        // System.out.println(num4);

        //////////////////////////////////
        /// String ->>> int
        
        // String a = "100", b = "200";
        // int c = Integer.parseInt(a) + Integer.parseInt(b);;
        // c += 100;
        // System.out.println(a);
        // System.out.println(b);
        // System.out.println(c);

        /// String ->>> double
        
        // String a = "100", b = "200";
        // double c = Double.parseDouble(a) + Double.parseDouble(b);
        // c += 100.50;
        // System.out.println(c);

        /// Integer ->>> String
        
        // int num1 = 100;
        // String age = String.valueOf(num1);
        // System.out.println(age);
    }
}
