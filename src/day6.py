from aoc import Aoc
import itertools
import math
import re
import sys
from utilities import isingrid

# Day 6
# https://adventofcode.com/2024

class Day6Solution(Aoc):

   def Run(self):
      self.StartDay(6, "Guard Gallivant")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(6)

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
      ....#.....
      .........#
      ..........
      ..#.......
      .......#..
      ..........
      .#..^.....
      ........#.
      #.........
      ......#...
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 41

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
      # rx = re.compile("^(?P<from>[A-Z0-9]{3}) = \((?P<left>[A-Z0-9]{3}), (?P<right>[A-Z0-9]{3})\)$")
      # match = rx.search(line)
      # pos = match["from"]

      grid = []
      for line in self.inputdata:
         grid.append(list(line))

      return grid

   def Step(self, grid, x: int, y: int, direction: int) -> (int, int, int):
      grid[y][x] = "X"
      width = len(grid[0])
      height = len(grid)
      nx = x + self.directions[direction][0]
      ny = y + self.directions[direction][1]
      if isingrid(nx, ny, width, height) and grid[ny][nx] == "#":
         direction = (direction + 1) % len(self.directions)
      else:
         x = nx
         y = ny
      return (x, y, direction)
      
   def PartA(self):
      self.StartPartA()

      self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
      grid = self.ParseInput()
      width = len(grid[0])
      height = len(grid)
      x = 0
      y = 0
      for yy, row in enumerate(grid):
         for xx, row in enumerate(row):
            if row == "^":
               x = xx
               y = yy
               break
      direction = 0
      while True:
         x, y, direction = self.Step(grid, x, y, direction)
         if not isingrid(x, y, width, height):
            break

      answer = sum(len([p for p in row if p == "X"]) for row in grid)

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day6Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

