# Day 14 of Advent of Code 2024: Restroom Redoubt
# https://adventofcode.com/2024/day/14
import re
from math import prod
from collections import Counter

class RobotArea:
    def __init__(self, robots, width=101, height=103):
        self.width = width
        self.height = height
        self.robots = robots
        pass
    
    def __str__(self):
        filtered = [r[0] for r in self.robots]
        countsPerPos = Counter(filtered)
        res = ""
        for y in range(self.height):
            for x in range(self.width):
                if (x,y) in countsPerPos:
                    res += str(countsPerPos[(x,y)])
                else:
                    res += '.'
            res += '\n'
        return res


    def moveRobot(self, robot):
        pos, vel = robot
        newPos = ((pos[0] + vel[0]) % self.width, (pos[1]+ vel[1]) % self.height)
        return newPos
    
    def moveAllRobots(self):
        for i, robot in enumerate(self.robots):
            newPos = self.moveRobot(robot)
            self.robots[i] = (newPos, robot[1])
    
    def safetyFactor(self):
        xMid, yMid = self.width//2, self.height//2
        quadrants = [0,0,0,0]
        for robot in self.robots:
            x, y = robot[0][0], robot[0][1]
            if 0 <= x < xMid:
                if 0 <= y < yMid:
                    quadrants[0] += 1
                elif yMid < y < self.height:
                    quadrants[1] += 1
            elif xMid < x < self.width:
                if 0 <= y < yMid:
                    quadrants[2] += 1
                elif yMid < y < self.height:
                    quadrants[3] += 1
        return prod(quadrants)


def main():
    robots = []
    with open("input14.txt") as file:
        for row in file:
            x,y, vx, vy = list(map(int, re.findall(r'(-?\d+)', row.strip())))
            robots.append(((x,y),(vx,vy)))
    
    area = RobotArea(robots)
    for _ in range(100):
        area.moveAllRobots()

    print(area)
    res1 = area.safetyFactor()

    print(f"Task 1: {res1}\nTask 2: {0}")


if __name__ == '__main__':
    main()
