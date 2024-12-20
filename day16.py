# Day 16 of Advent of Code 2024: Reindeer Maze
# https://adventofcode.com/2024/day/16
from itertools import pairwise
import networkx as nx

class Maze:
    def __init__(self, fhandle):
        self.grid = []
        for y, row in enumerate(fhandle):
            self.grid.append(row.strip())
            if 'E' in row:
                self.end = (row.index('E'), y)
            if 'S' in row:
                self.source = (row.index('S'), y)

        self.maxY = len(self.grid)
        self.maxX = len(self.grid[0])
    
    def __str__(self):
        return '\n'.join(self.grid)
    
    def __getitem__(self, index):
        x, y = index
        if 0 <= x < self.maxY and 0 <= y < self.maxY:
            return self.grid[y][x]
    
    def toNX(self):
        G = nx.Graph()
        for y, row in enumerate(self.grid[1:-1], start=1):
            for x, c in enumerate(zip(row, row[1:], row[2:]), start=1):
                l, m, r = c
                if m == '#':
                    continue
                elif m == 'S':
                    G.add_edge((x,y), (x+1,y), weight=1)
                    G.add_edge((x,y), (x,y-1), weight=1001)
                    continue
                elif m == 'E':
                    G.add_edge((x,y), (x-1,y), weight=1)
                    G.add_edge((x,y), (x,y+1), weight=1)
                    continue
                
                if l+m+r == '...':
                    if self[(x,y-1)] == '.' and self[(x,y+1)] == '.':
                        G.add_edge((x,y-1),(x,y+1), weight=2)
                        G.add_edge((x+1,y),(x+1,y), weight=2)
                        continue

                    if self[(x-1,y-1)] == '.':
                        G.add_edge((x,y),(x-1,y-1), weight=1002)
                    if self[(x+1,y-1)] == '.':
                        G.add_edge((x,y),(x+1,y-1), weight=1002)
                    if self[(x-1,y-1)] == '#' and self[(x-1,y+1)] == '#':
                        G.add_edge((x,y), (x-1,y), weight = 1)
                    elif self[(x-2,y)] == '.':
                        G.add_edge((x,y),(x-2,y), weight = 2)
                
                elif l+m+r == '#.#':
                    if self[(x,y-1)] == '#':
                        continue
                    if self[(x-1,y-1)] == '.':
                        G.add_edge((x,y),(x-1,y-1), weight=1002)
                    if self[(x+1, y-1)] == '.':
                        G.add_edge((x,y),(x+1,y-1), weight=1002)
                    if self[(x+1, y-1)] == '#' and self[(x-1,y-1)] == '#':
                        G.add_edge((x,y),(x,y-1), weight=1)
                    elif self[(x,y-2)] == '.':
                        G.add_edge((x,y),(x,y-2), weight=2)
        return G

                    
                




def main():
    res1, res2 = None, None
    with open("input16.txt") as file:
        maze = Maze(file)
    G = maze.toNX()
    shortPath = nx.shortest_path(G, source=maze.source, target=maze.end, weight='weight')
    weightsAlongPath = [G[u][v]['weight'] for u,v in pairwise(shortPath)]
    res1 = sum(weightsAlongPath)
    # for n, w in zip(shortPath, weightsAlongPath):
    #     print(n, w,end=' ')
    # print(f'{shortPath[-1]}\n')

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
