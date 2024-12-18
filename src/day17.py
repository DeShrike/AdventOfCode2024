from aoc import Aoc
import itertools
import math
import re
import sys

# Day 17
# https://adventofcode.com/2024

class Day17Solution(Aoc):

   def Run(self):
      self.StartDay(17, "Chronospatial Computer")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(17)

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
      Register A: 729
      Register B: 0
      Register C: 0

      Program: 0,1,5,4,3,0
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return "4,6,3,5,6,3,5,2,1,0"

   def TestDataB(self):
      self.inputdata.clear()
      testdata = \
      """
      Register A: 2024
      Register B: 0
      Register C: 0

      Program: 0,3,5,4,3,0
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 117440

   def ParseInput(self):
      # rx = re.compile("^(?P<from>[A-Z0-9]{3}) = \((?P<left>[A-Z0-9]{3}), (?P<right>[A-Z0-9]{3})\)$")
      # match = rx.search(line)
      # pos = match["from"]

      a = b = c = None
      prog = None
      raw = None
      for line in self.inputdata:
         if line[:12] == "Register A: ":
            a = int(line[12:])
         elif line[:12] == "Register B: ":
            b = int(line[12:])
         elif line[:12] == "Register C: ":
            c = int(line[12:])
         elif line[:9] == "Program: ":
            raw = line[9:]
            prog = [int(i) for i in raw.split(",")]

      return a, b, c, prog, raw

   def Execute(self, prog, aa) -> str:
      opcodes = ["adv", "bxl", "bst", "jnz", "bxc", "out", "bdv", "cdv"]
      answer = ""
      ip = 0
      a = aa
      b = c = 0
      result = ""
      while True:
         if ip >= len(prog):
            break
         opcode = opcodes[prog[ip]]
         operand = literal = prog[ip + 1]
         if operand == 4:
            operand = a
         elif operand == 5:
            operand = b
         elif operand == 6:
            operand = c

         #print(f"IP: {ip} {opcode} Literal: {literal} Operand: {operand}")
         #print(f"A: {a}  B: {b}   C: {c}")
         if opcode == opcodes[0]:
            a = a // (2 ** operand)
            ip += 2
         elif opcode == opcodes[1]:
            b = b ^ literal
            ip += 2
         elif opcode == opcodes[2]:
            b = (operand % 8) & 0x07
            ip += 2
         elif opcode == opcodes[3]:
            if a != 0:
               ip = literal
            else:
               ip += 2
         elif opcode == opcodes[4]:
            b = b ^ c
            ip += 2
         elif opcode == opcodes[5]:
            if result != "":
               result += ","
            result += str(operand % 8)
            ip += 2
         elif opcode == opcodes[6]:
            b = a // (2 ** operand)
            ip += 2
         elif opcode == opcodes[7]:
            c = a // (2 ** operand)
            ip += 2
      return result

   def ExecuteB(self, prog):
      opcodes = ["adv", "bxl", "bst", "jnz", "bxc", "out", "bdv", "cdv"]
      need = list(reversed(prog))
      needix = 0
      ip = len(prog) - 2
      a = b = c = 0
      while True:
         opcode = opcodes[prog[ip]]
         operand = literal = prog[ip + 1]


         if opcode == opcodes[0]:
            pass
            a = a // (2 ** operand)
            ip += 2
         elif opcode == opcodes[1]:
            pass
            b = b ^ literal
            ip += 2
         elif opcode == opcodes[2]:
            pass
            b = (operand % 8) & 0x07
            ip += 2
         elif opcode == opcodes[3]:
            if a == 0:
               ip = len(prog) - 2 - literal
            else:
               ip -= 2
         elif opcode == opcodes[4]:
            pass
            b = b ^ c
            ip += 2
         elif opcode == opcodes[5]:
            if result != "":
               result += ","
               
            result += str(operand % 8)
            ip += 2
         elif opcode == opcodes[6]:
            pass
            b = a // (2 ** operand)
            ip += 2
         elif opcode == opcodes[7]:
            pass
            c = a // (2 ** operand)
            ip += 2
         
      pass

   def PartA(self):
      self.StartPartA()

      a, b, c, prog, raw = self.ParseInput()
      answer = self.Execute(prog, a)

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      opcodes = ["adv", "bxl", "bst", "jnz", "bxc", "out", "bdv", "cdv"]
      a, b, c, prog, raw = self.ParseInput()
      aa = 0
      print(prog)
      print(raw)
      while True:
         aa += 5
         print(f"{aa}", end="\r")
         result = self.Execute(prog, aa)
         if result == raw:
            answer = aa
            break
         #if aa % 1000000000 == 0:
         #   print(result)
         print(f"{aa} -> {result}")
         #aaa = input()
         break
      answer = None
      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day17Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

