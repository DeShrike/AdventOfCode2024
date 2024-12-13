from aoc import Aoc
from utilities import neighbours4, neighbours8, isingrid
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
      #self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(12)

      #goal = self.TestDataA()
      #self.PartA()
      #self.Assert(self.GetAnswerA(), goal)

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
      EEEEE
      EXXXX
      EEEEE
      EXXXX
      EEEEE
      """
      testdata = \
      """
      AAAAAA
      AAABBA
      AAABBA
      ABBAAA
      ABBAAA
      AAAAAA
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
      testdata = \
      """
      AAAAAA
      AAABBA
      AAABBA
      ABBAAA
      ABBAAA
      AAAAAA
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 368

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

   def IsGoodH(self, x1: int, y1: int, x2: int, y2: int, grid, id: int) -> bool:
      #print(f" IsGood {x1} {y1} id:{id}")
      w = len(grid[0])
      h = len(grid)
      c1 = None if not isingrid(x1, y1 - 1, w, h) else grid[y1 - 1][x1]
      c2 = None if not isingrid(x1, y1, w, h) else grid[y1][x1]
      #print(f" ->  {c1} {c2}")
      if (c1 is None or c2 is None) and (c1 == id or c2 == id):
         return True
      return (c1 != id or c2 != id) and (c1 == id or c2 == id)

   def IsGoodV(self, x1: int, y1: int, x2: int, y2: int, grid, id: int) -> bool:
      #print(f" IsGood {x1} {y1} id:{id}")
      w = len(grid[0])
      h = len(grid)
      c1 = None if not isingrid(x1 - 1, y1, w, h) else grid[y1][x1 - 1]
      c2 = None if not isingrid(x1, y1, w, h) else grid[y1][x1]
      #print(f" ->  {c1} {c2}")
      if (c1 is None or c2 is None) and (c1 == id or c2 == id):
         return True
      return (c1 != id or c2 != id) and (c1 == id or c2 == id)

   def IsDia(self, xx: int, yy: int, grid, id: int) -> bool:
      # ac
      # bd
      w = len(grid[0])
      h = len(grid)
      a = None if not isingrid(yy - 1, xx - 1, w, h) else grid[yy - 1][xx - 1]
      b = None if not isingrid(yy, xx - 1, w, h) else grid[yy][xx - 1]
      c = None if not isingrid(yy - 1, xx, w, h) else grid[yy - 1][xx]
      d = None if not isingrid(yy, xx, w, h) else grid[yy][xx]
      
      if a == d and a != b and a != c:
         return True
      if c == b and c != a and c != d:
         return True
      
      return False

   def CalcSides(self, xx: int, yy: int, id: int, grid) -> int:
      vertexes = []
      width = len(grid[0])
      height = len(grid)
      for y in range(height + 1):
         for x in range(width + 1):
            vertexes.append((x, y))
            """
            count = 0
            for nx, ny in neighbours8(x, y, (width, height)):
               if grid[ny][nx] == id:
                  count += 1
            #print(f" {x} {y} -> {count}")
            #aa = input()
            if 0 < count < 4:
               if (x, y) not in vertexes:
                  vertexes.append((x, y))
            """
      
      
      #print("---Vertexes------")
      #print(vertexes)
      s1 = vertexes[:]
      s1.sort(key=lambda i: i[1] * 1000 + i[0])
      #print("Sorted 1:")
      #print(s1)
      lines = []
      line = []
      while len(s1) > 0:
         v = s1.pop(0)
         if len(line) == 0:
            line.append(v)
            lines.append(line)
            continue
         if v[1] == line[-1][1] and v[0] == line[-1][0] + 1:
            if self.IsGoodH(line[-1][0], line[-1][1], v[0], v[1], grid, id):
               if self.IsDia(line[-1][0], line[-1][1], grid, id):
                  line = [v]
                  lines.append(line)
               else:
                  #print("Yes")
                  line.append(v)
            else:
               #print("No")
               line = [v]
               lines.append(line)
         else:
            line   = [v]
            lines.append(line)


      s2 = vertexes[:]
      s2.sort(key=lambda i: i[0] * 1000 + i[1])
      #print("Sorted 2:")
      #print(s2)
      line = []
      while len(s2) > 0:
         v = s2.pop(0)
         if len(line) == 0:
            line.append(v)
            lines.append(line)
            continue
         if v[0] == line[-1][0] and v[1] == line[-1][1] + 1:
            if self.IsGoodV(line[-1][0], line[-1][1], v[0], v[1], grid, id):
               if self.IsDia(line[-1][0], line[-1][1], grid, id):
                  line = [v]
                  lines.append(line)
               else:
                  #print("Yes")
                  line.append(v)
            else:
               #print("No")
               line = [v]
               lines.append(line)
         else:
            line = [v]
            lines.append(line)

      #for l in lines:
      #   print(f"   {l}")
      #print(len(lines))
      #a = input()
      return len([line for line in lines if len(line) > 1])

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
      count = 0
      for y in range(height):
         for x in range(width):
            if done[y][x] > 0:
               continue
            print(data[y][x], end="")
            count += 1
            area, perimeter, sides = self.FloodFill(x, y, data, done, count)
            print(f" = {area} * {sides}")
            if sides == 2:
               sides = 4
            answer += area * sides

      # Attempt 1: 893904 is too low
      # Attempt 2: 892370 (not submitted)

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day12Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

