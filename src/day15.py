from typing import Tuple
from aoc import Aoc
import itertools
import math
import re
import sys

# Day 15
# https://adventofcode.com/2024

class Day15Solution(Aoc):

   def Run(self):
      self.StartDay(15, "Warehouse Woes")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(15)

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
      ##########
      #..O..O.O#
      #......O.#
      #.OO..O.O#
      #..O@..O.#
      #O#..O...#
      #O..O..O.#
      #.OO.O.OO#
      #....O...#
      ##########

      <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
      vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
      ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
      <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
      ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
      ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
      >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
      <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
      ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
      v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 10092

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 9021

   def ParseInput(self):
      grid = []
      movements = ""
      for line in self.inputdata:
         if line == "":
            continue
         if line[0] == "#":
            grid.append(list(line))
         else:
            movements += line
      return grid, movements

   def MoveA(self, grid, rx: int, ry: int, dx: int, dy: int, width: int, height: int) -> Tuple[int, int]:
      x, y = rx, ry
      while True:
         x = x + dx
         y = y + dy
         if grid[y][x] == "#":
            return (rx, ry)
         elif grid[y][x] == ".":
            break
      while x != rx or y != ry:
         vx, vy = x, y
         x = x - dx
         y = y - dy
         grid[vy][vx] = grid[y][x]
         grid[y][x] = "."
      return (vx, vy)

   def MoveBlok(self, grid, x: int, y: int, dy: int) -> None:
      grid[y + dy][x + 0] = grid[y][x + 0]
      grid[y + dy][x + 1] = grid[y][x + 1]
      grid[y][x + 0] = "."
      grid[y][x + 1] = "."

   def TryMoveB(self, grid, x: int, y: int, dy: int) -> bool:
      b1 = grid[y][x]
      b2 = grid[y][x + 1]
      nb1 = grid[y + dy][x]
      nb2 = grid[y + dy][x + 1]

      if nb1 == "." and nb2 == ".":
         self.MoveBlok(grid, x, y, dy)
         return True
      if nb1 == "#" or nb2 == "#":
         return False
      if nb1 == "[":
         if self.TryMoveB(grid, x, y + dy, dy):
            self.MoveBlok(grid, x, y, dy)
            return True
      elif nb1 == "]":
         okl = False
         okr = False
         if grid[y + dy][x - 1] == "[":
            if self.TryMoveB(grid, x - 1, y + dy, dy):
               okl = True
         else:
            okl = True

         if grid[y + dy][x + 1] == "[":
            if self.TryMoveB(grid, x + 1, y + dy, dy):
               okr = True
         else:
            okr = True

         if okl and okr:
            self.MoveBlok(grid, x, y, dy)
            return True
      elif nb2 == "[":
         if self.TryMoveB(grid, x + 1, y + dy, dy):
            self.MoveBlok(grid, x, y, dy)
            return True
      return False

   def MoveB(self, grid, rx: int, ry: int, dx: int, dy: int, width: int, height: int) -> Tuple[int, int]:
      bx1 = rx
      by1 = ry + dy
      p1 = grid[by1][rx]
      if p1 == "#":
         return (rx, ry)
      if p1 == ".":
         grid[ry + dy][rx] = "@"
         grid[ry][rx] = "."
         return (rx, ry + dy)
      if p1 == "[":
         pass
      elif p1 == "]":
         bx1 -= 1

      backup = [row[:] for row in grid]
      if self.TryMoveB(grid, bx1, by1, dy):
         grid[ry + dy][rx] = "@"
         grid[ry][rx] = "."
         return (rx, ry + dy)
      else:
         grid.clear()
         for row in backup:
            grid.append(row)

      return (rx, ry)
      
   def PrintGrid(self, grid) -> None:
      for y, row in enumerate(grid):
         for x, col in enumerate(row):
            print(col, end="")
         print("")

   def PartA(self):
      self.StartPartA()

      rx = ry = None
      grid, movements = self.ParseInput()
      width = len(grid[0])
      height = len(grid)
      for y, row in enumerate(grid):
         for x, col in enumerate(row):
            if col == "@":
               rx, ry = x, y

      directions = { "^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0) }

      for m in movements:
         rx, ry = self.MoveA(grid, rx, ry, *directions[m], width, height)

      answer = 0
      for y, row in enumerate(grid):
         for x, col in enumerate(row):
            if col == "O":
               answer += 100 * y + x

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      rx = ry = None
      gridA, movements = self.ParseInput()
      grid = []
      for y, rowA in enumerate(gridA):
         row = []
         for x, col in enumerate(rowA):
            if col == "#":
               row.append("#")
               row.append("#")
            elif col == ".":
               row.append(".")
               row.append(".")
            elif col == "O":
               row.append("[")
               row.append("]")
            elif col == "@":
               row.append("@")
               row.append(".")
         grid.append(row)

      width = len(grid[0])
      height = len(grid)
      for y, row in enumerate(grid):
         for x, col in enumerate(row):
            if col == "@":
               rx, ry = x, y

      directions = { "^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0) }

      #self.PrintGrid(grid)

      for m in movements:
         if m in "<>":
            rx, ry = self.MoveA(grid, rx, ry, *directions[m], width, height)
         else:
            rx, ry = self.MoveB(grid, rx, ry, *directions[m], width, height)

      answer = 0
      for y, row in enumerate(grid):
         for x, col in enumerate(row):
            if col == "[":
               answer += 100 * y + x

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day15Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

