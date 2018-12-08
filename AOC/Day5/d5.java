import java.util.*;
import java.io.*;

public class d5 {

    public static void main(String[] args)throws Exception {
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        int c;
        ArrayList<Character> list = new ArrayList<Character>();
        // Splits the input into a list of char's
        while ((c = br.read()) != -1) {
            if((int)c != 10) list.add((Character)(char)c);
        }

        // -------------------- PART 1 --------------------

        ArrayList<Character> reactedList = polymerReaction(list);

        System.out.println("/-------------- PART 1 --------------/");
        System.out.println("Size: " + reactedList.size());

        // -------------------- PART 2 --------------------

    }

    public static ArrayList<Character> polymerReaction(ArrayList<Character> _list) {
        ArrayList<Character> list = new ArrayList<Character>();
        for(Character c : _list) list.add(c);

        boolean removedItem = false;
        int numRemoves = 0;
        // Looking for reactions
        do {
            Character lastLetter = list.get(0);
            removedItem = false;
            for(int i = 1; i < list.size(); i++) {
                Character currentLetter = list.get(i);
                Character currUpper = (Character)Character.toUpperCase(currentLetter);
                Character lastUpper = (Character)Character.toUpperCase(lastLetter);

                // Check if reaction is suppose to happen
                if(!currentLetter.equals(lastLetter) && currUpper.equals(lastUpper)) {

                        // Remove both elements
                        list.remove(i);
                        list.remove(i-1);
                        removedItem = true;
                        numRemoves++;

                        if(list.size() - i > 0) {
                            i--;
                            lastLetter = list.get(i);
                        }
                } else {
                    lastLetter = currentLetter;
                }
            }
        } while(removedItem && list.size() > 1);
        return list;
    }

}
