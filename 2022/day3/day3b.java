import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class day3b {
    public static void main(String[] args) {
        int sum = 0;
        ArrayList<String> arr = new ArrayList<>();
        
        try {
            int priority = 0;
            char repeatedCharacter = '0';
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                arr.add(data);
            }
            myReader.close();
            for (int i = 0; i < arr.size(); i+= 3) {
                HashMap<Character, Integer> hashmap1 = new HashMap<>();
                HashMap<Character, Integer> hashmap2 = new HashMap<>();
                HashMap<Character, Integer> hashmap3 = new HashMap<>();
                String elfOne = arr.get(i);
                for (int j = 0; j < elfOne.length(); j++) {
                    hashmap1.put(elfOne.charAt(j), 1);
                }
                String elfTwo = arr.get(i + 1);
                for (int k = 0; k < elfTwo.length(); k++) {
                    hashmap2.put(elfTwo.charAt(k), 1);
                }
                String elfThree = arr.get(i + 2);
                for (int l = 0; l < elfThree.length(); l++) {
                    hashmap3.put(elfThree.charAt(l), 1);
                }
                int minLength = Math.min(elfThree.length(), Math.min(elfOne.length(), elfTwo.length()));
                String shortestString = null;
                if (elfOne.length() == minLength) {
                     shortestString = elfOne;
                }
                if (elfTwo.length() == minLength) {
                     shortestString = elfTwo;
                }
                if (elfThree.length() == minLength) {
                     shortestString = elfThree;
                }
                for (int a = 0; a < minLength; a++) {
                    if (hashmap1.get(shortestString.charAt(a)) != null && hashmap2.get(shortestString.charAt(a)) != null
                            && hashmap3.get(shortestString.charAt(a)) != null) {
                        repeatedCharacter = shortestString.charAt(a);
                    }
                }
                
                if (Character.isLowerCase(repeatedCharacter)) {
                    priority = (int) repeatedCharacter - 96;
                } else if (Character.isUpperCase(repeatedCharacter)) {
                    priority = (int) repeatedCharacter - 38;
                }
            
                sum += priority;   
            }
            
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        System.out.println(sum);
    }
}


