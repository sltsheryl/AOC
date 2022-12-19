import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.HashMap;
import java.util.Scanner;

public class day7 {
  public static TreeNode makeSubTree(ArrayList<String> listOfElem, HashMap<String, ArrayList<String>> hashmap,
      LinkedList<String> path) {
    int weight = 0;
    TreeNode tree = new TreeNode(weight);
    for (int i = 0; i < listOfElem.size(); i++) {
      // it is a file (regex for integer)
      if (listOfElem.get(i).matches("\\d+")) {
        int size = Integer.parseInt(listOfElem.get(i));
        weight += size;
        tree.setChildren(new TreeNode(size));
      } else {
        // it is a directory
        path.add(listOfElem.get(i));
        String dirPath = String.join("/", path);
        TreeNode subtree = makeSubTree(hashmap.get(dirPath), hashmap, path);
        path.removeLast();
        weight += subtree.getWeight();
        tree.setChildren(subtree);
      }
    }
    tree.setWeight(weight);

    return tree;
  }

  public static int traverseTree(TreeNode root) {
    int res = 0;
    if (root == null) {
      return 0;
    } else if (root.getWeight() <= 100000) {
      res += root.getWeight();
    }

    ArrayList<TreeNode> children = root.getChildren();
    for (TreeNode child : children) {
      // is a directory
      if (child.getChildren().size() > 0) {
        res += traverseTree(child);
      }
    }
    return res;
  }

  public static void main(String[] args) {
    try {
      File myObj = new File("input.txt");
      Scanner myReader = new Scanner(myObj);
      HashMap<String, ArrayList<String>> hashmap = new HashMap<>();
      String data = myReader.nextLine();
      LinkedList<String> path = new LinkedList<String>();
      while (myReader.hasNextLine()) {
        // cd a directory
        if (data.split(" ")[1].equals("cd") && !data.split(" ")[2].equals("..")) {
          String name = data.split(" ")[2].strip();
          path.add(name);
          String dirPath = String.join("/", path);
          ArrayList<String> fileList = new ArrayList<>();
          data = myReader.nextLine();
          data = myReader.nextLine();

          while (!data.split(" ")[0].equals("$")) {
            if (data.split(" ")[0].matches("\\d+")) {
              // add file
              fileList.add(data.split(" ")[0]);
            } else {
              fileList.add(data.split(" ")[1]);
            }
            if (myReader.hasNextLine()) {
              data = myReader.nextLine();
            } else {
              break;
            }
          }
          hashmap.put(dirPath, fileList);
        }
        // cd ..
        else if (data.split(" ")[1].equals("cd") && data.split(" ")[2].equals("..")) {
          data = myReader.nextLine();
          path.removeLast();
        }
      }
      myReader.close();
      LinkedList<String> rootPath = new LinkedList<String>();
      rootPath.add("/");
      TreeNode resTree = makeSubTree(hashmap.get("/"), hashmap, rootPath);
      System.out.println("total is " + resTree.getWeight());
      int resWeight = traverseTree(resTree);
      System.out.println("sol is " + resWeight);

    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }

  public static class TreeNode {
    public int weight;
    public ArrayList<TreeNode> children = new ArrayList<>();

    // constructor
    public TreeNode(int weight) {
      this.weight = weight;
    }

    public void setChildren(TreeNode child) {
      children.add(child);
    }

    public void setWeight(int weight) {
      this.weight = weight;
    }

    public int getWeight() {
      return weight;
    }

    public ArrayList<TreeNode> getChildren() {
      return children;
    }

  }
}
