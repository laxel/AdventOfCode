import java.util.ArrayList;

public class MarbleList {
    int currentMarble;
    ArrayList<Integer> list;

    public MarbleList() {
        currentMarble = 0;
        list = new ArrayList<Integer>();
        list.add(0);
    }

    public void insert(int value) {
        list.add(currentMarble, value);
    }

    public int remove() {
        return list.remove(currentMarble);
    }

    public void goCW(int steps) {
        for(int i = 0; i < steps; i++) {
            currentMarble++;
            if(currentMarble >= list.size()) {
                currentMarble = 0;
            }
        }
    }

    public void goCCW(int steps) {
        for(int i = 0; i < steps; i++) {
            currentMarble--;
            if(currentMarble < 0) {
                currentMarble = list.size() - 1;
            }
        }
    }

    public String toString() {
        return "CM: " + currentMarble + ", " + list.toString();
    }
}
