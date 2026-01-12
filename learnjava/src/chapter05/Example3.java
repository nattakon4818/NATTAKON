package chapter5;

public class Example3 {
    public static void main(String[] args) {
        int value;
        String output = "Random number 0 to 9 : \n";
        for (int c = 1; c <= 10; c++) {
            value = (int) (Math.random() * 10);
            output += value + ", ";
        }
        System.out.println(output);
        output = "\nRandom number is 15 to 25 : \n";
        for (int c = 1; c <= 10; c++) {
            value = 15 + (int) (Math.random() * 11);
            //      ^-----------------------|   ^----------------|
            // ถ้าไม่ได้เริ่มที่ 0 ให้เอาตัวที่จะเริ่มไว้ข้างหน้าแล้วตัวหลังให้หาผลต่างแล้วนำมาบวก 1
            output += value + ", ";
        }
        System.out.println(output);
    }
}
