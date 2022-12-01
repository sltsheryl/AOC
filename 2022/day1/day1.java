import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day1 {
    public static void main(String[] args) {
        int max1 = 0;
        int max2 = 0;
        int max3 = 0;
        int current = 0;
        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if (data.equals("")) {
                    if (current >= max1) {
                        int temp = max1;
                        max1 = current;
                        max2 = temp;
                        max3 = max2;
                    } else if (current >= max2) {
                        int temp = max2;
                        max2 = current;
                        max3 = temp;
                    } else if (current >= max3) {
                        max3 = current;
                    }
                    current = 0;
                } else {
                    current += Integer.parseInt(data);
                }
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        int[] res = new int[3];
        res[0] = max1;
        res[1] = max2;
        res[2] = max3;
        int sum = 0;
        for (int i = 0; i < res.length; i++) {
            sum += res[i];
        }
        System.out.println(sum);
    }
}

