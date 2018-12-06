import java.util.*;
import java.io.*;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;

public class d4 {
  public static void main(String[] args)throws Exception {
    File file = new File("input.txt");
    BufferedReader br = new BufferedReader(new FileReader(file));

    //String test = "[1518-07-10 23:54] Guard #3167 begins shift";
    //System.out.println(test.split(" ")[3].substring(1));

    String st;
    ArrayList<String> list = new ArrayList<String>();

    // Read input in to ArrayList ArrayList
    while ((st = br.readLine()) != null) {
      list.add(st.split("]")[0].substring(1));
    }

    // Sort list after date
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
    Collections.sort(list, (s1, s2) -> LocalDateTime.parse(s1, formatter).
      compareTo(LocalDateTime.parse(s2, formatter)));

    // Find amount of hours slept per guard
    boolean isAsleep = false;
    int currentGuard = 0;
    // Key: Guard ID, Value: Time spent sleeping
    HashMap<Integer,Integer> timeSlept = new HashMap<Integer,Integer>();

    for(int i = 0; i < list.size(); i++) {
      String input = list.get(i);
      System.out.println(input);

      /*switch (input.charAt(19)) {
        case 'G': // New shift begins
          currentGuard = Integer.parseInt(input.split(" ")[3].substring(1));
          isAsleep = false;
          break;
        case 'f': // Fall asleep
          isAsleep = true;

          break;
        case 'w': // Wake up
          isAsleep = false;

          break;
      }*/

    }


  }
}
