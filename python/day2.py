from aoc import Aoc
import itertools
import math
import re
import sys

# Day 2
# https://adventofcode.com/2024

class Day2Solution(Aoc):

   def Run(self):
      self.StartDay(2, "Red-Nosed Reports")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(2)

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
      7 6 4 2 1
      1 2 7 8 9
      9 7 6 2 1
      1 3 2 4 5
      8 6 4 4 1
      1 3 6 7 9
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 2

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 4

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append([int(level) for level in line.split(" ")])

      return data

   def ReportIsSafe(self, report) -> bool:
      hasDec = False
      hasInc = False
      for ix, l in enumerate(report):
         if ix == 0:
            continue
         diff = report[ix - 1] - l
         if abs(diff) > 3 or diff == 0:
            return False
         if diff < 0:
            hasDec = True
            if hasInc:
               return False
         else:
            hasInc = True
            if hasDec:
               return False
      return True

   def ReportIsSafeWithDampener(self, report) -> bool:
      if self.ReportIsSafe(report):
         return True
      for i in range(len(report)):
         temp = report[:]
         temp.pop(i)
         if self.ReportIsSafe(temp):
            return True

      return False

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      answer = len([report for report in data if self.ReportIsSafe(report)])

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = len([report for report in data if self.ReportIsSafeWithDampener(report)])

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day2Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

