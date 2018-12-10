
public class Coordinate{
    public int x;
    public int y;
    public int velx;
    public int vely;

    public Coordinate(int _x, int _y, int _velx, int _vely) {
        x = _x;
        y = _y;
        velx = _velx;
        vely = _vely;
    }

    public void update() {
        x += velx;
        y += vely;
    }
}
