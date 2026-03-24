package chapter08;

public class BankAccount {
    private double balance;

    public BankAccount(double deposit) {
        deposit(deposit);
    }

    public void setBalance(double amount) {
        this.balance = amount;
    }

    public double getBalance() {
        return this.balance;
    }

    public void deposit(double amount) {
        setBalance(getBalance() + amount);
    }

    public void withdraw(double amount) {
        if (amount <= getBalance())
            setBalance(getBalance() - amount);
        else
            System.out.println("Not enouh balance.");
    }

    public String toString() {
        return "Balance : " + getBalance();
    }
}
