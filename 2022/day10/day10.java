import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day10 {
    public static void main(String[] args) {
        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            int[] strengths = new int[6];
            int count = 1;
            int strength;
            int[] special = {20, 60, 100, 140, 180, 220};
            while (myReader.hasNextLine()) {
              
                String data = myReader.nextLine();
                if (data.split(" ")[0].equals("noop")) {
                } else if (data.split(" ")[0].equals("addx")) {
                    int step = count + 2;
                    if (count == step) {
                        strength += Integer.parseInt(data.split(" ")[1]);
                    }
                }
                count++;
                
            }
            myReader.close();
            
        
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
