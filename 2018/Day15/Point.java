public class Point implements Comparable<Point>{
    public int x;
    public int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Point p) {
        if(y > p.y) {
            return 1;
        } else if(y < p.y) {
            return -1;
        }
        // y = p.y
        if(x > p.x) {
            return 1;
        } else if(x < p.x) {
            return -1;
        }
        return 0;

    }
}
