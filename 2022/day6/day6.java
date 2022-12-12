import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class day6 {
    public static boolean isUnique(String s) {
        HashMap<Character, Integer> hashmap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (hashmap.get(s.charAt(i)) != null) {
                return false;
            } else {
                hashmap.put(s.charAt(i), 0);
            }
        }
        return true;
    }
    // sliding window
    public static void main(String[] args) {
        String input = "";
        int sizeOfMarker = 14;
        int counter = sizeOfMarker;
        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                input += data;
            }
            myReader.close();
            String res = "";
            for (int i = 0; i < sizeOfMarker; i++) {
                res += input.charAt(i);
            }
            while (!isUnique(res)) {
                res = res.substring(1);
                res += input.charAt(counter);
                counter ++;
            }
           
            System.out.println(counter);
            
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}


