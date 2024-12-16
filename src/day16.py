from aoc import Aoc
from utilities import neighbours4
import itertools
import math
import re
import sys

# Day 16
# https://adventofcode.com/2024

class Day16Solution(Aoc):

   def Run(self):
      self.StartDay(16, "Reindeer Maze")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(16)

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
      ###########
      #...#...#E#
      #.#.#.#.#.#
      #.#.#.#.#.#
      #S#.......#
      ###########
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 11048

      testdata = \
      """
      #################
      #...#...#...#..E#
      #.#.#.#.#.#.#.#.#
      #.#.#.#...#...#.#
      #.#.#.#.###.#.#.#
      #...#.#.#.....#.#
      #.#.#.#.#.#####.#
      #.#...#.#.#.....#
      #.#.#####.#.###.#
      #.#.#.......#...#
      #.#.###.#####.###
      #.#.#...#.....#.#
      #.#.#.#####.###.#
      #.#.#.........#.#
      #.#.#.#########.#
      #S#.............#
      #################
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 11048



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
      data = []
      for line in self.inputdata:
         data.append(list(line))

      sx = sy = ex = ey = None
      for y, row in enumerate(data):
         for x, col in enumerate(row):
            if col == "S":
               sx, sy = x, y
            elif col == "E":
               ex, ey = x, y

      direction = 0

      # E S W N
      self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
      return (data, (sx, sy), (ex, ey), direction)

   def CalcCost(self, path, direction: int) -> int:
      cost = 0
      p = path[0]
      for i in range(1, len(path)):
         pp = path[i]
         dx = pp[0] - p[0]
         dy = pp[1] - p[1]
         if abs(dx) > 1 or abs(dy) > 1:
            #print(p, pp)
            #a = input()
            #continue
            return 1_000_000
         #print(p, pp)
         #a = input()
         if self.directions[direction][0] != dx or \
            self.directions[direction][1] != dy:
            direction = self.directions.index((dx, dy))
            cost += 1000
         cost += 1
         p = pp
      return cost

   def CountWays(self, grid, x: int, y: int) -> int:
      count = 0
      size = (len(grid[0]), len(grid))
      for nx, ny in neighbours4(x, y, size):
         if grid[ny][nx] in "E.":
            count += 1
      return count

   def CountWays2(self, grid, x: int, y: int, p) -> int:
      count = 0
      size = (len(grid[0]), len(grid))
      for nx, ny in neighbours4(x, y, size):
         if grid[ny][nx] in "E.":
            if (nx, ny) not in p:
               count += 1
      return count

   def PrintGrid(self, grid, path):
      for y, row in enumerate(grid):
         for x, col in enumerate(row):
            if col == "#":
               print("#", end="")
            elif col in "SE.":
               if (x, y) in path:
                  if path[-1] == (x, y):
                     print("O", end="")
                  else:
                     print("o", end="")
               else:
                  print(".", end="")
         print("")

   def Step(self, grid, path, end, paths) -> None:
      size = (len(grid[0]), len(grid))
      pos = path[-1]
      print(path)
      self.PrintGrid(grid, path)
      #print("Path", path)
      print(pos)
      a = input()
      for nx, ny in neighbours4(*pos, size):
         if grid[ny][nx] == "#":
            continue
         if (nx, ny) in path:
            continue
         dx = nx - pos[0]
         dy = ny - pos[1]
         xx, yy = pos
         while True:
            xx += dx
            yy += dy
            if grid[yy][xx] == "E":
               path.append((xx, yy))
               paths.append(path[:])
               print(path)
               self.PrintGrid(grid, path)
               print("Found")
               c = input()
               print("Returning F")
               return
            else:
               if grid[yy][xx] == ".":
                  path.append((xx, yy))
                  cw = self.CountWays2(grid, xx, yy, path)
                  if cw >= 2:
                     print("A")
                     self.Step(grid, path[:], end, paths)
                     break
               elif grid[yy][xx] == "#":
                  cw = self.CountWays2(grid, *path[-1], path)
                  print(f"CW= {cw}")
                  if cw == 0:
                     print("CW***")
                     return
                  print("B")
                  self.Step(grid, path[:], end, paths)
                  break
               #else:
               #   path.append((xx,yy))
               #   print("C")
               #   self.Step(grid, path[:], end, paths)
               #   break
      print("Returning")

   def PartA(self):
      self.StartPartA()

      grid, start, end, direction = self.ParseInput()

      s = [start]
      paths = []
      self.Step(grid, s, end, paths)
      
      for p in paths:
         print(p)
         self.PrintGrid(grid, p)
         if p[-1] == end:
            cost = self.CalcCost(p, direction)
            print(f"Cost: {cost}")
            a = input()
      answer = min([self.CalcCost(p, direction) for p in paths])

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day16Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

