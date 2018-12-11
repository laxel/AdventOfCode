
public class Coordinate{
    public int x;
    public int y;
    public int velx;
    public int vely;

    public Coordinate(int[] input) {
        x = input[0];
        y = input[1];
        velx = input[2];
        vely = input[3];
    }

    public void update(int val) {
        x += val * velx;
        y += val * vely;
    }
}
