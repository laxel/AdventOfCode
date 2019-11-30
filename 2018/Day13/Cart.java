public class Cart {
    public int x;
    public int y;
    public int direction;   // 0 left, 1 upp, 2 right,  3 down
    public int nextTurn;    // 0 left, 1/3 forward, 2 right
    public Cart(int x, int y, int direction) {
        this.x = x;
        this.y = y;
        this.direction = direction;
        nextTurn = 0;
    }

}
