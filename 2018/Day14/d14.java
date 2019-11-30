import java.util.ArrayList;

public class d14 {
    public static void main (String[] args) throws Exception {
        String rawInput = "084601";
        int input_P1 = Integer.parseInt(rawInput); // input part 1

        int part2Index = -1;

        // List that contains all the scores;
        ArrayList<Integer> list = new ArrayList<Integer>();
        list.add(3); list.add(7);  // Add initial scores

        ArrayList<Integer> input_p2 = new ArrayList<Integer>();
        for(Character c : rawInput.toCharArray()) {
            input_p2.add(Character.getNumericValue(c));
        }

        int fstIndex = 0;
        int sndIndex = 1;
        int numAdded = 0;

        while(list.size() < input_P1 + 10 || part2Index == -1 ) {
            int newValue = list.get(fstIndex) + list.get(sndIndex);
            if(newValue > 9) {
                list.add(newValue / 10);
                list.add(newValue % 10);
                numAdded = 2;
            } else {
                list.add(newValue);
                numAdded = 1;
            }
            fstIndex += list.get(fstIndex) + 1;
            fstIndex = (fstIndex >= list.size()) ? fstIndex - list.size() : fstIndex;

            sndIndex += list.get(sndIndex) + 1;
            sndIndex = (sndIndex >= list.size()) ? sndIndex - list.size() : sndIndex;
            sndIndex = (sndIndex >= list.size()) ? sndIndex - list.size() : sndIndex;
            // Have to run this twice becuase in the first step for elf 2 he goes
            // around the list two times.

            // Logic for part 2
            while(numAdded > 0 && part2Index == -1) {
                numAdded--;
                boolean allMatch = true;
                for(int i = 1; (i < input_p2.size() + numAdded) && allMatch; i++) {
                    if(input_p2.get(input_p2.size() - i) != list.get(list.size() - i - numAdded)) {
                        allMatch = false;
                    }
                }
                if(allMatch) {
                    part2Index = list.size() - numAdded;
                }
            }
        }
        System.out.println("------------- PART 1 -------------");
        System.out.println(list.subList(input_P1, input_P1 + 10).toString());
        System.out.println("------------- PART 2 -------------");
        System.out.println(part2Index - input_p2.size() + " elements before.");
    }
}
