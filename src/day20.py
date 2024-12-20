from aoc import Aoc
from dijkstra import BuildGraph, Dijkstra, BackPedal
import itertools
import math
import re
import sys

# Day 20
# https://adventofcode.com/2024

class Day20Solution(Aoc):

   def Run(self):
      self.StartDay(20, "Race Condition")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(20)

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
      ###############
      #...#...#.....#
      #.#.#.#.#.###.#
      #S#...#.#.#...#
      #######.#.#.###
      #######.#.#...#
      #######.#.###.#
      ###..E#...#...#
      ###.#######.###
      #...###...#...#
      #.#####.#.###.#
      #.#...#.#.#...#
      #.#.#.#.#.#.###
      #...#...#...###
      ###############
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 84

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
      data = []
      start = None
      end = None
      for y, line in enumerate(self.inputdata):
         row = []
         for x, col in enumerate(line):
            if col == ".":
               row.append(0)
            elif col == "#":
               row.append(9999)
            elif col == "S":
               row.append(0)
               start = (x, y)
            elif col == "E":
               end = (x, y)
               row.append(0)

         data.append(row)

      return data, start, end

   def PrintGrid(self, grid, path):
      for y, line in enumerate(grid):
         for x, col in enumerate(line):
            if col > 1:
               print("#", end="")
            elif (x, y) in path:
               print("o", end="")
            else:
               print(".", end="")
         print("")

   def TryRace(self, grid, start, end, cheatspot) -> int:
      width = len(grid[0])
      height = len(grid)

      if cheatspot is not None:
         grid[cheatspot[1]][cheatspot[0]] = 0

      #print("Building Graph")
      graph, costs, parents = BuildGraph(grid)
      costs[start] = 0

      #print("Searching")
      result = Dijkstra(start, end, graph, costs, parents)
      path = BackPedal(start, end, result)

      #self.PrintGrid(grid, path)

      if cheatspot is not None:
         grid[cheatspot[1]][cheatspot[0]] = 9999

      cheats = 0
      for p in path:
         if grid[p[1]][p[0]] > 1:
            cheats += 1

      return len(path) - 1, cheats

   def PartA(self):
      self.StartPartA()

      grid, start, end = self.ParseInput()
      answer = 0

      normal_length, cheats = self.TryRace(grid, start, end, None)
      print(f"Normal length: {normal_length}")

      """
      width = len(grid[0])
      height = len(grid)
      print(f"Size: {width}x{height}")
      
      for y in range(1, height - 1):
         for x in range(1, width - 1):
            if grid[y][x] == 9999:
               print(f"{x},{y}")

               length, cheats = self.TryRace(grid, start, end, (x, y))
               print(f"-> length {length} has {cheats} cheats -> {normal_length - length} steps shorter")
               if cheats == 1 and length + 100 < normal_length:
                  answer += 1
      """

      # Attempt 1: 970 is too low

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      grid, start, end = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day20Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

