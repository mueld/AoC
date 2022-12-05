package Day4;

public class ElvPair {
  public static boolean FullyContains(Elv x, Elv y) {
    if (Contains(x, y)) {
      return true;
    } else if (Contains(y, x)) {
      return true;
    } else if (CheckOverlapping(x, y)) {
      return true;
    } else {
      return CheckOverlapping(y, x);
    }

  }

  public static boolean Contains(Elv x, Elv y) {
    if (y.RangeStart >= x.RangeStart && y.RangeStart <= x.RangeEnd) {
      if (y.RangeEnd <= x.RangeEnd) {
        return true;
      }
    }
    return false;
  }

  public static boolean CheckOverlapping(Elv x, Elv y) {
    if (x.RangeEnd >= y.RangeStart && x.RangeEnd <= y.RangeEnd) {
      return true;
    }
    return false;
  }

}
