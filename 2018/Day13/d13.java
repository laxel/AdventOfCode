import java.util.*;
import java.io.*;
import java.util.concurrent.TimeUnit;

public class d13 {
    public static void main(String[] args) throws Exception {
        boolean part1 = false;  // part 2 -> False
        boolean print = false; // Set true to print track

        // Read input
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String str;
        ArrayList<String> strList = new ArrayList<String>();
        int width = -1;

        while((str = br.readLine()) != null) {
            strList.add(str);
            if(str.length() > width) width = str.length();
        }

        char[][] map = new char[strList.size()][width];
        ArrayList<Cart> carts = new ArrayList<Cart>();

        for(int y = 0; y < strList.size(); y++) {
            String strToParse = strList.get(y);
            for(int x = 0; x < strToParse.length(); x++) {
                char ch = strToParse.charAt(x);
                if(ch == 'v') {
                    Cart c = new Cart(x,y,3);
                    carts.add(c);
                    map[y][x] = '|';
                }else if(ch == '^') {
                    Cart c = new Cart(x,y,1);
                    carts.add(c);
                    map[y][x] = '|';
                } else if(ch == '<') {
                    Cart c = new Cart(x,y,0);
                    carts.add(c);
                    map[y][x] = '-';
                } else if (ch == '>') {
                    Cart c = new Cart(x,y,2);
                    carts.add(c);
                    map[y][x] = '-';
                } else {
                    map[y][x] = ch;
                }
            }
        }

        int ticks = 0;

        whileLoop:
        while(true) {

            // Update carts
            ArrayList<Cart> cartsLeft = new ArrayList<Cart>();
            HashSet<Integer> indexTaken = new HashSet<Integer>();
            while(cartsLeft.size() != carts.size()) {
                int smallestPos = Integer.MAX_VALUE;
                int index = -1;
                for(int i = 0; i < carts.size(); i++) {
                    Cart cart = carts.get(i);
                    if(cart.y*width + cart.x < smallestPos && !indexTaken.contains(i)) {
                        smallestPos = cart.y*width + cart.x;
                        index = i;
                    }
                }
                cartsLeft.add(carts.get(index));
                indexTaken.add(index);
            }

            for(Cart c : cartsLeft) {
                int[] collision = updateCart(map, c, carts);
                if(collision[0] == 1) {
                    if(part1) {
                        System.out.println("Collision at x: " + collision[1] + ", y: " + collision[2] + " after " + ticks + " ticks.");
                        break whileLoop;
                    } else {

                        for(int z = 0; z < carts.size(); z++) {
                            Cart cart = carts.get(z);
                            if (cart.x == collision[1] && cart.y == collision[2]) {
                                carts.remove(z);
                                z--;
                                System.out.println("Cart removed ("+cart.x+", "+cart.y  +") at tick " + ticks + ", carts remaining " + carts.size());
                            }
                        }
                    }
                }
            }
            if(carts.size() == 1 && !part1) {
                System.out.println("Only one cart left, positioned at x: " + carts.get(0).x + ", y: " + carts.get(0).y);
                break whileLoop;
            }

            ticks++;

            // Printing
            if(print) {
                for(int y = 0; y < map.length; y++) {
                    for(int x = 0; x < map[y].length; x++) {
                        char toPrint = map[y][x];
                        for(Cart c : carts) {
                            if(c.x == x && c.y == y) {
                                if(c.direction == 0) toPrint = '<';
                                if(c.direction == 1) toPrint = '^';
                                if(c.direction == 2) toPrint = '>';
                                if(c.direction == 3) toPrint = 'v';
                            }
                        }
                        System.out.print(toPrint);
                    }
                    System.out.println();
                }
                TimeUnit.MILLISECONDS .sleep(1000);
                System.out.print("\033[H\033[2J");
            }

        }
    }

    public static int[] collision(char[][] map, ArrayList<Cart> carts) {
        for(int i = 0; i < carts.size(); i++) {
            for(int n = i+1; n < carts.size(); n++) {
                Cart cart1 = carts.get(i);
                Cart cart2 = carts.get(n);
                if (cart1.x == cart2.x && cart1.y == cart2.y) {
                    return new int[] {1,cart1.x,cart2.y};
                }
            }

        }
        return new int[]  {-1};
    }

    public static int[] updateCart(char[][] map, Cart cart, ArrayList<Cart> carts) {
        char standingOn = map[cart.y][cart.x];
        switch (standingOn) {
            case '+':
                int direction = cart.direction + ((cart.nextTurn == 0) ? -1 : 0)
                                               + ((cart.nextTurn == 2) ? 1 : 0);
                if(direction > 3) direction = 0;
                if(direction < 0) direction = 3;
                cart.nextTurn++;
                if(cart.nextTurn > 2) cart.nextTurn = 0;
                switch (direction) {
                    case 0: cart.x--;
                            break;
                    case 1: cart.y--;
                            break;
                    case 2: cart.x++;
                            break;
                    case 3: cart.y++;
                            break;
                }
                cart.direction = direction;
                break;

            case '-' :
                cart.x += (cart.direction == 0) ? -1 : 1;
                break;

            case '|' :
                cart.y += (cart.direction == 1) ? -1 : 1;
                break;

            case '/' :
                switch (cart.direction) {
                    case 0: cart.y++;
                            cart.direction = 3;
                            break;
                    case 1: cart.x++;
                            cart.direction = 2;
                            break;
                    case 2: cart.y--;
                            cart.direction = 1;
                            break;
                    case 3: cart.x--;
                            cart.direction = 0;
                            break;
                }
                break;

            case '\\' :
                switch (cart.direction) {
                    case 0: cart.y--;
                            cart.direction = 1;
                            break;
                    case 1: cart.x--;
                            cart.direction = 0;
                            break;
                    case 2: cart.y++;
                            cart.direction = 3;
                            break;
                    case 3: cart.x++;
                            cart.direction = 2;
                            break;
                }
                break;

            default :
                throw new IllegalArgumentException("No match for _standingOn_. x: " + cart.x + ", y: " + cart.y);
        }
        for(Cart c : carts) {
            if (cart.x == c.x && cart.y == c.y && cart != c) {
                return new int[] {1,cart.x,cart.y};
            }
        }
        return new int[]  {-1};
    }
}
