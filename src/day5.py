from aoc import Aoc
import itertools
import math
import re
import sys

# Day 5
# https://adventofcode.com/2024

class Day5Solution(Aoc):

   def Run(self):
      self.StartDay(5, "Print Queue")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(5)

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
      47|53
      97|13
      97|61
      97|47
      75|29
      61|13
      75|53
      29|13
      97|29
      53|29
      61|53
      97|53
      61|29
      47|13
      75|47
      97|75
      47|61
      75|61
      47|29
      75|13
      53|13

      75,47,61,53,29
      97,61,53,29,13
      75,29,13
      75,97,47,61,53
      61,13,29
      97,13,75,29,47
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 143

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 123

   def ParseInput(self):
      rules = []
      updates = []
      for line in self.inputdata:
         parts = line.split("|")
         if line == "":
            continue
         if len(parts) == 2:
            rules.append(parts)
         else:
            parts = line.split(",")
            updates.append(parts)

      return rules, updates

   def PartA(self):
      self.StartPartA()

      rules, updates = self.ParseInput()
      answer = 0
      for update in updates:
         ok = True
         for rule in rules:
            r1 = rule[0]
            r2 = rule[1]
            if r1 in update and r2 in update:
               if update.index(r1) > update.index(r2):
                  ok = False
            else:
               continue
         if ok:
            answer += int(update[(len(update) - 1) // 2])

      self.ShowAnswer(answer)

   def FixUpdate(self, update, rules):
      fixed = update[:]
      swapped = True
      while swapped:
         swapped = False
         for rule in rules:
            r1 = rule[0]
            r2 = rule[1]
            if r1 not in fixed or r2 not in fixed:
               continue
            ix1 = fixed.index(r1)
            ix2 = fixed.index(r2)
            if ix1 > ix2:
               fixed[ix1], fixed[ix2] = fixed[ix2], fixed[ix1]
               swapped = True

      return fixed

   def PartB(self):
      self.StartPartB()

      rules, updates = self.ParseInput()
      answer = 0
      for update in updates:
         ok = True
         for rule in rules:
            r1 = rule[0]
            r2 = rule[1]
            if r1 in update and r2 in update:
               if update.index(r1) > update.index(r2):
                  ok = False
            else:
               continue
         if not ok:
            fixed = self.FixUpdate(update, rules)
            answer += int(fixed[(len(fixed) - 1) // 2])

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day5Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

