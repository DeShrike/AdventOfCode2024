from aoc import Aoc
from utilities import neighbours4
import itertools
import math
import re
import sys

# Day 12
# https://adventofcode.com/2024

class Day12Solution(Aoc):

   def Run(self):
      self.StartDay(12, "Garden Groups")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(12)

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
      AAAA
      BBCD
      BBCC
      EEEC
      """
      testdata = \
      """
      OOOOO
      OXOXO
      OOOOO
      OXOXO
      OOOOO
      """
      testdata = \
      """
      RRRRIICCFF
      RRRRIICCCF
      VVRRRCCFFF
      VVRCCCJFFF
      VVVVCJJCFE
      VVIVCCJJEE
      VVIIICJJEE
      MIIIIIJJEE
      MIIISIJEEE
      MMMISSJEEE
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 1930

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return None

   def ParseInput(self):
      # rx = re.compile("^(?P<from>[A-Z0-9]{3}) = \((?P<left>[A-Z0-9]{3}), (?P<right>[A-Z0-9]{3})\)$")
      # match = rx.search(line)
      # pos = match["from"]

      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def Neighbours(self, x: int, y: int, grid):
      width = len(grid[0])
      height = len(grid)
      l = grid[y][x]
      for nx, ny in neighbours4(x, y, (width, height)):
         if grid[ny][nx] == l:
            yield (nx, ny)

   def FloodFill(self, xx: int, yy: int, grid, done, id: int):
      width = len(grid[0])
      height = len(grid)
      s = [(xx, yy)]
      l = grid[yy][xx]
      done[yy][xx] = id
      size = 1
      perimeter = 0
      while len(s) > 0:
         x, y = s.pop()
         nn = 0
         for nx, ny in self.Neighbours(x, y, grid):
            if done[ny][nx] == 0:
               done[ny][nx] = id
               s.append((nx, ny))
               size += 1
            nn += 1
         perimeter += 4 - nn
      return (size, perimeter)

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      answer = 0
      width = len(data[0])
      height = len(data)
      done = [[0 for col in row] for row in data]
      for y in range(height):
         for x in range(width):
            if done[y][x] > 0:
               continue
            #print(data[y][x], end="")
            count = 1
            area, perimeter = self.FloodFill(x, y, data, done, count)
            #print(f" = {area} * {perimeter}")
            answer += area * perimeter
      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day12Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

