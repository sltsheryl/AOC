import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day2b {
    public static void main(String[] args) {
        int score = 0;
        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String currOpponent = data.split(" ")[0];
                String currSuggested = data.split(" ")[1];
                switch (currOpponent) {
                    // rock
                    case "A":
                    // rock
                    if (currSuggested.equals("X")) {
                        // lose
                        // scissors
                        score += 3 + 0;
                        break;
                    // draw
                    // rock
                    } else if (currSuggested.equals("Y")) {
                        score += 3 + 1;
                        break;
                    } else {
                        // win
                        // paper
                        score += 2 + 6;
                        break;
                    }
                    
                    // paper
                    case "B":
                    // lose 
                    // rock
                    if (currSuggested.equals("X")) {
                        score += 0 + 1;
                        break;
                        // paper
                    } else if (currSuggested.equals("Y")) {
                        // draw
                        score += 3 + 2;
                        break;
                    } else {
                        // win
                        // scissors
                        score += 3 + 6;
                        break;
                    }

                    // scissors
                    case "C":
                    // paper
                    // lose
                    if (currSuggested.equals("X")) {
                        score += 2 + 0;
                        break;
                        // draw
                        // scissors
                    } else if (currSuggested.equals("Y")) {
                        score += 3 + 3;
                        break;
                    } else {
                        // win
                        // rock
                        score += 1 + 6;
                        break;
                    }
                }
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        
        System.out.println(score);
    }
}

