from aoc import Aoc
import itertools
import math
import re
import sys

# Day 9
# https://adventofcode.com/2024

class File():
   def __init__(self, size: int, fileid: int):
      self.id = fileid
      self.size = size

   def __repr__(self):
      return f"File({self.size}, {self.id})"


class Space():
   def __init__(self):
      self.free = 0
      self.files = []

   def __str__(self):
      if self.free > 0:
         return f"{self.free} free"
      else:
         s = ""
         for f in self.files:
            s += str(f)
         return s


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
      self.TestDataA()
      return 2858

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

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      diskmap = list(data[0])
      disk = []
      fid = 0
      while len(diskmap) > 0:
         l = int(diskmap.pop(0))
         if len(diskmap) > 0:
            freel = int(diskmap.pop(0))
         else:
            freel = 0
         f = File(l, fid)
         s = Space()
         s.files.append(f)
         disk.append(s)
         fid += 1
         if freel > 0:
            s = Space()
            s.free = freel
            disk.append(s)

      i = len(disk) - 1
      while i > 0:
         current = disk[i]
         if len(current.files) == 0:
            i -= 1
            current = disk[i]
         # find free space with at least current.files[0].size size
         j = 0
         fi = current.files[0]
         while j < i:
            if disk[j].free >= fi.size:
               disk[j].files.append(fi)
               disk[j].free -= fi.size
               current.free = fi.size
               current.files.clear()
               break
            j += 1
         i -= 1

      answer = 0
      pos = 0
      i = 0
      for space in disk:
         for fi in space.files:
            while fi.size > 0:
               answer += pos * fi.id
               fi.size -= 1
               pos += 1
         pos += space.free

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day9Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

