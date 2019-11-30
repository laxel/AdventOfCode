import java.util.*;
import java.io.*;

public class d5 {

    public static void main(String[] args)throws Exception {
        // Read input
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        int c;
        ArrayList<Character> list = new ArrayList<Character>();
        // Splits the input into a list of char's
        while ((c = br.read()) != -1) {
            if((int)c != 10) list.add((Character)(char)c);
        }

        part1(list);
        part2(list);
    }
    public static void part1(ArrayList<Character> list) {
        // -------------------- PART 1 --------------------
        ArrayList<Character> listCopy = new ArrayList<Character>();
        for(Character c : list) listCopy.add(c);

        polymerReaction(listCopy);

        System.out.println("/-------------- PART 1 --------------/");
        System.out.println("Size: " + listCopy.size());
    }

    public static void part2(ArrayList<Character> list) {
        // -------------------- PART 2 --------------------
        // Find all letters in input:
        HashSet<Character> letters = new HashSet<Character>();
        for(Character ch : list) {
            Character upperCaseCh = (Character)Character.toUpperCase(ch);
            letters.add(upperCaseCh);
        }

        // Try to react individually with each letter found in previus step.
        int minSize = Integer.MAX_VALUE;
        Character bestChar = ' ';
        for(Character ch : letters) {
            // Copy original list
            ArrayList<Character> listCopy = new ArrayList<Character>();
            for(Character c : list) listCopy.add(c);
            // Remove chosen letter
            removeLetter(listCopy, ch);
            // Do the reaction on the list
            polymerReaction(listCopy);
            if(listCopy.size() < minSize) {
                minSize = listCopy.size();
                bestChar = ch;
            }

        }
        System.out.println("/-------------- PART 2 --------------/");
        System.out.println("The 'best' character was " + bestChar + " with size " + minSize);
    }

    public static void polymerReaction(ArrayList<Character> list) {

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
    }

    public static void removeLetter(ArrayList<Character> list, Character letter) {
        for(int i = 0; i < list.size(); i++) {
            Character UpperCaseCh = (Character)Character.toUpperCase(list.get(i));
            if(letter.equals(UpperCaseCh)) {
                list.remove(i);
                i--;
            }
        }
    }
}
