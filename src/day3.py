from aoc import Aoc
import itertools
import math
import re
import sys

# Day 3
# https://adventofcode.com/2024

class Day3Solution(Aoc):

   def Run(self):
      self.StartDay(3, "Mull It Over")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(3)

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
      xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 161

   def TestDataB(self):
      self.inputdata.clear()
      # self.TestDataA()    # If test data is same as test data for part A
      testdata = \
      """
      xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 48

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def PartA(self):
      self.StartPartA()

      rx = re.compile("mul\((?P<num1>[0-9]{1,3}),(?P<num2>[0-9]{1,3})\)")

      data = self.ParseInput()
      answer = 0
      for line in data:
         matches = rx.findall(line)
         for n1, n2 in matches:
            answer += int(n1) * int(n2)

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      rx = re.compile("mul\((?P<num1>[0-9]{1,3}),(?P<num2>[0-9]{1,3})\)|(do\(\))|(don't\(\))")

      data = self.ParseInput()
      answer = 0
      enabled = True
      for line in data:
         matches = rx.findall(line)
         for n1, n2, do, dont in matches:
            if do != "":
               enabled = True
            elif dont != "":
               enabled = False
            elif enabled:
               answer += int(n1) * int(n2)

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day3Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

