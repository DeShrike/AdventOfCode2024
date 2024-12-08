from aoc import Aoc
import itertools
import math
import re
import sys
from utilities import isingrid

# Day 8
# https://adventofcode.com/2024

class Day8Solution(Aoc):

   def Run(self):
      self.StartDay(8, "Resonant Collinearity")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(8)

      goal = self.TestDataA()
      self.PartA()
      self.Assert(self.GetAnswerA(), goal)

      goal = self.TestDataB()
      self.PartB()
      self.Assert(self.GetAnswerB(), goal)

   def TestDataA(self):
      self.inputdata.clear()
      testdata = \
      """
      ............
      ........0...
      .....0......
      .......0....
      ....0.......
      ......A.....
      ............
      ............
      ........A...
      .........A..
      ............
      ............
      """
      testdatax = \
      """
      ..........
      ..........
      ..........
      ....a.....
      ........a.
      .....a....
      ..........
      ..........
      ..........
      ..........
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 14

   def TestDataB(self):
      self.inputdata.clear()
      # self.TestDataA()    # If test data is same as test data for part A
      testdata = \
      """
      1000
      2000
      3000
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return None

   def ParseInput(self):
      grid = []
      for line in self.inputdata:
         grid.append(list(line))

      return grid

   def PartA(self):
      self.StartPartA()

      grid = self.ParseInput()
      width = len(grid[0])
      height = len(grid)
      print(f"Size: {width} x {height}")
      letters = {}
      for y in range(height):
         for x in range(width):
            c = grid[y][x]
            if c == ".":
               continue
            if c not in letters:
               letters[c] = []
            letters[c].append((x, y))
      #print(letters)
      #print("")
      antinodes = set()
      for letter, lijst in letters.items():
         for i, pos in enumerate(lijst):
            for j, pos2 in enumerate(lijst):
               if i == j:
                  continue
               if pos2[0] < pos[0] and pos2[1] < pos[1]:
                  continue
               dx = pos2[0] - pos[0]
               dy = pos2[1] - pos[1]
               antinodes.add((pos[0] - dx, pos[1] - dy))
               antinodes.add((pos2[0] + dx, pos2[1] + dy))
               #p1 = (pos[0] - dx, pos[1] - dy)
               #p2 = (pos2[0] + dx, pos2[1] + dy)
               #print(f"1: {pos}    2: {pos2}  dx: {dx} dy: {dy}")
               #print(f"Added  {p1}   and   {p2}")
               #a = input()
         #break
      #print(antinodes)
      #print("")
      filtered = [an for an in antinodes if isingrid(an[0], an[1], width, height)]
      #print(filtered)
      answer = len(filtered)

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day8Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

