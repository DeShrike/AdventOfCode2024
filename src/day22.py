from aoc import Aoc
import itertools
import math
import re
import sys

# Day 22
# https://adventofcode.com/2024

class Day22Solution(Aoc):

   def Run(self):
      self.StartDay(22, "Monkey Market")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(22)

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
      1
      10
      100
      2024
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 37327623

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
         data.append(int(line))

      return data

   def Prune(self, num: int) -> int:
      return num % 16777216

   def Step(self, num: int) -> int:
      n64 = num * 64
      s1 = n64 ^ num
      s1 = self.Prune(s1)

      n32 = s1 // 32
      s2 = n32 ^ s1
      s2 = self.Prune(s2)

      n2048 = s2 * 2048
      s3 = n2048 ^ s2
      s3 = self.Prune(s3)
      return s3

   def PartA(self):
      self.StartPartA()

      numbers = self.ParseInput()
      answer = 0
      for num in numbers:
         secret = num
         for step in range(2000):
            secret = self.Step(secret)
         answer += secret

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day22Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

