from aoc import Aoc
import itertools
import math
import re
import sys

# Day 4
# https://adventofcode.com/2024

class Day4Solution(Aoc):

   def Run(self):
      self.StartDay(4, "AOC")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(4)

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
      MMMSXXMASM
      MSAMXMSMSA
      AMXSXMAAMM
      MSAMASMSMX
      XMASAMXAMM
      XXAMMXXAMA
      SMSMSASXSS
      SAXAMASAAA
      MAMMMXMMMM
      MXMXAXMASX
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 18

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 9

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def Directions(self):
      dirs = [(1, 0),(1, 1),(0, 1),(-1, 1),(-1, 0),(-1, -1),(0, -1),(1, -1)]
      for dir in dirs:
         yield dir

   def isXmas(self, data, x: int, y: int, dx: int, dy: int, ix: int) -> bool:
      word = "XMAS"
      height = len(data)
      width = len(data[0])

      if x < 0 or y < 0 or x >= width or y >= height:
         return False
      if data[y][x] != word[ix]:
         return False
      ix += 1
      if ix >= len(word):
         return True
      if not self.isXmas(data, x + dx, y + dy, dx, dy, ix):
         return False
      return True

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()

      answer = 0

      height = len(data)
      width = len(data[0])
      for x in range(width):
         for y in range(height):
            for dx, dy in self.Directions():
               if self.isXmas(data, x, y, dx, dy, 0):
                  answer += 1

      self.ShowAnswer(answer)

   def isMas1(self, data, x: int, y: int) -> bool:
      return (data[y - 1][x - 1] == "M" and data[y + 1][x + 1] == "S") or \
             (data[y - 1][x - 1] == "S" and data[y + 1][x + 1] == "M")

   def isMas2(self, data, x: int, y: int) -> bool:
      return (data[y - 1][x + 1] == "M" and data[y + 1][x - 1] == "S") or \
             (data[y - 1][x + 1] == "S" and data[y + 1][x - 1] == "M")

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = 0

      height = len(data)
      width = len(data[0])
      for x in range(1, width - 1):
         for y in range(1, height - 1):
            if data[y][x] != "A":
               continue
            if self.isMas1(data, x, y) and self.isMas2(data, x, y):
               answer += 1

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day4Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

