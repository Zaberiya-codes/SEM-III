import java.util.Scanner;

public class VotingCheck {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = input.nextInt();

        if(age>= 18){
            System.out.println("you are eligible to vote");
        } else{
            System.out.println("sorry, you must be at least 18.");
        }
    }
