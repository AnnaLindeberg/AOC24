# Day 6 of Advent of Code 2024: Guard Gallivant
# https://adventofcode.com/2024/day/6
from collections import defaultdict
import copy

class Map:
    def __init__(self, fhandle) -> None:
        self.directions = [(0,-1), (1,0), (0,1), (-1, 0)]
        map = []
        for y, row in enumerate(fhandle):
            row = row.strip()
            if '^' in row:
                x = row.index('^')
                row = row.replace('^', '.')
                self.guard = (x,y)
            map.append(row)
        
        self.map = map
        self.guardDir = (0, -1)
        self.guardOnLoop = False
        self.visited = defaultdict(set)
        # self.visited[self.guard].add((self.guardDir))
        self.max_x = len(map[0])
        self.max_y = len(map)

    def __str__(self) -> str:
        return "\n".join(self.map) + '\n'

    def __getitem__(self, index):
        if not isinstance(index, tuple):
            raise TypeError
        x, y = index
        if isinstance(x, slice) and isinstance(y,slice):
            if x.step == 0:
                return self[x.start,y]
            elif y.step == 0:
                return self[x, y.start]
            else:
                raise TypeError
        elif isinstance(x, int) and isinstance(y, int):
            if 0 <= x < self.max_x and 0 <= y < self.max_y:
                return self.map[y][x]
            # else:
            #     return ''
        elif isinstance(x, slice) and isinstance(y, int):
            start = 0 if x.start is None else x.start
            if x.stop is None and (x.step is None or x.step > 0):
                stop = self.max_x
            elif x.stop is None:
                stop = -1
            else:
                stop = x.stop
            step = 1 if x.step is None else x.step

            if 0 <= y < self.max_y:
                return "".join([self.map[y][xc] for xc in range(start, stop, step)])
        elif isinstance(x, int) and isinstance(y, slice):
            start = 0 if y.start is None else y.start
            if y.stop is None and (y.step is None or y.step > 0):
                stop = self.max_y
            elif y.stop is None:
                stop = -1
            else:
                stop = y.stop
            step = 1 if y.step is None else y.step
            
            if 0 <= x < self.max_x:
                return "".join([self.map[yc][x] for yc in range(start, stop, step)])

    def placeObstruction(self, x, y):
        if 0 <= x < self.max_x and 0 <= y < self.max_y:
            self.map = self.map[:y] + [self.map[y][:x] + '#' + self.map[y][x+1:]] + self.map[y+1:]
        else:
            raise TypeError

    def walkForward(self):
        if self.guard is None:
            return False
        xOff, yOff = self.guardDir
        x, y = self.guard
        ahead = self[x::xOff,y::yOff]
        guardOnMap = True
        if '#' in ahead:
            obstruction = ahead.index('#')
        else:
            obstruction = len(ahead)
            guardOnMap = False
        for i in range(obstruction):
            thisPoint = (x + xOff*i, y + yOff*i)
            if self.guardDir in self.visited[thisPoint]:
                self.guardOnLoop = True
            else:
                self.visited[thisPoint].add(self.guardDir)
        
        if guardOnMap:
            self.guard = thisPoint
            self.guardDir = self.directions[(1 + self.directions.index(self.guardDir)) % 4]
            return True
        self.guard = None
        self.guardDir = None
        # print("Guard leaves the map now")
        return False
            

        
        

def main():
    with open("input6.txt") as file:
        startmap = Map(file)
    map = copy.deepcopy(startmap)
    
    guardOnMap = map.walkForward()
    while guardOnMap:
        guardOnMap = map.walkForward()
    res1 = len(map.visited)
    obstructionPositions = list(map.visited.keys())

    res2 = 0
    for obstruction in obstructionPositions:
        if obstruction == startmap.guard:
            continue
        map = copy.deepcopy(startmap)
        map.placeObstruction(*obstruction)
        guardOnMap = map.walkForward()
        while guardOnMap and not map.guardOnLoop:
            guardOnMap = map.walkForward()
        if map.guardOnLoop:
            res2 += 1
    
    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
