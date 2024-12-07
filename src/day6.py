from aoc import Aoc
import itertools
import math
import re
import sys
from utilities import isingrid, mapf
from canvas import Canvas

# Day 6
# https://adventofcode.com/2024

class Day6Solution(Aoc):

   def Run(self):
      self.StartDay(6, "Guard Gallivant")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(6)

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
      ....#.....
      .........#
      ..........
      ..#.......
      .......#..
      ..........
      .#..^.....
      ........#.
      #.........
      ......#...
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 41

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 6

   def ParseInput(self):
      grid = []
      for line in self.inputdata:
         grid.append(list(line))

      return grid

   def Step(self, grid, x: int, y: int, direction: int) -> (int, int, int):
      grid[y][x] = "X"
      width = len(grid[0])
      height = len(grid)
      nx = x + self.directions[direction][0]
      ny = y + self.directions[direction][1]
      if isingrid(nx, ny, width, height) and grid[ny][nx] in "#O":
         direction = (direction + 1) % len(self.directions)
      else:
         x = nx
         y = ny
      return (x, y, direction)

   def CreatePNGA(self, grid, path, sx: int, sy: int) -> None:
      width = len(grid[0])
      height = len(grid)
      boxsize = 2
      canvas = Canvas(width * boxsize, height * boxsize)
      for y in range(height):
         for x in range(width):
            c = grid[y][x]
            if c == ".":
               color = (0x18, 0x18, 0x18)
            elif c == "^":
               color = (0x00, 0xFF, 0x00)
            elif c == "#":
               color = (0xFF, 0xFF, 0xFF)
            elif c == "X":
               color = (0xFF, 0x00, 0x00)
            canvas.set_big_pixel(x * boxsize, y * boxsize, color, boxsize)

      for ix, xy in enumerate(path):
         c = mapf(ix, 0, len(path), 50, 255)
         color = (int(c), 0, 0)
         canvas.set_big_pixel(xy[0] * boxsize, xy[1] * boxsize, color, boxsize)

      canvas.set_big_pixel(sx * boxsize, sy * boxsize, (0x00, 0xFF, 0x00), boxsize)

      pngname = "day6a.png"
      print(f"Saving {pngname}")
      canvas.save_PNG(pngname)

   def PartA(self):
      self.StartPartA()

      self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
      grid = self.ParseInput()
      width = len(grid[0])
      height = len(grid)
      x = 0
      y = 0
      for yy, row in enumerate(grid):
         for xx, col in enumerate(row):
            if col == "^":
               sx = x = xx
               sy = y = yy
               break
      direction = 0
      path = []
      while True:
         x, y, direction = self.Step(grid, x, y, direction)
         if not isingrid(x, y, width, height):
            break
         else:
            path.append((x, y))

      answer = sum(len([p for p in row if p == "X"]) for row in grid)
      self.CreatePNGA(grid, path, sx, sy)

      self.ShowAnswer(answer)

   def PrintGrid(self, grid) -> None:
      for row in grid:
         for col in row:
            print(f"{col}", end="")
         print("")

   def PartB(self):
      self.StartPartB()

      self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
      grid = self.ParseInput()
      width = len(grid[0])
      height = len(grid)
      print(f"Grid size: {width} x {height}")
      sx = 0
      sy = 0
      for yy, row in enumerate(grid):
         for xx, col in enumerate(row):
            if col == "^":
               sx = xx
               sy = yy
               break

      x = sx
      y = sy
      direction = 0
      while True:
         x, y, direction = self.Step(grid, x, y, direction)
         if not isingrid(x, y, width, height):
            break
      grid[sy][sx] = "^"
      placesused = sum(len([p for p in row if p == "X"]) for row in grid)

      answer = 0
      direction = 0
      for yy, row in enumerate(grid):
         for xx, col in enumerate(row):
            if col in "^#.":   
               continue
            newgrid = [row[:] for row in grid]
            newgrid[yy][xx] = "O"
            print(f"{xx} {yy}  ", end="\r")
            x = sx
            y = sy
            direction = 0
            count = 0
            while True:
               x, y, direction = self.Step(newgrid, x, y, direction)
               if not isingrid(x, y, width, height):
                  break
               count += 1
               if count > placesused * 2:
                  answer += 1
                  break

      # Brute force: 1655, 193.87 sec
      # Version 2:   1655, 73.66 sec
      # Version 3:   1655, 49.61 sec
      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day6Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

