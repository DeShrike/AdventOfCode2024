from aoc import Aoc
import itertools
import math
import re
import sys

# Day 24
# https://adventofcode.com/2024

class Day24Solution(Aoc):

   def Run(self):
      self.StartDay(24, "Crossed Wires")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(24)

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
      x00: 1
      x01: 0
      x02: 1
      x03: 1
      x04: 0
      y00: 1
      y01: 1
      y02: 1
      y03: 1
      y04: 1

      ntg XOR fgs -> mjb
      y02 OR x01 -> tnw
      kwq OR kpj -> z05
      x00 OR x03 -> fst
      tgd XOR rvg -> z01
      vdt OR tnw -> bfw
      bfw AND frj -> z10
      ffh OR nrd -> bqk
      y00 AND y03 -> djm
      y03 OR y00 -> psh
      bqk OR frj -> z08
      tnw OR fst -> frj
      gnj AND tgd -> z11
      bfw XOR mjb -> z00
      x03 OR x00 -> vdt
      gnj AND wpb -> z02
      x04 AND y00 -> kjc
      djm OR pbm -> qhw
      nrd AND vdt -> hwm
      kjc AND fst -> rvg
      y04 OR y02 -> fgs
      y01 AND x02 -> pbm
      ntg OR kjc -> kwq
      psh XOR fgs -> tgd
      qhw XOR tgd -> z09
      pbm OR djm -> kpj
      x03 XOR y03 -> ffh
      x00 XOR y04 -> ntg
      bfw OR bqk -> z06
      nrd XOR fgs -> wpb
      frj XOR qhw -> z04
      bqk OR frj -> z07
      y03 OR x01 -> nrd
      hwm AND bqk -> z03
      tgd XOR rvg -> z12
      tnw OR pbm -> gnj
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 2024

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
      rxand = re.compile("^(?P<i1>[a-z0-9]{3}) AND (?P<i2>[a-z0-9]{3}) -> (?P<out>[a-z0-9]{3})$")
      rxor = re.compile("^(?P<i1>[a-z0-9]{3}) OR (?P<i2>[a-z0-9]{3}) -> (?P<out>[a-z0-9]{3})$")
      rxxor = re.compile("^(?P<i1>[a-z0-9]{3}) XOR (?P<i2>[a-z0-9]{3}) -> (?P<out>[a-z0-9]{3})$")
      # match = rx.search(line)
      # pos = match["from"]

      gates = {}
      operations = []
      for line in self.inputdata:
         if ":" in line:
            parts = line.split(":")
            gates[parts[0][0:3]] = bool(int(parts[1]))
         elif "->" in line:
            match = rxand.search(line)
            if match:
               i1 = match["i1"]
               i2 = match["i2"]
               out = match["out"]
               operations.append((i1, "AND", i2, out))
               if i1 not in gates:
                  gates[i1] = None
               if i2 not in gates:
                  gates[i2] = None
               if out not in gates:
                  gates[out] = None
               continue
            match = rxor.search(line)
            if match:
               i1 = match["i1"]
               i2 = match["i2"]
               out = match["out"]
               operations.append((i1, "OR", i2, out))
               if i1 not in gates:
                  gates[i1] = None
               if i2 not in gates:
                  gates[i2] = None
               if out not in gates:
                  gates[out] = None
               continue
            match = rxxor.search(line)
            if match:
               i1 = match["i1"]
               i2 = match["i2"]
               out = match["out"]
               operations.append((i1, "XOR", i2, out))
               if i1 not in gates:
                  gates[i1] = None
               if i2 not in gates:
                  gates[i2] = None
               if out not in gates:
                  gates[out] = None
               continue

      return gates, operations

   def PartA(self):
      self.StartPartA()

      gates, operations = self.ParseInput()
      answer = None
      print(gates)
      print(operations)
      
      done = False
      while not done:
         done = True
         for i1, op, i2, out in operations:
            if gates[out] is None:
               done = False
               if gates[i1] is not None and gates[i2] is not None:
                  if op == "AND":
                     gates[out] = gates[i1] and gates[i2]
                  elif op == "OR":
                     gates[out] = gates[i1] or gates[i2]
                  elif op == "XOR":
                     gates[out] = gates[i1] ^ gates[i2]

      i = 0
      result = ""
      while True:
         gate = f"z{i:02}"
         if gate not in gates:
            break
         result = ("1" if gates[gate] else "0") + result
         i += 1
      print(result)
      answer = int(result, 2)

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day24Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

