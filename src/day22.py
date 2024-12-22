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
      testdata = \
      """
      1
      2
      3
      2024
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 23

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

      numbers = self.ParseInput()
      answer = None

      seq = {}
      for num in numbers:
         secret = num
         s1 = s2 = s3 = s4 = s5 = 0
         s5 = secret % 10
         for step in range(2000):
            secret = self.Step(secret)
            price = secret % 10
            s1, s2, s3, s4, s5 = s2, s3, s4, s5, price
            d1 = s2 - s1
            d2 = s3 - s2
            d3 = s4 - s3
            d4 = s5 - s4

            if step >= 3:
               k = (d1, d2, d3, d4)
               if k not in seq:
                  seq[k] = []
               f = False
               for n in seq[k]:
                  if n[1] == num:
                     f = True
               if not f:
                  seq[k].append((price, num))

      bananas = []
      for k, v in seq.items():
         if len(v) > 2:
            t = sum([p[0] for p in v])
            bananas.append(t)

      # Attempt 1: 1459 is too low
      # Attempt 2: 1614 is correct

      answer = max(bananas)
      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day22Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

