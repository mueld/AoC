package Day1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;;

public class Day1 {
  public static void main(String[] args) {
    var inputFile = new File("Day1/CaloriesIntakes.txt");
    if (!inputFile.exists()) {
      System.out.println("File doesnt exists!!");
      return;
    }
    var numbers = new ArrayList<Integer>();
    try (BufferedReader reader = new BufferedReader(new FileReader(inputFile))) {

      var line = "";
      var localMax = 0;
      var max = 0;
      var currentMaximus = new ArrayList<Integer>();

      while ((line = reader.readLine()) != null) {
        if (!line.isEmpty()) {

          var number = Integer.valueOf(line);
          localMax += number;
        } else {

          currentMaximus.add(localMax);
          Collections.sort(currentMaximus);

          if (currentMaximus.size() > 3) {
            currentMaximus.remove(0);
          }

          localMax = 0;
        }
      }

      for (var i : currentMaximus) {
        max += i;
      }
      System.out.println(max);
    } catch (Exception e) {

    }

  }
}
