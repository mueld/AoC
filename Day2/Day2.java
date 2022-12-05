package Day2;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;


public class Day2 {

  public static void main(String[] args) {
    var inputFile = new File("Day2/InputData.txt");
    if (!inputFile.exists()) {
      System.out.println("File doesnt exists!!");
      return;
    }
    var rock = "A";
    var paper = "B";
    var scissors = "C";
    var responseRock = "X";
    var resonsePaper = "Y";
    var responseScissors = "Z";

    var winningTurns = new HashMap<String, String>();
    winningTurns.put("A", resonsePaper);
    winningTurns.put("B", responseScissors);
    winningTurns.put("C", responseRock);

    var losingTurns = new HashMap<String, String>();
    losingTurns.put(rock, responseScissors);
    losingTurns.put(paper, responseRock);
    losingTurns.put(scissors, resonsePaper);

    var drwas = new HashMap<String, String>();
    drwas.put(rock, responseRock);
    drwas.put(paper, resonsePaper);
    drwas.put(scissors, responseScissors);
    // drwas.put(responseRock, rock);
    // drwas.put(resonsePaper, paper);
    // drwas.put(responseScissors, scissors);

    class Turn {
      public HashMap<String, Integer> selectedShapePoints = new HashMap<String, Integer>();
      public static int winningPoints = 6;
      public static int drawPoints = 3;

      public Turn() {
        selectedShapePoints.put(resonsePaper, 2);
        selectedShapePoints.put(responseRock, 1);
        selectedShapePoints.put(responseScissors, 3);
      }

      public int getPoints(String x, String y) {
        var newY = "";
        switch (y) {
          case "X": // lose
            newY = losingTurns.get(x);
            break;

          case "Y": // draw
            newY = drwas.get(x);
            break;
          case "Z": // win
            newY = winningTurns.get(x);
            break;
        }
        if (newY == null || newY.isEmpty()) {
          newY = "";
        }

        var selectedPoint = selectedShapePoints.get(newY);
        if (selectedPoint == null) {
          selectedPoint = 0;
        }
        if (winningTurns.get(x).equals(newY)) {
          return winningPoints + selectedPoint;
        } else if (drwas.get(x).equals(newY)) {
          return drawPoints + selectedPoint;
        } else {
          return selectedPoint;
        }
      }
    }

    try (BufferedReader reader = new BufferedReader(new FileReader(inputFile))) {
      var line = "";
      var turn = new Turn();
      var totalpoints = 0;

      while ((line = reader.readLine()) != null) {
        if (!line.isEmpty()) {
          var splitedLine = line.split(" ");
          var x = splitedLine[0];
          var y = splitedLine[1];
          totalpoints += turn.getPoints(x, y);
        }
      }
      System.out.println(totalpoints);
    } catch (Exception e) {
      System.out.println(e);
    }
  }

}
