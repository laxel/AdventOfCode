public class Tuple {
  public final String instr;
  public final int[] list;
  public Tuple(String instr, int[] list) {
    this.instr = instr;
    this.list = list;
  }

  @Override
  public String toString() {
      return instr + " - " + list[0] + ", " + list[1] + ", " + list[2]; 
  }
}
