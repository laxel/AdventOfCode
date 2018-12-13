public class Cart {
    public int x;
    public int y;
    public int direction;   // 0 right, 1 upp, 2 left,  3 down
    public int nextTurn;
    public Cart(int x, int y, int direction) {
        this.x = x;
        this.y = y;
        this.direction = direction;
        nextTurn = -1;
    }

    public int getTurnDirection() {
        direction++;
        return 1;
    }

    public enum direction {
    RIGHT, UPP, LEFT, DOWN;
    }

}
