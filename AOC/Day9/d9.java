import java.util.*;
import java.io.*;

public class d9 {
    public static void main(String[] args) throws Exception {
        // Read input
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String str = br.readLine();
        int numPlayers = Integer.parseInt(str.split(" ")[0]);
        int maxMarble = Integer.parseInt(str.split(" ")[6]);

        MarbleList list = new MarbleList();
        int[] playerScore = new int[numPlayers];
        int currPlayer = 1;
        int currValue = 1;
        while(currValue < maxMarble) {
            if(currValue % 23 == 0) {
                list.goCCW(7);
                playerScore[currPlayer - 1] += currValue + list.remove();
            } else {
                list.goCW(2);
                list.insert(currValue);
            }
            currValue++;
            currPlayer++;
            if(currPlayer > numPlayers) currPlayer = 1;
        }
        int maxScore = 0;
        for(int i = 0; i < playerScore.length; i++) {
            if(playerScore[i] > maxScore) maxScore = playerScore[i];
        }
        System.out.print("Max score was: " + maxScore);
    }
}
