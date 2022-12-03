import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class day3 {
    public static void main(String[] args) {
        int sum = 0;
        try {
            int priority = 0;
            char repeatedCharacter = '0';
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                int len = data.length();
                HashMap<Character, Integer> hashmap = new HashMap<>();
                for (int i = 0; i < (len / 2); i++) {
                    hashmap.put(data.charAt(i), 1);
                    
                }
                for (int j = len / 2; j < len; j++) {
                    if (hashmap.get(data.charAt(j)) != null) {
                        repeatedCharacter = data.charAt(j);

                        break;
                    }
                }
                if (Character.isLowerCase(repeatedCharacter)) {
                    priority = (int) repeatedCharacter - 96;
                } else if (Character.isUpperCase(repeatedCharacter)) {
                    priority = (int) repeatedCharacter - 38;
                }
            
                sum += priority;   
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        System.out.println(sum);
    }
}


