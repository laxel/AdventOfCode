import java.util.ArrayList;

public class Node{
    public ArrayList<Node> children;
    public ArrayList<Integer> values;

    public Node() {
        children = new ArrayList<Node>();
        values = new ArrayList<Integer>();
    }

    public void addChild(Node _node) {
        children.add(_node);
    }

    public void addValue(Integer _value) {
        values.add(_value);
    }
    public String toString() {
        return this.toStringLevel(0);
    }

    private String toStringLevel(int i) {
        StringBuilder sb = new StringBuilder();

        sb.append(values.toString());
        i++;
        for(Node node : children) {
            sb.append("\n");
            for(int n = 0; n < i; n++) sb.append("   ");
            sb.append(" - " + node.toStringLevel(i));
        }
        return sb.toString();
    }

}
