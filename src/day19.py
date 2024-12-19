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
      self.TestDataA()
      return 16

   def ParseInput(self):
      patterns = None
      designs = []
      for line in self.inputdata:
         if line == "":
            continue
         if "," in line:
            patterns = [l.strip(" ") for l in line.split(",")]
         else:
            designs.append(line.strip(" "))

      return patterns, designs

   def CountWays(self, design: str, patterns, level: int) -> int:
      count = 0
      if design == "":
         return 1
      for p in patterns:
         #if level < 10:
         #   print((" " * level) + p, level, len(patterns))
         #print(f" pattern: {p}")
         if design[0:len(p)] == p:
            rest = design[len(p):]
            #pp = [p for p in patterns if p in rest]
            #if len(pp) == 0:
            #   continue
            #print(len(patterns), len(pp))
            count += self.CountWays(rest, patterns, level + 1)
      return count

   def PartA(self):
      self.StartPartA()

      patterns, designs = self.ParseInput()

      reg = "^("
      for p in patterns:
         reg += "(" + p.strip() + ")*"
      reg += ")*$"

      rx = re.compile(reg)

      answer = 0

      for d in designs:
         match = rx.search(d)
         if match:
            answer += 1

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      patterns, designs = self.ParseInput()

      reg = "^("
      for p in patterns:
         reg += "(" + p.strip() + ")*"
      reg += ")*$"

      rx = re.compile(reg)

      answer = 0

      """
      for d in designs:
         matches = rx.findall(d)
         answer += len(matches)
      """

      for i, d in enumerate(designs):
         print(f"{i}/{len(designs)}", end="\r")
         match = rx.search(d)
         if match:
            print(d)
            pp = [p for p in patterns if p in d]
            print(len(patterns), len(pp))
            answer += self.CountWays(d, pp, 0)
         #a = input()

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day19Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

