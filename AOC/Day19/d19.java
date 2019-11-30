import java.util.*;
import java.io.*;

public class d19 {

    public static int[] registers = new int[6];
    public static int pointer = -1;

    public static void main(String[] args) throws Exception {
        // --- Read input ---
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String str;
        ArrayList<Tuple> input = new ArrayList<Tuple>();

        if((str = br.readLine()) != null) {
            pointer = Integer.parseInt(str.split(" ")[1]);
        }

        while((str = br.readLine()) != null) {
            String instr = str.split(" ")[0];
            int[] list = new int[3];
            for(int i = 0; i < 3; i++) {
                list[i] = Integer.parseInt(str.split(" ")[i+1]);
            }
            input.add(new Tuple(instr, list));
        }

        // --- Other stuff ---
        boolean outOfIndex = false;
        while(!outOfIndex && registers[pointer] < input.size() && registers[pointer] >= 0) {
            Tuple currentInstr = input.get(registers[pointer]);

            outOfIndex = opcode(currentInstr);

            registers[pointer]++;
        }

        System.out.println("---------------- Part 1 ----------------");
        System.out.println("Value in register 0: " + registers[0]);

        System.out.println("---------------- Part 2 ----------------");
        System.out.println("Look at 'reverseEnginering' file.");
        System.out.println("To get the anweer i first looked at part 1.");
        System.out.println("I realised that the answer was the sum of all the prime factors");
        System.out.println("from whats initially in register 5.");
        System.out.println("In part 1: 1017 => 1 + 3 + + 9 + 113 + 339 + 1017 = 1482");
        System.out.println("In part 2: 10551417 => 1 + 3 + 3517139 + 10551417 = 14068560");
    }


    public static boolean opcode(Tuple t) throws Exception {
        String opcode = t.instr;
        int A = t.list[0];
        int B = t.list[1];
        int C = t.list[2];

        try{
            switch (opcode) {
                case "addr": // addr
                    registers[C] = registers[A] + registers[B];
                    if(A == 4 && B == 0 && C == 0) {
                        System.out.println(registers[1] + " * " + registers[4] + " = " + registers[5] + " - " + registers[0]);
                    }
                    return false;

                case "addi": //addi
                    registers[C] = registers[A] + B;
                    return false;

                case "mulr": // mulr
                    registers[C] = registers[A] * registers[B];
                    return false;

                case "muli": // muli
                    registers[C] = registers[A] * B;
                    return false;

                case "banr": // banr
                    registers[C] = registers[A] & registers[B];
                    return false;

                case "bani": // bani
                    registers[C] = registers[A] & B;
                    return false;

                case "borr": // borr
                    registers[C] = registers[A] | registers[B];
                    return false;

                case "bori": // bori
                    registers[C] = registers[A] | B;
                    return false;

                case "setr": // setr
                    registers[C] = registers[A];
                    return false;

                case "seti": //seti
                    registers[C] = A;
                    return false;

                case "gtir": // gtir
                    registers[C] = A > registers[B] ? 1 : 0;
                    return false;

                case "gtri": // gtri
                    registers[C] = registers[A] > B ? 1 : 0;
                    return false;

                case "gtrr": // gtrr
                    registers[C] = registers[A] > registers[B] ? 1 : 0;
                    return false;

                case "equir": // equir
                   registers[C] = A ==registers[B] ? 1 : 0;
                    return false;

                case "eqri": // eqri
                   registers[C] =registers[A] == B ? 1 : 0;
                    return false;

                case "eqrr": // eqrr
                   registers[C] =registers[A] ==registers[B] ? 1 : 0;
                    return false;

                default:
                    throw new Exception("INVALID OPCODE: " + opcode);
            }
        } catch(ArrayIndexOutOfBoundsException ident) {
            return true;
        }
    }
}
