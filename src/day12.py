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
      OOOOO
      OXOXO
      OOOOO
      OXOXO
      OOOOO
      """
      testdata = \
      """
      AAAA
      BBCD
      BBCC
      EEEC
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
      return 1206

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

   def CalcSides(self, xx: int, yy: int, id: int, grid) -> int:
      vertexes = []
      width = len(grid[0])
      height = len(grid)
      for y in range(height):
         for x in range(width):
            #if grid[y][x] != id:
            #   continue
            count = 0
            for nx, ny in neighbours4(x, y, (width, height)):
               if grid[ny][nx] == id:
                  count += 1
            if 0 < count < 4:
               if (x, y) not in vertexes:
                  vertexes.append((x, y))
      print("-----------")
      print(vertexes)
      s1 = vertexes[:]
      s1.sort(key=lambda i: i[1] * 1000 + i[0])
      print("")
      print(s1)
      lines = []
      line = []
      while len(s1) > 0:
         v = s1.pop(0)
         if len(line) == 0:
            line.append(v)
            lines.append(line)
            continue
         if v[1] == line[-1][1] and v[0] == line[-1][0] + 1:
            line.append(v)
         else:
            line = [v]
            lines.append(line)



      s2 = vertexes[:]
      s2.sort(key=lambda i: i[0] * 1000 + i[1])
      print("")
      print(s2)
      line = []
      while len(s2) > 0:
         v = s2.pop(0)
         if len(line) == 0:
            line.append(v)
            lines.append(line)
            continue
         if v[0] == line[-1][0] and v[1] == line[-1][1] + 1:
            line.append(v)
         else:
            line = [v]
            lines.append(line)


      for l in lines:
         print(f"   {l}")
      print(len(lines))
      a = input()
      return len(lines)

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

      sides = self.CalcSides(xx, yy, id, done)

      return (size, perimeter, sides)

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
            area, perimeter, sides = self.FloodFill(x, y, data, done, count)
            #print(f" = {area} * {perimeter}")
            answer += area * perimeter

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = 0
      width = len(data[0])
      height = len(data)
      done = [[0 for col in row] for row in data]
      for y in range(height):
         for x in range(width):
            if done[y][x] > 0:
               continue
            print(data[y][x], end="")
            count = 1
            area, perimeter, sides = self.FloodFill(x, y, data, done, count)
            print(f" = {area} * {sides}")
            answer += area * sides

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day12Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

