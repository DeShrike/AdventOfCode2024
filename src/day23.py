from aoc import Aoc
import itertools
import math
import re
import sys

# Day 23
# https://adventofcode.com/2024

class Day23Solution(Aoc):

   def Run(self):
      self.StartDay(23, "LAN Party")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(23)

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
      kh-tc
      qp-kh
      de-cg
      ka-co
      yn-aq
      qp-ub
      cg-tb
      vc-aq
      tb-ka
      wh-tc
      yn-cg
      kh-ub
      ta-co
      de-co
      tc-td
      tb-wq
      wh-td
      ta-ka
      td-qp
      aq-cg
      wq-ub
      ub-vc
      de-ta
      wq-aq
      wq-vc
      wh-yn
      ka-de
      kh-ta
      co-tc
      wh-qp
      tb-vc
      td-yn
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 7

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return "co,de,ka,ta"

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(tuple(line.split("-")))

      return data

   def PartA(self):
      self.StartPartA()

      connections = self.ParseInput()
      answer = 0
      groups = set()
      for ix1, con1 in enumerate(connections):
         a1, a2 = con1
         for ix2, con2 in enumerate(connections):
            if ix1 == ix2:
               continue
            b1, b2 = con2
            if a2 == b1:
               if (a1, b2) in connections or \
                  (b2, a1) in connections:
                  groups.add(tuple(sorted((a1, a2, b2))))
            elif a2 == b2:
               if (a1, b1) in connections or \
                  (b1, a1) in connections:
                  groups.add(tuple(sorted((a1, a2, b1))))
            elif b1 == a1:
               if (a2, b2) in connections or \
                  (b2, a2) in connections:
                  groups.add(tuple(sorted((a1, a2, b2))))
            elif b2 == a1:
               if (a2, b1) in connections or \
                  (b1, a2) in connections:
                  groups.add(tuple(sorted((a1, a2, b1))))

      for group in groups:
         if group[0][0] == "t" or group[1][0] == "t" or group[2][0] == "t":
            answer += 1

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      connections = self.ParseInput()
      answer = None

      groups = {}
      for con in connections:
         c1, c2 = con
         if c1 not in groups:
            groups[c1] = []
         groups[c1].append(c2)
         if c2 not in groups:
            groups[c2] = []
         groups[c2].append(c1)

      sets = [list(sorted([k, *v])) for k, v in groups.items()]

      for s in sorted(sets):
         print(s)

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day23Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

