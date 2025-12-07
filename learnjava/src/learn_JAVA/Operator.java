package learn_JAVA;

public class Operator {
    public static void main(String[] args) {
        // ตัวดำเนินการทางคณิตศาสตร์
        int a = 15;
        int b = 4;

        // + การบวก
        int sum = a + b;
        System.out.println(sum);

        // - การลบ
        int difference = a - b;
        System.out.println(difference);

        // * การคูณ
        int product = a * b;
        System.out.println(product);

        // / หารเอาผลลัพธ์
        int quotient = a / b;
        System.out.println(quotient);

        // % หารเอาเศษ
        int remainder = a % b;
        System.out.println(remainder);

        ///////////////////////////////////////////////

        // ตัวดำเนินการเปรียบเทียบ
        int x = 10;
        int y = 20;

        // == เท่ากับ
        System.out.println(x == y); // false

        // != ไม่เท่ากับ
        System.out.println(x != y); // true

        // > มากกว่า
        System.out.println(x > y); // false

        // < น้อยกว่า
        System.out.println(x < y); // true

        // >= มากกว่าหรือเท่ากับ
        System.out.println(x >= y); // false

        // <= น้อยกว่าหรือเท่ากับ
        System.out.println(x <= y); // true

        ///////////////////////////////////////////////

        // ตัวดำเนินการตรรกะ
        boolean p = true;
        boolean q = false;

        // && และ
        System.out.println(p && q); // false

        // || หรือ
        System.out.println(p || q); // true

        // ! ไม่
        System.out.println(!p); // false

        ///////////////////////////////////////////////

        // ตัวดำเนินการเพิ่มค่าและลดค่า
        int count = 5;

        // ++ เพิ่มค่า
        count++; // เพิ่มค่าก่อนใช้งาน
        System.out.println(count);

        ++count; // เพิ่มค่าหลังใช้งาน
        System.out.println(count);

        // -- ลดค่า
        count--; // ลดค่าก่อนใช้งาน
        System.out.println(count);

        --count; // ลดค่าหลังใช้งาน
        System.out.println(count);

        ///////////////////////////////////////////////

        // Compound Assignment
        int num1 = 10, num2 = 5;

        num1 += num2; // เท่ากับ num1 = num1 + num2
        System.out.println(num1);

        num1 -= num2; // เท่ากับ num1 = num1 - num2
        System.out.println(num1);

        num1 *= num2; // เท่ากับ num1 = num1 * num2
        System.out.println(num1);

        num1 /= num2; // เท่ากับ num1 = num1 / num2
        System.out.println(num1);

        num1 %= num2; // เท่ากับ num1 = num1 % num2
        System.out.println(num1);
    }
}
