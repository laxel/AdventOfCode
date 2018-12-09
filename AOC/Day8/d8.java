import java.util.*;
import java.io.*;

public class d8 {
    public static void main(String[] args) throws Exception {
        // Read input
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String str;
        ArrayList<Integer> list = new ArrayList<Integer>();

        while ((str = br.readLine()) != null) {
            String[] strList = str.split(" ");
            for(String s : strList) {
                list.add(Integer.parseInt(s));
            }
        }

        Node root = buildTree(list);
        System.out.println("/-------------- PART 1 --------------/");
        System.out.println(treeSum1(root));
        System.out.println("/-------------- PART 2 --------------/");
        System.out.println(treeSum2(root));

    }
    
    public static Node buildTree(ArrayList<Integer> list) {

        int pointer = 0;
        Stack<Integer> startChildren = new Stack<Integer>();
        Stack<Integer> childrenStack = new Stack<Integer>();
        Stack<Integer> valueStack = new Stack<Integer>();
        Stack<Node> nodeStack = new Stack<Node>();

        do {
            // Step 1
            childrenStack.push(list.get(pointer));
            startChildren.push(list.get(pointer));
            valueStack.push(list.get(pointer + 1));

            // Step 2
            if(childrenStack.peek() == 0) {
                Node node  = new Node();
                pointer += 2;
                int numValues = valueStack.pop();
                for(int i = 0; i < numValues; i++) {
                    node.addValue(list.get(pointer));
                    pointer++;
                }

                childrenStack.pop(); startChildren.pop();
                nodeStack.push(node);

                if(childrenStack.empty()) {
                    return nodeStack.pop();
                }
                while(!childrenStack.empty()) {
                    if(childrenStack.peek() <= 1) {
                        Node _node = new Node();
                        int _numValues = valueStack.pop();
                        for(int i = 0; i < _numValues; i++) {
                            _node.addValue(list.get(pointer));
                            pointer++;
                        }
                        childrenStack.pop();
                        int numChildren = startChildren.pop();
                        for(int i = 0; i < numChildren; i++) {
                            _node.children.add(nodeStack.pop());
                        }
                        nodeStack.push(_node);

                        if(childrenStack.empty()) {
                            return nodeStack.pop();
                        } else {

                        }
                    } else {
                        childrenStack.push(childrenStack.pop() - 1);
                        break;
                    }
                }

            } else {
                pointer += 2;
            }

        } while(true);
    }

    public static Integer treeSum1(Node node) {
        Integer sum = 0;

        for(Integer v : node.values) {
            sum += v;
        }

        for(Node n : node.children) {
            sum += treeSum1(n);
        }
        return sum;
    }

    public static Integer treeSum2(Node node) {
        Integer sum = 0;
        // Leaf node
        if(node.children.size() == 0) {
            for(Integer v : node.values) {
                sum += v;
            }
            return sum;
        }
        // Node with children
        for(Integer metaData : node.values) {
            if(metaData <= node.children.size()) {
                int index = metaData - 1;
                // My tree have it's children "reversed", takes the index of the inverse to fix this
                sum += treeSum2(node.children.get(node.children.size() - 1 - index));
            }
        }
        return sum;
    }
}
