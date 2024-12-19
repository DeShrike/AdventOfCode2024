from aoc import Aoc
import itertools
import math
import re
import sys

# Day 18
# https://adventofcode.com/2024

class Day18Solution(Aoc):

   def Run(self):
      self.StartDay(18, "RAM Run")
      self.ReadInput()
      self.size = 71
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(18)

      self.size = 7

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
      5,4
      4,2
      4,5
      3,0
      2,1
      6,3
      2,4
      1,5
      0,6
      3,3
      2,6
      5,1
      1,2
      5,5
      2,5
      6,5
      1,4
      0,4
      6,4
      1,1
      6,1
      1,0
      0,5
      1,6
      2,0
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 22

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
      for line in self.inputdata:
         parts = line.split(",")
         x = int(parts[0])
         y = int(parts[1])
         data.append('(x, y))

      return data

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
      
      answer = None

      # Add solution here

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      pairs = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day18Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

