from aoc import Aoc
import itertools
import math
import re
import sys

# Day 1
# https://adventofcode.com/2024

class Day1Solution(Aoc):

   def Run(self):
      self.StartDay(1, "Historian Hysteria")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(1)

      goal = self.TestDataA()
      self.PartA()
      self.Assert(self.GetAnswerA(), goal)

      #goal = self.TestDataB()
      #self.PartB()
      #self.Assert(self.GetAnswerB(), goal)

   def TestDataA(self):
      self.inputdata.clear()
      testdata = \
      """
      3   4
      4   3
      2   5
      1   3
      3   9
      3   3
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 11

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
      list1 = [int(line.replace("   ", " ").split(" ")[0]) for line in self.inputdata]
      list2 = [int(line.replace("   ", " ").split(" ")[1]) for line in self.inputdata]

      return list1, list2

   def PartA(self):
      self.StartPartA()

      list1, list2 = self.ParseInput()
      answer = sum([abs(v1 - v2) for v1, v2 in zip(sorted(list1), sorted(list2))])

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day1Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

