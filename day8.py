# Day 8 of Advent of Code 2024: Resonant Collinearity
# https://adventofcode.com/2024/day/8
from collections import defaultdict, deque
from itertools import combinations
import re

def antinodesOf(pos1, pos2, maxX, maxY):
    # assume pos1.x <= pos2.x
    xDiff = pos2[0] - pos1[0]
    yDiff = pos2[1] - pos1[1]
    res = []
    if 0 <= pos1[0]-xDiff < maxX and 0<= pos1[1]-yDiff < maxY:
        res.append((pos1[0]-xDiff, pos1[1]-yDiff))
    if 0 <= pos2[0]+xDiff < maxX and 0<= pos2[1]+yDiff < maxY:
        res.append((pos2[0]+xDiff, pos2[1]+yDiff))
    return res
        

def main():
    all_antennas = defaultdict(list)
    with open("small_input8.txt") as file:
        for y, row in enumerate(file):
            row = row.strip()
            for x, elt in enumerate(row):
                if elt == '.':
                    continue
                all_antennas[elt].append((x,y))
            maxX, maxY = len(row), y + 1
    
    # antinodes = set()
    # for antennas in all_antennas.values():
    #     for antennaA, antennaB in combinations(antennas, 2):
    #         if antennaA[0] <= antennaB[0]:
    #             newAntinodes = antinodesOf(antennaA, antennaB, maxX, maxY)
    #         else:
    #             newAntinodes = antinodesOf(antennaB, antennaA, maxX, maxY)
    #         print(antennaA, antennaB, newAntinodes)
    #         antinodes.update(newAntinodes)
    # res1 = len(antinodes)

    antinodes = set()
    for antennas in all_antennas.values():
        for idxA, antennaA in enumerate(antennas):
            for antennaB in antennas[idxA+1:]:
                if antennaA[0] <= antennaB[0]:
                    newAntinodes = antinodesOf(antennaA, antennaB, maxX, maxY)
                else:
                    newAntinodes = antinodesOf(antennaB, antennaA, maxX, maxY)
                antinodes.update(newAntinodes)
                for new in newAntinodes:
                    if new not in antennas:
                        antennas.append(new)
    res1 = len(antinodes)
    print(antinodes)

    #1302 too low
    print(f"Task 1: {res1}\nTask 2: {0}")


if __name__ == '__main__':
    main()
