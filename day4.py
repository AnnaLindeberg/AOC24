# Day 4 of Advent of Code 2024: Ceres Search
# https://adventofcode.com/2024/day/4
from collections import Counter

class Grid:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.max_y = len(grid) - 1
        self.max_x = len(grid[0]) - 1
        self.offsets = {'N':(0,-1), 'E':(1,0), 'W':(-1,0), 'S':(0,1), 'NE':(1,1), 'NW': (-1,1), 'SE':(1,-1), 'SW':(-1,-1)}

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
            i = 1
            while pos[0] != index.stop[0] or pos[1] != index.stop[1]:
                res += self[pos]
                pos = (index.start[0] + i*offset[0], index.start[1] + i*offset[1])
                i += 1
            return res
            
    def wordsFromHere(self, here, length=4):
        res = []
        for dir, offset in self.offsets.items():
            stop = (here[0] + offset[0]*length, here[1] + offset[1]*length)
            word = self[here:stop:dir]
            if len(word) == length:
                res.append(word)
        return res

    def wordSearch(self, word):
        # return counts of the occurrence of the word ≠ ''
        indices = [(x,y) for x in range(self.max_x + 1) for y in range(self.max_y + 1)]
        res = 0
        for index in indices:
            if self[index] != word[0]:
                continue
            wordCounts = Counter(self.wordsFromHere(index, len(word)))
            res += wordCounts[word]
        return res
    
    def wordSearch_XMAS(self):
        indices = [(x,y) for x in range(1, self.max_x) for y in range(1, self.max_y)]
        res = 0
        for index in indices:
            if self[index] != 'A':
                continue
            words = [self[(index[0]-1, index[1]+1):(index[0]+2, index[1]-2):'SE'], self[(index[0]+1,index[1]+1):(index[0]-2,index[1]-2):'SW']]
            # print(index, words)
            if words[0] not in ['MAS','SAM']:
                continue
            if words[1] not in ['MAS','SAM']:
                continue
            res += 1
        return res



def main():
    grid = []
    with open("input4.txt") as file:
        for row in file:
            grid.append(row.strip())
    grid = Grid(grid)
    res1 = grid.wordSearch('XMAS')
    res2 = grid.wordSearch_XMAS()
    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
