package Day4;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;

public class Day4 {
  public static void main(String[] args) {
    var inputFile = new File("Day4/InputData.txt");
    if (!inputFile.exists()) {
      System.out.println("File doesnt exists!!");
      return;
    }

    try (BufferedReader reader = new BufferedReader(new FileReader(inputFile))) {

      var line = "";
      var counter = 0;
      while ((line = reader.readLine()) != null) {
        if (!line.isEmpty()) {
          var groups = line.split(",");
          var elfs = new ArrayList<Elv>();
          for (var group : groups) {
            var ranges = group.split("-");
            elfs.add(new Elv(Integer.parseInt(ranges[0]), Integer.parseInt(ranges[1])));
          }
          if (elfs.size() != 2) {
            System.out.println("Size of elfs doesnt match!!!!");
            return;
          }
          if (ElvPair.FullyContains(elfs.get(0), elfs.get(1))) {
            counter++;
          }
        }
      }

      System.out.println(counter);

    } catch (Exception e) {
      System.out.println(e.toString());
    }

  }
}
