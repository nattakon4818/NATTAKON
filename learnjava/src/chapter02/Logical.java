package chapter02;
public class Logical {
    public static void main(String[] args) {
        int x = 2, y = 6;
        System.out.print(" (x == 3) && (y != 6) = ");
        System.out.println( ((x == 3) && (y != 6)) );
        System.out.print(" (x == 3) || (y != 6) = ");
        System.out.println( ((x == 3) || (y != 6)) );
        System.out.println( " !(x != y) = " + (!(x != y)) );
    }
}
