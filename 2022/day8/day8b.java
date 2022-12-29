import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class day8b {

    public static int getScore(int[][] grid, int row, int col) {
        int scoreA = 0;
        int scoreB = 0;
        int scoreC = 0;
        int scoreD = 0;
        
        for (int j = col - 1; j >= 0; j--) {
                if (j < 0 || j >= grid[0].length) {
                    break;
                }
                if (grid[row][j] >= grid[row][col]) {
                    scoreA++;
                    break;
                }
                scoreA++;
            }

            for (int j = col + 1; j <= grid[0].length; j++) {
                if (j < 0 || j >= grid[0].length) {
                    break;
                }
                if (grid[row][j] >= grid[row][col]) {
                    scoreB++;
                    break;
                }
                scoreB++;
            }
       
            for (int j = row - 1; j >= 0; j--) {
                if (j < 0 || j >= grid.length) {
                    break;
                }
                if (grid[j][col] >= grid[row][col]) {
                    scoreC++;
                    break;
                }
                scoreC++;
            }
            for (int j = row + 1; j <= grid.length; j++) {
                if (j < 0 || j >= grid.length) {
                    break;
                }
                if (grid[j][col] >= grid[row][col]) {
                    scoreD++;
                    break;
                }
                scoreD++;
            }
        
        return scoreA * scoreB * scoreC * scoreD;
    }
    public static void main(String[] args) {
        try {
            ArrayList<String> stringGrid = new ArrayList<>();
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                stringGrid.add(data);
            }
            myReader.close();
            int numOfRows = stringGrid.size();
            int numOfCols = stringGrid.get(0).length();
            int[][] grid = new int[numOfRows][numOfCols];
            for (int i = 0; i < numOfRows; i++) {
                for (int j = 0; j < numOfCols; j++) {
                    grid[i][j] = stringGrid.get(i).charAt(j) - '0';
                }
            }
            int maxScore = 0;
            for (int i = 0; i < numOfRows; i++) {
                for (int j = 0; j < numOfCols; j++) {
                    int score = getScore(grid, i, j);
                    if (score > maxScore) {
                        maxScore = score;
                    }
                }
            }
            System.out.println(maxScore);

        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
