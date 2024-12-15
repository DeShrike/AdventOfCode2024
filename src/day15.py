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
      #self.inputdata.clear()
      #self.TestDataA()
      #return 9021
      self.inputdata.clear()
      testdata = \
      """
      #######
      #...#.#
      #.....#
      #..OO@#
      #..O..#
      #.....#
      #######

      <vv<<^^<<^^
      """
      #<vv<<^^<<^^
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 0

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

   def TryMoveB(self, grid, x: int, y: int, dy: int, pp) -> bool:
      p1x = x
      p1y = y
      p2x = x + 1
      p2y = y
      b1 = grid[p1y][p1x]
      b2 = grid[p2y][p2x]
      print(f"TryMove {x},{y}")
      print(f" Box: {pp}  {grid[p1y][p1x - 1]} {b1}{b2} {grid[p1y][p2x + 1]}")
      if b1 == "." and b2 == ".":
         print(f"D ok  {pp}")
         print(f"  {grid[p1y][p1x]}{grid[p2y][p2x]}  <- {grid[p1y - dy][p1x]}{grid[p2y - dy][p2x]}")
         grid[p1y][p1x] = grid[p1y - dy][p1x]
         grid[p2y][p2x] = grid[p2y - dy][p2x]
         grid[p1y - dy][p1x] = "."
         grid[p2y - dy][p2x] = "."
         self.PrintGrid(grid)
         a = input()
         return True
      if b1 == "#" or b2 == "#":
         print("C")
         return False
      if b1 == "[":
         print(f"A   {b1}{b2}")
         if self.TryMoveB(grid, p1x, p1y + dy, dy, "CenterA"):
            print(f"A ok  {pp}")
            print(f"  {grid[p1y][p1x]}{grid[p2y][p2x]}  <- {grid[p1y - dy][p1x]}{grid[p2y - dy][p2x]}")
            """
            grid[p1y + dy][p1x] = grid[p1y][p1x]
            grid[p2y + dy][p2x] = grid[p2y][p2x]
            grid[p1y][p1x] = "."
            grid[p2y][p2x] = "."
            """
            self.PrintGrid(grid)
            a = input()
            return True
      elif b1 == "]":
         print("B")
         if self.TryMoveB(grid, p1x - 1, p1y + dy, dy, "LeftB") and \
            self.TryMoveB(grid, p1x + 1, p1y + dy, dy, "RightB"):
            print(f"B ok {pp}")
            print(f"  {grid[p1y][p1x]}{grid[p2y][p2x]}  <- {grid[p1y - dy][p1x]}{grid[p2y - dy][p2x]}")
            grid[p1y][p1x] = grid[p1y - dy][p1x]
            grid[p2y][p2x] = grid[p2y - dy][p2x]
            grid[p1y - dy][p1x] = "."
            grid[p2y - dy][p2x] = "."
            self.PrintGrid(grid)
            a = input()
            return True
      else:
         print(f"Bad {b1}{b2}")
      return False

   def MoveB(self, grid, rx: int, ry: int, dx: int, dy: int, width: int, height: int) -> Tuple[int, int]:

      p1 = grid[ry + dy][rx]
      if p1 == "#":
         return (rx, ry)
      if p1 == ".":
         grid[ry + dy][rx] = "@"
         grid[ry][rx] = "."
         return (rx, ry + dy)
      by1 = ry + dy
      if p1 == "[":
         print("**")
         bx1 = rx
      elif p1 == "]":
         print("****")
         bx1 = rx - 1
      else:
         print("Bad !!!!!")
      
      if self.TryMoveB(grid, bx1, by1, dy, "First"):
         grid[ry + dy][rx] = "@"
         grid[ry][rx] = "."
         return (rx, ry + dy)
      
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
         #print(row)
      #print(movements)
      #print(len(movements))
      #print(f"{rx},{ry}")
      #print(f"{width},{height}")

      directions = { "^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0) }

      for m in movements:
         rx, ry = self.MoveA(grid, rx, ry, *directions[m], width, height)

      self.PrintGrid(grid)
      
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
      print(f"{rx},{ry}")
      print(f"{width},{height}")

      directions = { "^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0) }

      self.PrintGrid(grid)

      for m in movements:
         print(f"------------------- {m} -------")
         if m in "<>":
            rx, ry = self.MoveA(grid, rx, ry, *directions[m], width, height)
         else:
            rx, ry = self.MoveB(grid, rx, ry, *directions[m], width, height)
         self.PrintGrid(grid)
         a = input()

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

