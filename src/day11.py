from aoc import Aoc
import itertools
import math
import re
import sys

# Day 11
# https://adventofcode.com/2024

class Day11Solution(Aoc):

   def Run(self):
      self.StartDay(11, "Plutonian Pebbles")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(11)

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
      125 17
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 55312

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return None

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def Blink(self, stones):
      newstones = []
      for stone in stones:
         if stone == 0:
            newstones.append(1)
         elif len(str(stone)) % 2 == 0:
            s = str(stone)
            s1 = s[:len(s) // 2]
            s2 = s[len(s) // 2:]
            newstones.append(int(s1))
            newstones.append(int(s2))
         else:
            newstones.append(stone * 2024)
      return newstones

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      stones = [int(num) for num in data[0].split(" ")]
      for _ in range(25):
         stones = self.Blink(stones)
      answer = len(stones)

      self.ShowAnswer(answer)


   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      stones = [int(num) for num in data[0].split(" ")]
      prev = len(stones)
      for blink in range(75):
         stones = self.Blink(stones)
         print(f"{blink}  -> {len(stones)}  {len(stones) - prev}")
         prev = len(stones)

      answer = 0

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day11Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

