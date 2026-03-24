package chapter07;

public class App {
    public static void main(String[] args) {
        Book b1 = new Book("Java", "Smith", 200);
        Book b2 = new Book("Python", "Somsak", 150);
        b1.displayInfo();
        b2.displayInfo();

        // Student1 s1 = new Student1();
        // Student1 s2 = new Student1();
        // s1.name = "Alice";
        // s2.name = "nattakon";
        // s1.displaySchool();
        // s2.displaySchool();
    }
}
