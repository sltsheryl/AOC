import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class day5b {

    public static Stack<String> reverseStack(Stack<String> stack) {
        Stack<String> y = new Stack<>();
        while (!stack.empty()) {
            String x = stack.pop();
            y.add(x);
        }
        return y;
    }
    
    public static void main(String[] args) {
        ArrayList<String> grid = new ArrayList<>();
        ArrayList<Integer[]> instructions = new ArrayList<>();

        int numOfLines = 8;
        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            for (int i = 0; i < numOfLines; i++) {
                String currLine = myReader.nextLine();
                grid.add(currLine);
            }

            String numbering[] = myReader.nextLine().split(" ");

            int len = Integer.parseInt(numbering[numbering.length - 1]);

            List<Stack<String>> stacks = new ArrayList<>(len);

            for (int i = 0; i < len; i++) {
                stacks.add(new Stack<String>());
            }
            for (int j = 0; j < grid.size(); j++) {
                int chunkSize = 4;
                String[] chunks = grid.get(j).split("(?<=\\G.{" + chunkSize + "})");
                for (int k = 0; k < chunks.length; k++) {
                    if (!chunks[k].split("")[1].equals(" ")) {
                        stacks.get(k).add(chunks[k].split("")[1]);
                    }
                }
            }

            for (int n = 0; n < stacks.size(); n++) {
                stacks.set(n, reverseStack(stacks.get(n)));

            }
            myReader.nextLine();
            while (myReader.hasNextLine()) {
                String currLine = myReader.nextLine();

                Pattern p = Pattern.compile("\\d+");
                Matcher m = p.matcher(currLine);
                int index = 0;
                Integer[] instruction = new Integer[3];
                while (m.find()) {
                    instruction[index] = Integer.parseInt(m.group());
                    index++;
                }
                instructions.add(instruction);
            }

            myReader.close();

            for (int a = 0; a < instructions.size(); a++) {
                int numOfTimes = instructions.get(a)[0];
                int initialPosition = instructions.get(a)[1];
                int finalPosition = instructions.get(a)[2];

                ArrayList<String> toTransfer = new ArrayList<>();

                for (int times = 0; times < numOfTimes; times++) {
                    String z = stacks.get(initialPosition - 1).pop();
                    toTransfer.add(z);
                    
                }
                for (int i = toTransfer.size() - 1; i >= 0; i--) {
                    stacks.get(finalPosition - 1).push(toTransfer.get(i));
                }
            }

            for (int x = 0; x < stacks.size(); x++) {
                System.out.print(stacks.get(x).pop());
            }

        } catch (FileNotFoundException e) { 
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
       
    }
}
