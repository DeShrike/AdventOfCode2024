from aoc import Aoc
import itertools
import math
import re
import sys

# Day 19
# https://adventofcode.com/2024

class Day19Solution(Aoc):

   def Run(self):
      self.StartDay(19, "Linen Layout")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(19)

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
      r, wr, b, g, bwu, rb, gb, br

      brwrr
      bggr
      gbbr
      rrbgbr
      ubwu
      bwurrg
      brgr
      bbrgwb
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 6

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
      patterns = None
      designs = []
      for line in self.inputdata:
         if line == "":
            continue
         if "," in line:
            patterns = line.split(",")
         else:
            designs.append(line.strip(" "))

      return patterns, designs

   def PartA(self):
      self.StartPartA()

      patterns, designs = self.ParseInput()
      
      reg = "^("
      for p in patterns:
         reg += "(" + p.strip() + ")*"
      reg += ")*$"
      #print(reg)
      #print(len(reg))
      answer = 0
      
      rx = re.compile(reg)

      for d in designs:
         match = rx.search(d)
         if match:
            answer += 1

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day19Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

