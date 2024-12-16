# Day 15 of Advent of Code 2024: Warehouse Woes
# https://adventofcode.com/2024/day/15

class Warehouse:
    def __init__(self, grid, robot) -> None:
        self.grid = grid
        self.max_y = len(grid) - 1
        self.max_x = len(grid[0]) - 1
        self.robot = robot
        # self.offsets = {'N':(0,-1), 'E':(1,0), 'W':(-1,0), 'S':(0,1), 'NE':(1,1), 'NW': (-1,1), 'SE':(1,-1), 'SW':(-1,-1)}
        self.offsets = {'^':(0,-1), '>':(1,0), '<':(-1,0), 'v':(0,1)}

    def __getitem__(self, index):
        if isinstance(index, tuple):
            x, y = index
            if 0 <= x <= self.max_x and 0 <= y <= self.max_y:
                return self.grid[y][x]
            else:
                return ''
        if isinstance(index, slice):
            res = ""
            offset = self.offsets[index.step]
            pos = index.start
            if index.stop is None:
                if index.step == '<':
                    stop = (-1, index.start[1])
                elif index.step == '^':
                    stop = (index.start[0], -1)
                elif index.step == '>':
                    stop = (self.max_x + 1, index.start[1])
                else:
                    stop = (index.start[0], self.max_y + 1)
            else:
                stop = index.stop
            i = 1
            while pos[0] != stop[0] or pos[1] != stop[1]:
                res += self[pos]
                pos = (index.start[0] + i*offset[0], index.start[1] + i*offset[1])
                i += 1
            return res
    
    def __setitem__(self, pos, elt):
        if self[pos] != '':
            self.grid[pos[1]][pos[0]] = elt
    
    def __str__(self):
        res = ""
        for row in self.grid:
            res += ''.join(row) + '\n'
        return res

    def moveRobot(self, direction):
        stuffInFront = self[self.robot::direction]
        if '.' not in stuffInFront or stuffInFront.index('.') > stuffInFront.index('#'):
            return
        offset = self.offsets[direction]
        # deal with moving any boxes
        if stuffInFront[1] != '.':
            steps = stuffInFront.index('.')
            newBoxPos = (self.robot[0] + offset[0]*steps, self.robot[1] + offset[1]*steps)
            self[newBoxPos] = 'O'
        # deal with moving the robot
        newRobotPos = (self.robot[0]+offset[0], self.robot[1]+offset[1])
        self[newRobotPos] = '@'
        self[self.robot] = '.'
        self.robot = newRobotPos
    
    def GPSscore(self):
        res = 0
        for y, row in enumerate(self.grid):
            for x, stuff in enumerate(row):
                if stuff == 'O':
                    res += x + y*100
        return res

def main():
    objects = []
    readingGrid = True
    moveseq = ""
    with open("input15.txt") as file:
        for y, row in enumerate(file):
            row = row.strip()
            if len(row) == 0:
                readingGrid = False
                continue
            if readingGrid:
                if '@' in row:
                    robotPos = (row.index('@'), y)
                    # row.replace('@', '.')
                objects.append(list(row))
            else:
                moveseq += row
    warehouse = Warehouse(objects, robotPos)
    # print(warehouse)
    for dir in moveseq:
        # print(dir)
        warehouse.moveRobot(dir)
    res1 = warehouse.GPSscore()
    
    print(f"Task 1: {res1}\nTask 2: {0}")


if __name__ == '__main__':
    main()
