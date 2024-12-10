from aoc import Aoc
from utilities import neighbours4
import itertools
import math
import re
import sys

# Day 10
# https://adventofcode.com/2024

class Day10Solution(Aoc):

   def Run(self):
      self.StartDay(10, "Hoof It")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(10)

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
      89010123
      78121874
      87430965
      96549874
      45678903
      32019012
      01329801
      10456732
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 36

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 81

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append([int(c) for c in line])

      return data

   def Hike(self, grid, x: int, y: int, tops, count: int) -> int:
      size = (len(grid[0]), len(grid))
      h = grid[y][x]
      for nx, ny in neighbours4(x, y, size):
         if grid[ny][nx] == h + 1:
            if grid[ny][nx] == 9:
               tops.add((nx, ny))
               count += 1
            else:
               count = self.Hike(grid, nx, ny, tops, count)

      return count

   def PartA(self):
      self.StartPartA()

      grid = self.ParseInput()
      answer = 0
      for y, row in enumerate(grid):
         for x, col in enumerate(row):
            if col == 0:
               tops = set()
               self.Hike(grid, x, y, tops, 0)
               answer += len(tops)
               
      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      grid = self.ParseInput()
      answer = 0
      for y, row in enumerate(grid):
         for x, col in enumerate(row):
            if col == 0:
               tops = set()
               answer += self.Hike(grid, x, y, tops, 0)

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day10Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

