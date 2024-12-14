# Day 12 of Advent of Code 2024: Garden Groups
# https://adventofcode.com/2024/day/12
from collections import deque, defaultdict
from itertools import pairwise

def intervals(L):
    L = sorted(L)
    intervalCount = 0
    for e1,e2 in pairwise(L):
        if e2 != e1 + 1:
            intervalCount += 1
    return intervalCount + 1


class FlowerBeds:
    def __init__(self, fhandle):
        self.grid = []
        for row in fhandle:
            self.grid.append(row.strip())
        self.maxY = len(self.grid)
        self.maxX = len(self.grid[0])
        self.cost = 0
        self.cheapCost = 0
        self.fenced = set()
    
    def __getitem__(self, index):
        x, y = index
        if 0 <= x < self.maxY and 0 <= y < self.maxY:
            return self.grid[y][x]
        
    
    def fenceBed(self, start):
        flower = self[start]
        if start in self.fenced or flower is None:
            return 0, 0
        queue = deque()
        queue.append(start, )
        area, permineter = 0, 0
        verticalSides, horizontalSides = defaultdict(list), defaultdict(list)
        while queue:
            pos = queue.pop()
            area += 1
            self.fenced.add(pos)
            for offset in [(0,1), (1,0), (-1,0), (0,-1)]:
                xoff, yoff = offset
                adj = (pos[0]+xoff, pos[1]+yoff)
                if self[adj] != flower:
                    permineter += 1
                    if offset == (1,0):
                        verticalSides[pos[0]+0.1].append(pos[1])
                    elif offset == (-1,0):
                        verticalSides[pos[0]-0.1].append(pos[1])
                    elif offset == (0,1):
                        horizontalSides[pos[1]+0.1].append(pos[0])
                    else:
                        horizontalSides[pos[1]-0.1].append(pos[0])

                elif (adj not in self.fenced) and (adj not in queue):
                    queue.append(adj)

        
        cost = area*permineter
        verticalSides = {k:intervals(v) for k,v in verticalSides.items()}
        horizontalSides = {k:intervals(v) for k,v in horizontalSides.items()}
        sides = 0
        for count in verticalSides.values():
            sides += count
        for count in horizontalSides.values():
            sides += count
        cheaperCost = area*sides
        self.cost += cost
        self.cheapCost += cheaperCost
        return cost, cheaperCost
    
    def fenceAll(self):
        for y, row in enumerate(self.grid):
            for x, flower in enumerate(row):
                if (x,y) not in self.fenced:
                    # print(f"{flower}: {self.fenceBed((x,y))}")
                    self.fenceBed((x,y))
        return self.cost, self.cheapCost
    


def main():
    with open("input12.txt") as file:
        flowerbeds = FlowerBeds(file)
    
    res1, res2 = flowerbeds.fenceAll()

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
