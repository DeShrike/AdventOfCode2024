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
      testdata = \
      """
      x00: 0
      x01: 1
      x02: 0
      x03: 1
      x04: 0
      x05: 1
      y00: 0
      y01: 0
      y02: 1
      y03: 1
      y04: 0
      y05: 1

      x00 AND y00 -> z05
      x01 AND y01 -> z02
      x02 AND y02 -> z01
      x03 AND y03 -> z03
      x04 AND y04 -> z04
      x05 AND y05 -> z00
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return "z00,z01,z02,z05"

   def ParseInput(self):
      rxand = re.compile("^(?P<i1>[a-z0-9]{3}) AND (?P<i2>[a-z0-9]{3}) -> (?P<out>[a-z0-9]{3})$")
      rxor = re.compile("^(?P<i1>[a-z0-9]{3}) OR (?P<i2>[a-z0-9]{3}) -> (?P<out>[a-z0-9]{3})$")
      rxxor = re.compile("^(?P<i1>[a-z0-9]{3}) XOR (?P<i2>[a-z0-9]{3}) -> (?P<out>[a-z0-9]{3})$")

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

   def GetNumber(self, gates, startletter: str) -> int:
      i = 0
      result = ""
      while True:
         gate = f"{startletter}{i:02}"
         if gate not in gates:
            break
         result = ("1" if gates[gate] else "0") + result
         i += 1
      #print(startletter, result, int(result, 2))
      return int(result, 2)

   def Go(self, gates, operations) -> None:
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

   def SwapOperations(self, operations, ix1: int, ix2: int) -> None:
      pass

   def PartA(self):
      self.StartPartA()

      gates, operations = self.ParseInput()
      self.Go(gates, operations)

      answer = self.GetNumber(gates, "z")

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      gates, operations = self.ParseInput()
      print(f"Gates: {len(gates)}")
      print(f"Operations: {len(operations)}")
      answer = None

      """
      for a1 in range(len(operations)):
         print(a1, len(operations))
         for a2 in range(len(operations)):
            if a1 == a2:
               continue
            print("->", a2, len(operations))
            for a3 in range(len(operations)):
               if a1 == a3 or a2 == a3:
                  continue
               print("-->", a3, len(operations))
               for a4 in range(len(operations)):
                  if a3 == a4:
                     continue
                  if a1 == a4 or a2 == a4:
                     continue
                  opers = [list(o) for o in operations]
                  self.SwapOperations(opers, a1, a2)
                  self.SwapOperations(opers, a3, a4)
                  # todo : reset registers
                  self.Go(gates, opers)

                  x = self.GetNumber(gates, "x")
                  y = self.GetNumber(gates, "y")
                  z = self.GetNumber(gates, "z")
                  if x + y == z:
                     print("Found it !!!")
      print(x + y)
      """

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day24Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

