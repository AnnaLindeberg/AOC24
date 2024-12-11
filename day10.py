# Day 10 of Advent of Code 2024: Hoof It
# https://adventofcode.com/2024/day/10
from collections import deque

class Grid:
    def __init__(self, fhandle):
        self.grid = []
        for row in fhandle:
            self.grid.append(row.strip())
        self.maxY = len(self.grid)
        self.maxX = len(self.grid[0])
    
    def __getitem__(self, index):
        x, y = index
        if 0 <= x < self.maxY and 0 <= y < self.maxY:
            return int(self.grid[y][x])
        
    def DFS(self, start):
        stack = deque()
        for xoff,yoff in [(0,1), (1,0), (-1,0), (0,-1)]:
            stack.append(((start[0]+xoff, start[1]+yoff), 0))
        trailHeads = set()
        trails = 0
        while stack:
            pos, k = stack.pop()
            if self[pos] is None:
                continue
            if self[*pos] == 9 and k == 8:
                trailHeads.add(pos)
                trails += 1
            elif self[pos] == k + 1:
                for xoff,yoff in [(0,1), (1,0), (-1,0), (0,-1)]:
                    stack.append(((pos[0]+xoff, pos[1]+yoff), k+1))
        return len(trailHeads), trails
        

def main():
    with open("input10.txt") as file:
        grid = Grid(file)
    
    res1, res2 = 0, 0
    for y, row in enumerate(grid.grid):
        for x, elt in enumerate(row):
            if elt != '0':
                continue
            heads, trails = grid.DFS((x,y))
            print(heads, trails)
            res1 += heads
            res2 += trails



    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
