import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day2 {
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
                        // draw
                        score += 3 + 1;
                        break;
                    // paper
                    } else if (currSuggested.equals("Y")) {
                        // won
                        score += 6 + 2;
                        break;
                    } else {
                        // lose
                        // scissors
                        score += 0 + 3;
                        break;
                    }
                    
                    // paper
                    case "B":
                    // rock
                    if (currSuggested.equals("X")) {
                        // lose
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
                    // rock
                    // win
                    if (currSuggested.equals("X")) {
                        score += 6 + 1;
                        break;
                        // paper
                        // lose
                    } else if (currSuggested.equals("Y")) {
                        score += 0 + 2;
                        break;
                    } else {
                        // draw
                        // scissors
                        score += 3 + 3;
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

