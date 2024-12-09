from aoc import Aoc
import itertools
import math
import re
import sys

# Day 9
# https://adventofcode.com/2024

class Day9Solution(Aoc):

   def Run(self):
      self.StartDay(9, "Disk Fragmenter")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(9)

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
      2333133121414131402
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 1928

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
         data.append(line)

      return data

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      diskmap = list(data[0])

      answer = 0
      idl = 0
      idr = (len(diskmap) // 2) + 1
      #print(f"ID L: {idl}   ID R: {idr}")
      pos = 0
      l = int(diskmap.pop(0))
      freel = int(diskmap.pop(0))
      r = 0
      freer = 0
      while l > 0 or r > 0:
         while l > 0:
            #print(f"{pos} * {idl}")
            answer += idl * pos
            pos += 1
            l -= 1
         while freel > 0:
            if r == 0:
               if len(diskmap) > 0:
                  r = int(diskmap.pop(-1))
                  freer = int(diskmap.pop(-1))
                  idr -= 1
            #print(f"{pos} * {idr}")
            answer += idr * pos
            r -= 1
            pos += 1
            freel -= 1
         if len(diskmap) > 0:
            l = int(diskmap.pop(0))
            if len(diskmap) > 0:
               freel = int(diskmap.pop(0))
            else:
               freel = r
            idl += 1
         

      # Add solution here

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day9Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

