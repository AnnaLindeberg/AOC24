# Day 12 of Advent of Code 2024: Garden Groups
# https://adventofcode.com/2024/day/12
from collections import deque

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
            return 0,0
        queue = deque()
        queue.append((start, []))
        area, permineter, sides = 0, 0, 0
        while queue:
            pos, fences2continue = queue.pop()
            area += 1
            self.fenced.add(pos)
            neighbors, fenceDirs = [], []
            for xoff,yoff in [(0,1), (1,0), (-1,0), (0,-1)]:
                adj = (pos[0]+xoff, pos[1]+yoff)
                if self[adj] != flower:
                    fenceDirs.append((xoff,yoff))
                    permineter += 1
                elif (adj not in self.fenced) and (adj not in [q[0] for q in queue]):
                    neighbors.append((adj, (xoff,yoff)))
            
            sides += len(set(fenceDirs).difference(fences2continue))
            for adj, offset in neighbors:
                newFences = [fence for fence in fenceDirs if (fence[0]+offset[0],fence[1]+offset[1]) != (0,0)]
                queue.append((adj, newFences))

        
        cost = area*permineter
        lowCost = area*sides
        self.cost += cost
        self.cheapCost += lowCost
        return cost, lowCost
    
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
