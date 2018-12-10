import java.util.ArrayList;

public class DubbleLinkedList {
    Node root;
    Node currentMarble;

    private class Node {
        Node next;
        Node prev;
        Integer value;

        public Node(int _value, Node _next, Node _prev) {
            value = _value;
            next = _next;
            prev = _prev;
        }
    }

    public DubbleLinkedList() {
        Node _root = new Node(-1, null, null);
        _root.next = _root; _root.prev = _root;
        root = _root;

        currentMarble = root;

        insert(0);
    }

    public void insert(Integer value) {
        Node newNode = new Node(value, null, null);
        newNode.next = currentMarble; newNode.prev = currentMarble.prev;
        currentMarble.prev.next = newNode;
        currentMarble.prev = newNode;
        currentMarble = newNode;
    }

    public int remove() {
        int value = currentMarble.value;
        currentMarble.next.prev = currentMarble.prev;
        currentMarble.prev.next = currentMarble.next;
        currentMarble = currentMarble.next;
        return value;
    }

    public void goCW(int steps) {
        for(int i = 0; i < steps; i++) {
            currentMarble = currentMarble.next;
            if(currentMarble == root)
                currentMarble = currentMarble.next;
        }
    }

    public void goCCW(int steps) {
        for(int i = 0; i < steps; i++) {
            currentMarble = currentMarble.prev;
            if(currentMarble == root)
                currentMarble = currentMarble.prev;
        }
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node pointer = root.next;
        sb.append(currentMarble.value + " [");
        while(pointer != root) {
            sb.append(pointer.value + ", ");
            pointer = pointer.next;
        }
        sb.append("]");
        pointer = root.next;
        while(pointer != root) {
            sb.append("\n[" + pointer.prev.value + ", " + pointer.value  + ", " + pointer.next.value + "]" );
            pointer = pointer.next;
        }
        return sb.toString();
    }
}
