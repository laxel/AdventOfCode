import java.util.*;
import java.io.*;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;

public class d4 {
    public static void main(String[] args)throws Exception {
        // -------------------- PART 1 --------------------
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;
        ArrayList<String> list = new ArrayList<String>();
        HashMap<String, String> map = new HashMap<String, String>();

        // Read input in to ArrayList ArrayList
        while ((st = br.readLine()) != null) {
            String date = st.split("]")[0].substring(1);
            list.add(date); // List with all the dates (only dates!)
            map.put(date,st);
        }

        // Sort list after date
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        Collections.sort(list, (s1, s2) -> LocalDateTime.parse(s1, formatter).
            compareTo(LocalDateTime.parse(s2, formatter)));

        ArrayList<String> sortedList = new ArrayList<String>();
        for(int i = 0; i < list.size(); i++) {
            sortedList.add(map.get(list.get(i)));
            //System.out.println(sortedList.get(i));
        }


        // Find amount of hours slept per guard
        boolean isAsleep = false;
        int asleepSince = 0;
        int currentGuard = 0;
        // Key: Guard ID, Value: Time spent sleeping
        HashMap<Integer,ArrayList<Integer>> timeSlept =
            new HashMap<Integer,ArrayList<Integer>>();

        for(int i = 0; i < sortedList.size(); i++) {
            String input = sortedList.get(i);

            switch (input.charAt(19)) {
            case 'G': // New shift begins
                currentGuard = Integer.parseInt(input.split(" ")[3].substring(1));
                isAsleep = false;
                break;
            case 'f': // Fall asleep
                isAsleep = true;
                asleepSince = Integer.parseInt(input.split("]")[0].split(":")[1]);
                break;
            case 'w': // Wake up
                isAsleep = false;
                ArrayList<Integer> guardSleepTime = timeSlept.get(currentGuard);

                int currentTime = Integer.parseInt(input.split("]")[0].split(":")[1]);

                if (guardSleepTime == null)
                    guardSleepTime = new ArrayList<Integer>(Collections.nCopies(60, 0));

                // Increment timeSlept for the guard
                for(int t = asleepSince; t < currentTime; t++) {
                    guardSleepTime.set(t,guardSleepTime.get(t) + 1);
                }

                timeSlept.put(currentGuard, guardSleepTime);
                break;
            }
        }

        // Finds the guard with the most minutes sleept
        Integer worstGuard = -1;
        int worstMinutes = -1;
        for (Integer guard : timeSlept.keySet()) {
            ArrayList<Integer> array = timeSlept.get(guard);
            int minutesSleept = 0;
            for(Integer w : array) {
                minutesSleept += w;
            }
            if(minutesSleept > worstMinutes) {
                worstGuard = guard;
                worstMinutes = minutesSleept;
            }
        }

        // Find the minutes most frequently sleept on
        ArrayList<Integer> worstList = timeSlept.get(worstGuard);
        int frequentMinute = -1;
        int maxTime = 0;
        for(int q = 0; q < 60; q++) {
            Integer e = worstList.get(q);
            if(e > maxTime) {
                maxTime = e;
                frequentMinute = q;
            }
        }
        System.out.println("/-------------- PART 1 --------------/");
        System.out.println("The guard with most minutes asleep was " + worstGuard + " with " + worstMinutes + " minutes asleep");
        System.out.println("He most frequently sleept on the " + frequentMinute + " minute.");
        System.out.println(worstGuard + " * " + frequentMinute + " = " + (worstGuard*frequentMinute));


        // -------------------- PART 2 --------------------
        int _frequentMinute = -1;
        int _maxTime = 0;
        int guardId = -1;

        for (Integer guard : timeSlept.keySet()) {
            ArrayList<Integer> guardValues = timeSlept.get(guard);

            for(int f = 0; f < 60; f++) {
                Integer v = guardValues.get(f);
                if(v > _maxTime) {
                    _maxTime = v;
                    _frequentMinute = f;
                    guardId = guard;
                }
            }
        }
        System.out.println("/-------------- PART 2 --------------/");
        System.out.println("Guard " + guardId + " was asleep for " + _maxTime + " on minute " + _frequentMinute);
        System.out.println(_frequentMinute + " * " + guardId + " = " + (_frequentMinute * guardId));

    }
}
