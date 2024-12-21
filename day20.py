# Day 20 of Advent of Code 2024: Race Condition
# https://adventofcode.com/2024/day/20
import networkx as nx
from math import inf
from collections import defaultdict

class RaceTrack:
    def __init__(self, tmp):
        self.track = tmp
        G = nx.Graph()
        for y, row in enumerate(tmp[1:-1],start=1):
            for x, stuff in enumerate(row[1:-1], start=1):
                if stuff == '#':
                    continue
                G.add_node((x,y))
                if tmp[y-1][x] != '#':
                    G.add_edge((x,y),(x,y-1))
                if tmp[y][x-1] != '#':
                    G.add_edge((x,y),(x-1,y))
                if stuff == 'S':
                    self.start = (x,y)
                if stuff == 'E':
                    self.end = (x,y)
        self.mazeLimits = (x,y)
        self.G = G
        max_len = len(nx.shortest_path(self.G, self.start, self.end)) - 1
        print("max", max_len)
        self.toEnd = defaultdict(lambda: inf, nx.single_target_shortest_path_length(self.G, self.end, cutoff=max_len))
        self.toEndBackwards = defaultdict(list)
        for k, v in self.toEnd.items():
            self.toEndBackwards[v].append(k)
        self.fromStart = defaultdict(lambda: inf, nx.single_source_shortest_path_length(self.G, self.start, cutoff=max_len))
        self.maxLen = max_len

    def cheatJumpHere(self, here, scoreSave, stepLimit):
        res = list()
        x, y = here
        if stepLimit < 5:
            noCheatScore = self.fromStart[here] + self.toEnd[here]
            for steps in [(0,0), (-2,0), (0,-2), (0,2), (2,0), (1,1), (-1,1), (-1,-1),(1,-1)]:
                new_x, new_y = x + steps[0], y + steps[1]
                scoreWithThisCheat = self.fromStart[here] + self.toEnd[(new_x,new_y)] + 2
                if scoreWithThisCheat < noCheatScore:
                    res.append(scoreWithThisCheat)
        else:
            scoreToBeat = self.maxLen - scoreSave
            for i in range(scoreToBeat + 1):
                for x2, y2 in self.toEndBackwards[i]:
                    if abs(x-x2) + abs(y-y2) <= stepLimit:
                        res.append(self.fromStart[here] + i + abs(x-x2) + abs(y-y2))
        return res
        
    
    def allCheatJumps(self, minSave, stepLimit):
        res = defaultdict(int)
        for x,y in self.G:
            if (x,y) == self.end or self.fromStart[(x,y)] > self.maxLen:
                continue
            withCheat = self.cheatJumpHere((x,y), minSave, stepLimit)
            woCheat = self.fromStart[(x,y)] + self.toEnd[(x,y)]
            for score in withCheat:
                if woCheat - score >= minSave:
                    res[woCheat - score] += 1
        return res
        

    def __str__(self):
        return str(self.G)



def main():
    res1, res2 = None, None
    tmp = []
    with open("input20.txt") as file:
        for row in file:
            tmp.append(row.strip())

    track = RaceTrack(tmp)
    countsOfSaves = track.allCheatJumps(100, 2)
    res1 = sum(countsOfSaves.values())
    
    countsOfSaves = track.allCheatJumps(100, 20)
    res2 = sum(countsOfSaves.values())

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
