from aoc import Aoc
from lesolver import LinearEquationSolver
import itertools
import math
import re
import sys

# Day 13
# https://adventofcode.com/2024

class Day13Solution(Aoc):

   def Run(self):
      self.StartDay(13, "Claw Contraption")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(13)

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
      Button A: X+94, Y+34
      Button B: X+22, Y+67
      Prize: X=8400, Y=5400

      Button A: X+26, Y+66
      Button B: X+67, Y+21
      Prize: X=12748, Y=12176

      Button A: X+17, Y+86
      Button B: X+84, Y+37
      Prize: X=7870, Y=6450

      Button A: X+69, Y+23
      Button B: X+27, Y+71
      Prize: X=18641, Y=10279
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 480

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 875318608908

   def ParseInput(self):
      rx1 = re.compile("^Button (?P<b>[AB])\: X\+(?P<x>[0-9]*), Y\+(?P<y>[0-9]*)$")
      rx2 = re.compile("^Prize: X=(?P<x>[0-9]*), Y=(?P<y>[0-9]*)$")

      machines = [] # [(ax, ay, bx, by, px, py), ...]
      
      ax = ay = bx = by = px = py = 0
      
      for line in self.inputdata:
         if line == "":
            machines.append((ax, ay, bx, by, px, py))
            continue
         match = rx1.search(line)
         if match:
            l = match["b"]
            if l == "A":
               ax = int(match["x"])
               ay = int(match["y"])
            else:
               bx = int(match["x"])
               by = int(match["y"])
         else:
            match = rx2.search(line)
            if match:
               px = int(match["x"])
               py = int(match["y"])
            else:
               print("Bad")

      machines.append((ax, ay, bx, by, px, py))

      return machines

   def Play(self, machine):
      aa = 3
      bb = 1
      ax, ay, bx, by, px, py = machine
      
      sa = sb = None
      mintokens = 1_000_000
      for b in range(100):
         for a in range(100):
            if a * ax + b * bx == px and a * ay + b * by == py:
               tokens = aa * a + bb * b
               if tokens < mintokens:
                  mintokens = tokens
                  sa, sb = a, b
      return mintokens if mintokens != 1_000_000 else 0

   def Solve(self, machine):
      to_add = 10_000_000_000_000
      aa = 3
      bb = 1
      ax, ay, bx, by, px, py = machine
      px += to_add
      py += to_add
      solver = LinearEquationSolver(ax, bx, px, ay, by, py)
      try:
         a, b = solver.solve_equations()
         if a == int(a) and b == int(b):
            tokens = aa * int(a) + bb * int(b)
            return tokens
      except ValueError as e:
         print(f"Error: {e}")

      return 0

   def PartA(self):
      self.StartPartA()

      machines = self.ParseInput()
      answer = 0
      for ma in machines:
         answer += self.Play(ma)

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      machines = self.ParseInput()
      answer = 0
      for ma in machines:
         answer += self.Solve(ma)

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day13Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

