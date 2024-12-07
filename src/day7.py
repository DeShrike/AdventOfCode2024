from aoc import Aoc
import itertools
import math
import re
import sys

# Day 7
# https://adventofcode.com/2024

class Day7Solution(Aoc):

   def Run(self):
      self.StartDay(7, "Bridge Repair")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(7)

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
      190: 10 19
      3267: 81 40 27
      83: 17 5
      156: 15 6
      7290: 6 8 6 15
      161011: 16 10 13
      192: 17 8 14
      21037: 9 7 18 13
      292: 11 6 16 20
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 3749

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 11387

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         parts = line.split(":")
         nums = parts[1].strip().split(" ")
         data.append((int(parts[0]), [int(num) for num in nums]))

      return data

   def EvaluateA(self, nums, comb: int) -> int:
      e = nums[0]
      for n in range(1, len(nums)):
         if comb & (1 << (n - 1)) == 1 << (n - 1):
            e = e + nums[n]
         else:
            e = e * nums[n]
      return e

   def EvaluateB(self, nums, comb: int) -> int:
      e = nums[0]
      for n in range(1, len(nums)):
         r = comb % 3
         comb = comb // 3
         if r == 0:
            e = e + nums[n]
         elif r == 1:
            e = e * nums[n]
         else:
            #e = int(str(e) + str(nums[n]))
            e = e * (10 ** len(str(nums[n]))) + nums[n]
      return e

   def CheckA(self, data) -> bool:
      k = data[0]
      v = data[1]
      r = 2 ** (len(v) - 1)
      for comb in range(r):
         e = self.EvaluateA(v, comb)
         if e == k:
            return True
      return False

   def CheckB(self, data) -> bool:
      k = data[0]
      v = data[1]
      r = 3 ** (len(v) - 1)
      for comb in range(r):
         e = self.EvaluateB(v, comb)
         if e == k:
            return True
      return False

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      answer = 0
      for line in data:
         if self.CheckA(line):
            answer += line[0]

      # Attempt 1: 6392012775707 is too low
      # Attempt 2: 6392012777720 is correct

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = 0
      for line in data:
         if self.CheckA(line):
            answer += line[0]
         elif self.CheckB(line):
            answer += line[0]

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day7Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

