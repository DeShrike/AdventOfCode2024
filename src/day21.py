from aoc import Aoc
import itertools
import math
import re
import sys

# Day 21
# https://adventofcode.com/2024

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"
A = "A"

class NumPad():
   """
   +---+---+---+
   | 7 | 8 | 9 |
   +---+---+---+
   | 4 | 5 | 6 |
   +---+---+---+
   | 1 | 2 | 3 |
   +---+---+---+
       | 0 | A |
       +---+---+
   """
   def __init__(self, mode: int, presser):
      self.pos = A
      self.mode = mode
      self.presser = presser
      self.positions = { 
         "7": (0, 0),
         "8": (1, 0),
         "9": (2, 0),
         "4": (0, 1),
         "5": (1, 1),
         "6": (2, 1),
         "1": (0, 2),
         "2": (1, 2),
         "3": (2, 2),
         "0": (1, 3),
         "A": (2, 3),
      }

   def need(self, key):
      if self.presser is None:
         return key
      seq = ""
      x, y = self.positions[self.pos]
      gx, gy = self.positions[key]

      if gx == 0 and x > 0 and gy < y and y == 3:
         seq += self.presser.need(UP)
         y -= 1

      if gy == 3 and y < 3 and gx > x and x == 0:
         seq += self.presser.need(RIGHT)
         x += 1

      if self.mode == 0:
         while gx < x:
            seq += self.presser.need(LEFT)
            x -= 1

         while gy > y:
            seq += self.presser.need(DOWN)
            y += 1

         while gy < y:
            seq += self.presser.need(UP)
            y -= 1

         while gx > x:
            seq += self.presser.need(RIGHT)
            x += 1
      else:
         while gy < y:
            seq += self.presser.need(UP)
            y -= 1

         while gx < x:
            seq += self.presser.need(LEFT)
            x -= 1

         while gy > y:
            seq += self.presser.need(DOWN)
            y += 1

         while gx > x:
            seq += self.presser.need(RIGHT)
            x += 1
      
      seq += self.presser.need(A)
      self.pos = key

      return seq

class ArrowPad():
   """
       +---+---+
       | ^ | A |
   +---+---+---+
   | < | v | > |
   +---+---+---+
   """
   def __init__(self, presser):
      self.pos = A
      self.presser = presser
      self.moves = {
         (A, UP): [LEFT],
         (A, DOWN): [DOWN, LEFT],
         (A, LEFT): [DOWN, LEFT, LEFT],
         (A, RIGHT): [DOWN],
         (A, A): [],

         (UP, A): [RIGHT],
         (UP, DOWN): [DOWN],
         (UP, LEFT): [DOWN, LEFT],
         (UP, RIGHT): [DOWN, RIGHT],
         (UP, UP): [],

         (DOWN, A): [RIGHT, UP],
         (DOWN, UP): [UP],
         (DOWN, LEFT): [LEFT],
         (DOWN, RIGHT): [RIGHT],
         (DOWN, DOWN): [],

         (RIGHT, A): [UP],
         (RIGHT, UP): [UP, LEFT],
         (RIGHT, LEFT): [LEFT, LEFT],
         (RIGHT, DOWN): [LEFT],
         (RIGHT, RIGHT): [],

         (LEFT, A): [RIGHT, RIGHT, UP],
         (LEFT, UP): [RIGHT, UP],
         (LEFT, RIGHT): [RIGHT, RIGHT],
         (LEFT, DOWN): [RIGHT],
         (LEFT, LEFT): [],
      }

   def need(self, key):
      if self.presser is None:
         return ""
      seq = ""
      steps = self.moves[(self.pos, key)]
      for step in steps:
         seq += self.presser.need(step)
      seq += self.presser.need(A)
      self.pos = key
      return seq


class Day21Solution(Aoc):

   def Run(self):
      self.StartDay(21, "Keypad Conundrum")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(21)

      goal = self.TestDataA()
      self.PartA()
      self.Assert(self.GetAnswerA(), goal)

   def TestDataA(self):
      self.inputdata.clear()
      testdata = \
      """
      029A
      980A
      179A
      456A
      379A
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 126384

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def CalcComplexity(self, code: str, seq: str) -> int:
      rx = re.compile("(?P<num>[0-9]*)")
      match = rx.search(code)
      #print(f"{len(seq)} * {int(match['num'])}")
      return len(seq) * int(match["num"])

   def PressCodes(self, codes, robotcount: int) -> int:
      """
      human = ArrowPad(None)
      robot3 = ArrowPad(human)
      robot2 = ArrowPad(robot3)
      doorrobot = NumPad(0, robot2)

      humanx = ArrowPad(None)
      robot3x = ArrowPad(human)
      robot2x = ArrowPad(robot3)
      doorrobotx = NumPad(1, robot2)
      """

      r0 = ArrowPad(None)
      for _ in range(robotcount):
         r0 = ArrowPad(r0)
      doorrobot0 = NumPad(0, r0)

      r1 = ArrowPad(None)
      for _ in range(robotcount):
         r1 = ArrowPad(r1)
      doorrobot1 = NumPad(1, r1)

      result = 0
      for code in codes:
         print(code)
         seq0 = ""
         seq1 = ""

         #print(f"Doorrobot: {doorrobot.pos}  Robot2: {robot2.pos}  Robot3: {robot3.pos}")

         for c in code:
            seq0 += doorrobot0.need(c)
            seq1 += doorrobot1.need(c)

         if len(seq0) < len(seq1):
            print(len(seq0))
            result += self.CalcComplexity(code, seq0)
         else:
            print(len(seq1))
            result += self.CalcComplexity(code, seq1)

      return result

   def PartA(self):
      self.StartPartA()

      codes = self.ParseInput()
      answer = self.PressCodes(codes, 2)

      # Attempt 1: 220674 is too high
      # Attempt 2: 211136 is too low
      # Attempt 3: 215374 is correct

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      codes = self.ParseInput()
      answer = self.PressCodes(codes, 15)

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day21Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

