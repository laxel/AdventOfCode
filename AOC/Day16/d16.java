import java.io.*;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class d16 {
    public static void main(String[] args) throws Exception {
        // --- Read input ---
        File file = new File("part1.txt");

        BufferedReader br = new BufferedReader(new FileReader(file));
        Pattern p = Pattern.compile("(\\d+),? (\\d+),? (\\d+),? (\\d+)");

        String str;
        int status = 0;
        int index = 0;
        ArrayList<int[][]> input = new ArrayList<int[][]>();

        while((str = br.readLine()) != null) {
            if(status == 0) input.add(new int[3][4]);

            Matcher m = p.matcher(str);
            if(m.find()) {
                for(int i = 1; i < 5; i++) {
                    input.get(index)[status][i-1] = Integer.parseInt(m.group(i));
                }
            }
            status++;
            if(status == 4) {
                status = 0;
                index++;
            }
        }

        int numThreeOrMore = 0;
        ArrayList[] table = new ArrayList[16];
        for (int i = 0; i < table.length; i++) {
            table[i] = new ArrayList();
        }

        for(int[][] l : input) {
            int opcode = l[1][0];
            int A = l[1][1];
            int B = l[1][2];
            int C = l[1][3];

            int numRight = 0;
            ArrayList<Integer> matched = new ArrayList<Integer>();

            for(int code = 0; code < 16; code++) {
                int[] output = opcode(code, A, B, C, l[0]);
                boolean match = true;
                for(int n = 0; n < 4; n++) {
                    if(l[2][n] != output[n]) match = false;
                }
                if(match) {
                    numRight++;
                    matched.add(code);
                }
            }
            if(table[opcode].isEmpty()) {
                for(Integer i : matched) table[opcode].add(i);
            } else {
                for(int _index = 0; _index < table[opcode].size(); _index++) {
                    int i = (int)table[opcode].get(_index);
                    boolean doesExist = false;
                    for(Integer n : matched) {
                        if(i == n) doesExist = true;
                    }
                    if(!doesExist) {
                        table[opcode].remove(_index);
                        _index--;
                    }
                }
            }

            if(numRight >= 3) {
                numThreeOrMore++;
            }

        }

        // ---------------- PART 2 ----------------

        // Get the correct opcode numbers
        boolean removed = true;
        int currentRemoved = -1;
        int nextRemoved = -1;
        HashMap<Integer, Integer> correctOpcode = new HashMap<Integer, Integer>();
        while(removed) {
            removed = false;
            for(int i = 0; i < table.length ; i++) {
                if(table[i] != null) {
                    for(int n = 0; n < table[i].size(); n++) {
                        if((int)table[i].get(n) == currentRemoved) {
                            table[i].remove(n);
                            n--;
                        }
                    }

                    if(table[i].size() == 1 && !removed) {
                        nextRemoved = (int)table[i].get(0);
                        correctOpcode.put(i, (int)table[i].get(0));
                        table[i] = null;
                        removed = true;
                    }
                }
            }
            currentRemoved = nextRemoved;
        }
        System.out.println(correctOpcode.toString());

        // Read part2 file
        file = new File("part2.txt");
        br = new BufferedReader(new FileReader(file));

        ArrayList<int[]> commands = new ArrayList<int[]>();

        while((str = br.readLine()) != null) {
            String[] array = str.split(" ", -1);
            int[] intArray = new int[4];
            for(int n = 0; n < array.length; n++) {
                intArray[n] = Integer.parseInt(array[n]);
            }
            commands.add(intArray);
        }

        int[] registers = new int[4];
        for(int[] command : commands) {
            int opcode = correctOpcode.get(command[0]);
            int A = command[1];
            int B = command[2];
            int C = command[3];
            registers = opcode(opcode, A, B, C, registers);
        }
        for(int i : registers) {
            System.out.print(i + ", ");
        }
        System.out.println();

        System.out.println(numThreeOrMore);

    }

    public static int[] opcode(int opcode, int A, int B, int C, int[] _registers) throws Exception {
        int[] registers = new int[_registers.length];
        for(int i = 0; i < _registers.length; i++) {
            registers[i] = _registers[i];
        }

        switch (opcode) {
            case 0: // addr
                registers[C] = registers[A] + registers[B];
                return registers;

            case 1: //addi
                registers[C] = registers[A] + B;
                return registers;

            case 2: // mulr
                registers[C] = registers[A] * registers[B];
                return registers;

            case 3: // muli
                registers[C] = registers[A] * B;
                return registers;

            case 4: // banr
                registers[C] = registers[A] & registers[B];
                return registers;

            case 5: // bani
                registers[C] = registers[A] & B;
                return registers;

            case 6: // borr
                registers[C] = registers[A] | registers[B];
                return registers;

            case 7: // bori
                registers[C] = registers[A] | B;
                return registers;

            case 8: // setr
                registers[C] = registers[A];
                return registers;

            case 9: //seti
                registers[C] = A;
                return registers;

            case 10: // gtir
                registers[C] = A > registers[B] ? 1 : 0;
                return registers;

            case 11: // gtri
                registers[C] = registers[A] > B ? 1 : 0;
                return registers;

            case 12: // gtrr
                registers[C] = registers[A] > registers[B] ? 1 : 0;
                return registers;

            case 13: // equir
               registers[C] = A ==registers[B] ? 1 : 0;
                return registers;

            case 14: // eqri
               registers[C] =registers[A] == B ? 1 : 0;
                return registers;

            case 15: // eqrr
               registers[C] =registers[A] ==registers[B] ? 1 : 0;
                return registers;

            default:
                throw new Exception("INVALID OPCODE: " + opcode);

        }
    }
}
