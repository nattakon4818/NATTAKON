package chapter08;

public class Student {
    private String name;
    private int age;

    public Student(String name, int age) {
        setName(name);
        setAge(age);
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }
    
    public void setAge(int age) {
        if (age > 0) {
            this.age = age;
        } else {
            System.out.println("Age error");
        }
    }

    public int getAge() {
        return this.age;
    }

    public String toString() {
        return "Name : " + getName() + "\n" +
                "Age : " + getAge();
    }
}
