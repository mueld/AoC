package Day3;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

import org.w3c.dom.css.Counter;;

public class Day3 {
  public static void main(String[] args) {
    var inputFile = new File("Day3/InputData.txt");
    if (!inputFile.exists()) {
      System.out.println("File doesnt exists!!");
      return;
    }

    try (BufferedReader reader = new BufferedReader(new FileReader(inputFile))) {

      var line = "";
      var sumOfAllLetters = 0;
      var sum = 0;
      var GroupLetters = new ArrayList<HashSet<Integer>>();

      var lineCounters = 0;
      var foundItemsCount = 0;
      while ((line = reader.readLine()) != null) {
        if (!line.isEmpty()) {

          if (lineCounters == 0) {
            GroupLetters = new ArrayList<HashSet<Integer>>();
            GroupLetters.add(new HashSet<>());
            foundItemsCount = 0;
          }

          var letters = GroupLetters.get(lineCounters);

          var firstHalf = line.subSequence(0, line.length()).chars().toArray();

          for (Integer c : firstHalf) {
            letters.add(c);

            if (foundItemsCount == 3) {
              break;
            }
            foundItemsCount = 0;

            for (var i = 0; i < GroupLetters.size(); i++) {
              if (GroupLetters.get(i).contains(c)) {
                foundItemsCount++;
                if (foundItemsCount == 3) {
                  if (c < 91) {
                    sum += (c - 38);
                  } else {
                    sum += (c - 96);
                  }
                  break;
                }
              }
            }
          }
          lineCounters++;
          GroupLetters.add(new HashSet<>());
          lineCounters = lineCounters % 3;
        }
      }

      // while ((line = reader.readLine()) != null) {
      // if (!line.isEmpty()) {
      // var lettersFromFirstHalf = new HashSet<Integer>();
      // var lettersFromSecondHalf = new HashSet<Integer>();

      // if ((line.length() % 2) != 0) {
      // var test = false;
      // }

      // var firstHalf = line.subSequence(0, line.length() / 2);
      // var secondHald = line.subSequence(line.length() / 2, line.length());

      // firstHalf.chars().forEach(c -> {
      // lettersFromFirstHalf.add(c);
      // });

      // for (Integer c : secondHald.chars().toArray()) {
      // if (lettersFromFirstHalf.contains(c)) {

      // if (c < 91) {
      // sum += (c - 38);
      // } else {
      // sum += (c - 96);
      // }
      // break;
      // }

      // }
      // }
      // }
      System.out.println(sum);

    } catch (Exception e) {
      System.out.println(e.toString());
    }

  }
}
