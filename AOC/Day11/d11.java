
public class d11 {
    public static void main(String[] args) throws Exception {
        int serialNumber = 1788; // Input
        int[] list = new int[300*300];

        // Find powerLevel for each coordinate
        for(int y = 1; y <= 300; y++) {
            for(int x = 1; x <= 300; x++) {
                int rackID = x + 10;
                int powerLevel = (rackID * y + serialNumber) * rackID;
                powerLevel = ((powerLevel / 100) % 10) - 5;
                list[(x-1) + (y-1)*300] = powerLevel;
            }
        }

        // ---------------- PART 1 ----------------
        int maxSum = Integer.MIN_VALUE;
        int xBest = -1; int yBest = -1;
        // For every coordinate
        for(int y = 0; y < 297; y++) {
            for(int x = 0; x < 297; x++) {
                int sum = 0;
                // Find 3x3 sum
                for(int dy = 0; dy < 3; dy++) {
                    for(int dx = 0; dx < 3; dx++) {
                        sum += list[(x + dx) + (y + dy)*300];
                    }
                }
                if (sum > maxSum) {
                    maxSum = sum;
                    xBest = x + 1;
                    yBest = y + 1;
                }
            }
        }
        System.out.println("------------- PART 1 -------------");
        System.out.println("(x,y): (" + xBest + ", " + yBest + ")");

        // ---------------- PART 2 ----------------
        System.out.println("------------- PART 2 -------------");
        System.out.println("This will take some time, please be patient.");
        maxSum = Integer.MIN_VALUE;
        xBest = -1; yBest = -1;
        int squareSize = -1;
        int sum  = -1;
        // For every coordinate
        for(int y = 0; y < 300; y++) {
            for(int x = 0; x < 300; x++) {
                int maxSquare = Math.min(300 - x,300-y);
                //System.out.println(maxSquare);
                for(int sqS = 0; sqS < maxSquare; sqS++) {
                    sum = 0;
                    for(int dy = 0; dy < sqS; dy++) {
                        for(int dx = 0; dx < sqS; dx++) {
                            sum += list[(x + dx) + (y + dy)*300];
                        }
                    }
                    if (sum > maxSum) {
                        maxSum = sum;
                        xBest = x + 1;
                        yBest = y + 1;
                        squareSize = sqS;
                    }
                }
            }
            if(y % 30 == 0 && y != 0) {
                System.out.println(((float)y)/3 + "% done");
            }
        }
        System.out.println("(x,y,size): (" + xBest + ", " + yBest + ", " + squareSize + ")");
        System.out.println("With a total powerLevel of " + maxSum);
    }
}
