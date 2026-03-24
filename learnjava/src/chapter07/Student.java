package chapter07;

// data class
public class Student {
    public String name;
    public int age;

    public Student() {
        name = "Unkhow";
        age = 0;
    }

    public Student(String n, int a) {
        name = n;
        age = a;
    }

    public void displayInfo() {
        System.out.println(name + " is " + age + " years old.");
    }
}
