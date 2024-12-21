from aoc import Aoc
from dijkstra import BuildGraph, Dijkstra, BackPedal
from canvas import Canvas
from utilities import mapf
import itertools
import math
import re
import sys

# Day 20
# https://adventofcode.com/2024

class Day20Solution(Aoc):

   def Run(self):
      self.StartDay(20, "Race Condition")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(20)

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
      ###############
      #...#...#.....#
      #.#.#.#.#.###.#
      #S#...#.#.#...#
      #######.#.#.###
      #######.#.#...#
      #######.#.###.#
      ###..E#...#...#
      ###.#######.###
      #...###...#...#
      #.#####.#.###.#
      #.#...#.#.#...#
      #.#.#.#.#.#.###
      #...#...#...###
      ###############
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 84

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return None

   def ParseInput(self):
      data = []
      start = None
      end = None
      for y, line in enumerate(self.inputdata):
         row = []
         for x, col in enumerate(line):
            if col == ".":
               row.append(0)
            elif col == "#":
               row.append(9999)
            elif col == "S":
               row.append(0)
               start = (x, y)
            elif col == "E":
               end = (x, y)
               row.append(0)

         data.append(row)

      return data, start, end

   def PrintGrid(self, grid, path):
      for y, line in enumerate(grid):
         for x, col in enumerate(line):
            if col > 1:
               print("#", end="")
            elif (x, y) in path:
               print("o", end="")
            else:
               print(".", end="")
         print("")

   def CreatePNGA(self, grid, path, start, end, cheat) -> None:
      width = len(grid[0])
      height = len(grid)
      boxsize = 4
      canvas = Canvas(width * boxsize, height * boxsize)
      for y in range(height):
         for x in range(width):
            c = grid[y][x]
            if c == 9999:
               color = (0x18, 0x18, 0x18)
            else:
               color = (0x00, 0x00, 0x00)

            canvas.set_big_pixel(x * boxsize, y * boxsize, color, boxsize)

      for ix, xy in enumerate(path):
         c = mapf(ix, 0, len(path), 50, 255)
         color = (int(c), 0, 0)
         canvas.set_big_pixel(xy[0] * boxsize, xy[1] * boxsize, color, boxsize)

      canvas.set_big_pixel(start[0] * boxsize, start[1] * boxsize, (0x00, 0xFF, 0x00), boxsize)
      canvas.set_big_pixel(end[0] * boxsize, end[1] * boxsize, (0x00, 0xFF, 0x00), boxsize)
      if cheat is not None:
         canvas.set_big_pixel(cheat[0] * boxsize, cheat[1] * boxsize, (0xFF, 0xFF, 0x00), boxsize)

      if cheat is None:
         pngname = "day20a.png"
      else:
         pngname = f"day20a_{cheat[0]}_{cheat[1]}.png"
      print(f"Saving {pngname}")
      canvas.save_PNG(pngname)

   def TryRace(self, grid, start, end, cheatspot) -> int:
      width = len(grid[0])
      height = len(grid)

      if cheatspot is not None:
         grid[cheatspot[1]][cheatspot[0]] = 0

      #print("Building Graph")
      graph, costs, parents = BuildGraph(grid)
      costs[start] = 0

      #print("Searching")
      result = Dijkstra(start, end, graph, costs, parents)
      #print("BackPedaling")
      path = BackPedal(start, end, result)

      #self.PrintGrid(grid, path)

      if cheatspot is not None:
         grid[cheatspot[1]][cheatspot[0]] = 9999

      cheats = 0
      for p in path:
         if grid[p[1]][p[0]] > 1:
            cheats += 1

      return path, cheats

   def PartA(self):
      self.StartPartA()

      grid, start, end = self.ParseInput()
      answer = 0

      path, cheats = self.TryRace(grid, start, end, None)
      normal_length = len(path)
      print(f"Normal length: {normal_length}")

      self.CreatePNGA(grid, path, start, end, None)

      width = len(grid[0])
      height = len(grid)
      print(f"Size: {width}x{height}")

      for i in range(len(path)):
         cx, cy = path[i]
         n1x, n1y = cx - 2, cy
         n2x, n2y = cx + 2, cy
         n3x, n3y = cx, cy - 2
         n4x, n4y = cx, cy + 2
         nn = [(n1x, n1y), (n2x, n2y), (n3x, n3y), (n4x, n4y)]
         for j in range(i + 101, len(path)):
            if path[j] in nn:
               answer += 1 

      """
      for y in range(1, height - 1):
         for x in range(1, width - 1):
            if grid[y][x] == 9999:
               print(f"{x},{y}")

               path, cheats = self.TryRace(grid, start, end, (x, y))
               length = len(path)
               print(f"-> length {length} has {cheats} cheats -> {normal_length - length} steps shorter")
               if cheats == 1 and length + 100 < normal_length:
                  self.CreatePNGA(grid, path, start, end, (x, y))
                  answer += 1
      """
      # Attempt 1: 970 is too low
      # Attempt 2: 1365 is too high
      # Attempt 3: 1355 is correct

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      grid, start, end = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day20Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

