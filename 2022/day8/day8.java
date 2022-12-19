import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class day8 {
    public static void main(String[] args) {
        ArrayList<String> input = new ArrayList<String>();
        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                input.add(data);
            }
            myReader.close();
            int numOfCols = input.get(0).length();
            int numOfRows = input.size();
            int[][] grid = new int[numOfRows][numOfCols];
            for (int i = 0; i < numOfRows; i++) {
                for (int j = 0; j < numOfCols; j++)
                    grid[i][j] = input.get(i).charAt(j);
            }
            boolean[][] visited = new boolean[numOfRows][numOfCols];
            // check for left and right
            for (int row = 0; row < numOfRows; row++) {
                int height = -1;
                for (int col = 0; col < numOfCols; col++) {
                    if (grid[row][col] > height) {
                        visited[row][col] = true;
                        height = grid[row][col];
                    } 
                }
                height = -1;
                for (int col = numOfCols - 1; col >= 0; col--) {
                    if (grid[row][col] > height) {
                        visited[row][col] = true;
                        height = grid[row][col];
                    }
                }

            }
            // check for up and down
            for (int col = 0; col < numOfCols; col++) {
                int minHeight = -1;
                for (int row = 0; row < numOfRows; row++) {
                    if (grid[row][col] > minHeight) {
                        visited[row][col] = true;
                        minHeight = grid[row][col];
                    }
                }
                
                minHeight = -1;
                for (int row = numOfRows - 1; row >= 0; row--) {
                    if (grid[row][col] > minHeight) {
                        visited[row][col] = true;
                        minHeight = grid[row][col];
                    } 
                }
            }

            int res = 0;
            for (int i = 0; i < numOfRows; i++) {
                for (int j = 0; j < numOfCols; j++) {
                    if (visited[i][j]) {
                        res++;
                    }
                }

            }
            System.out.println(res);

        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
