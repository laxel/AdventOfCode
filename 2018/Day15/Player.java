public class Player implements Comparable<Player>{
    public int race; // 0 = Elf, 1 = Goblin
    public int x;
    public int y;
    public int hp;

    public Player(int race, int x, int y) {
        this.race = race;
        this.x = x;
        this.y = y;
        hp = 200;
    }

    public static Player copyPlayer(Player player) {
        Player p = new Player(player.race, player.x, player.y);
        return p;
    }

    @Override
    public String toString() {
        return ((race == 0) ? "Elf: " : "Goblin: ") + "(" + x + ", " + y + ") " + hp;
    }

    @Override
    public int compareTo(Player p) {
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
