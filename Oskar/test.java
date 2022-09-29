
import java.util.Scanner;

public class test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        String input = s.nextLine();
        String[] ord = input.split(" ");
        String start = ord[1].substring(0,1).toUpperCase() + ord[1].substring(1) + " " + ord[0].toLowerCase();
        String slutning  = input.substring(ord[0].length() + ord[1].length() + 1, input.length()-1); 
        String svar = start + slutning + "!"; 
        System.out.println(svar);
    }
}