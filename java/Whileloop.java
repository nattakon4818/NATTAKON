public class Whileloop {
    public static void main(String[] args) {
        int count = 1;
        // เงื่อนไขในการทำซ้ำ
        while (true) { // ใช้ true เพื่อให้ลูปทำงานตลอดไปจนกว่าจะเจอคำสั่ง break
            System.out.println("Count is : " + count);
            count ++;

            if (count > 20) break;
        }
    }
}
