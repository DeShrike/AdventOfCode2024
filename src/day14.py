from aoc import Aoc
from canvas import Canvas
import itertools
import math
import re
import sys

# Day 14
# https://adventofcode.com/2024

class Day14Solution(Aoc):

   def Run(self):
      self.StartDay(14, "Restroom Redoubt")
      self.ReadInput()

      self.width = 101
      self.height = 103

      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(14)

      self.width = 11
      self.height = 7

      goal = self.TestDataA()
      self.PartA()
      self.Assert(self.GetAnswerA(), goal)

   def TestDataA(self):
      self.inputdata.clear()
      testdata = \
      """
      p=0,4 v=3,-3
      p=6,3 v=-1,-3
      p=10,3 v=-1,2
      p=2,0 v=2,-1
      p=0,0 v=1,3
      p=3,0 v=-2,-2
      p=7,6 v=-1,-3
      p=3,0 v=-1,-2
      p=9,3 v=2,3
      p=7,3 v=-1,2
      p=2,4 v=2,-3
      p=9,5 v=-3,-3
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 12

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return None

   def ParseInput(self):
      rx = re.compile("^p\=(?P<px>[0-9]*),(?P<py>[0-9]*) v\=(?P<vx>[\-0-9]*),(?P<vy>[\-0-9]*)$")

      data = []
      for line in self.inputdata:
         match = rx.search(line)
         px = int(match["px"])
         py = int(match["py"])
         vx = int(match["vx"])
         vy = int(match["vy"])
         data.append([px, py, vx, vy])

      return data

   def Step(self, steps: int, robot) -> None:
      x = robot[0]
      y = robot[1]
      vx = robot[2]
      vy = robot[3]
      x += vx * steps
      y += vy * steps
      x = x % self.width
      y = y % self.height
      robot[0] = x
      robot[1] = y

   def IsQ1(self, px: int, py: int):
      return px < self.width // 2 and py < self.height // 2

   def IsQ2(self, px: int, py: int):
      return px > self.width // 2 and py < self.height // 2

   def IsQ3(self, px: int, py: int):
      return px < self.width // 2 and py > self.height // 2

   def IsQ4(self, px: int, py: int):
      return px > self.width // 2 and py > self.height // 2

   def CountRobots(self, robots):
      grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
      for r in robots:
         grid[r[1]][r[0]] += 1

      return grid

   def CountQ(self, robots):
      q1 = q2 = q3 = q4 = 0
      for robot in robots:
         px = robot[0]
         py = robot[1]
         if self.IsQ1(px, py):
            q1 += 1
         elif self.IsQ2(px, py):
            q2 += 1
         elif self.IsQ3(px, py):
            q3 += 1
         elif self.IsQ4(px, py):
            q4 += 1
      return q1, q2, q3, q4

   def CreatePNGB(self, grid, step: int) -> None:
      boxsize = 4
      canvas = Canvas(self.width * boxsize, self.height * boxsize)
      for y in range(self.height):
         for x in range(self.width):
            c = grid[y][x]
            if c == 0:
               color = (0x18, 0x18, 0x18)
            elif c == 1:
               color = (0x00, 0xFF, 0x00)
            elif c == 2:
               color = (0xFF, 0x00, 0x00)
            else:
               color = (0xFF, 0xFF, 0xFF)
            canvas.set_big_pixel(x * boxsize, y * boxsize, color, boxsize)

      pngname = f"day14b{step:05}.png"
      print(f"Saving {pngname}")
      canvas.save_PNG(pngname)

   def PartA(self):
      self.StartPartA()

      robots = self.ParseInput()
      for robot in robots:
         self.Step(100, robot)

      q1, q2, q3, q4 = self.CountQ(robots)
      answer = q1 * q2 * q3 * q4

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      # 2781
      # 2882
      # 2983

      ix = 0
      robots = self.ParseInput()
      for step in range(7_000):
         for robot in robots:
            self.Step(1, robot)

         #if (step - 2781) % 101 == 0:
         if step == 6619:
            answer = step + 1
            grid = self.CountRobots(robots)
            ix += 1
            self.CreatePNGB(grid, step)

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day14Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5
   
