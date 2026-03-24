package chapter07;

public class Book {
    public String title;
    public String author;
    public float price;

    public Book(String t, String a, float p) {
        title = t;
        author = a;
        price = p;
    }

    public void displayInfo() {
        System.out.println(title + " : " + author + " : " + price);
    }
}
