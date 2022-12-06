import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day4 {
    public static void main(String[] args) {
        int count = 0;
        
        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String firstPart = data.split(",")[0];
                String secondPart = data.split(",")[1];
                int firstStart = Integer.parseInt(firstPart.split("-")[0]);
                int firstEnd = Integer.parseInt(firstPart.split("-")[1]);
                int secondStart = Integer.parseInt(secondPart.split("-")[0]);
                int secondEnd = Integer.parseInt(secondPart.split("-")[1]);

                if ((firstStart <= secondStart && firstEnd >= secondEnd)
                        || (firstStart >= secondStart && firstEnd <= secondEnd)) {
                    count++;
                }
            }
            myReader.close();
        
            
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        System.out.println(count);
    }
}

