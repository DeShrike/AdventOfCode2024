from aoc import Aoc
import itertools
import math
import re
import sys

# Day 25
# https://adventofcode.com/2024

class Day25Solution(Aoc):

   def Run(self):
      self.StartDay(25, "Code Chronicle")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(25)

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
      #####
      .####
      .####
      .####
      .#.#.
      .#...
      .....

      #####
      ##.##
      .#.##
      ...##
      ...#.
      ...#.
      .....

      .....
      #....
      #....
      #...#
      #.#.#
      #.###
      #####

      .....
      .....
      #.#..
      ###..
      ###.#
      ###.#
      #####

      .....
      .....
      .....
      #....
      #.#..
      #.#.#
      #####
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 3

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
      locks = []
      keys = []
      lock = key = None
      i = 0
      while True:
         line = self.inputdata[i]
         if line == "":
            i += 1
            continue
         elif line == "#####":
            lock = [0, 0, 0, 0, 0]
            locks.append(lock)
            for ii in range(6):
               i += 1
               line = self.inputdata[i]
               for c in range(len(line)):
                  if line[c] == "#":
                     lock[c] += 1
         elif line == ".....":
            key = [-1, -1, -1, -1, -1]
            keys.append(key)
            for ii in range(6):
               i += 1
               line = self.inputdata[i]
               for c in range(len(line)):
                  if line[c] == "#":
                     key[c] += 1
         i += 1
         if i >= len(self.inputdata):
            break

      return locks, keys

   def PartA(self):
      self.StartPartA()

      locks, keys = self.ParseInput()

      answer = 0
      for lock in locks:
         for key in keys:
            if max([(lock[i] + key[i]) for i in range(5)]) <= 5:
               answer += 1

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day25Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

