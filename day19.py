# Day 19 of Advent of Code 2024: Linen Layout
# https://adventofcode.com/2024/day/19

from collections import defaultdict


def designsPossible(towelLookup, design):
    n = len(design)
    DP = [0 for _ in range(n + 1)] # index k will store no of ways to make design[k:]
    DP[-1] = 1 # dummy position n is used for the case when the design ends with a given pattern
    for idx in range(n-1,-1,-1):
        possibilities = 0
        for chunk in towelLookup[design[idx]]:
            if idx + len(chunk) > n:
                # this definitely won't fit
                continue
            elif design[idx:idx+len(chunk)] == chunk:
                possibilities += DP[idx + len(chunk)]
        DP[idx] = possibilities
    return DP[0]

                


def main():
    res1, res2 = 0, 0
    with open("input19.txt") as file:
        towels = file.readline().strip().split(', ')
        # patterns between 1 and 8 in length
        # 5 different colors: burwg
        towelsLookup = defaultdict(list)
        for towel in towels:
            towelsLookup[towel[0]].append(towel)
        file.readline()
        for row in file:
            possible = designsPossible(towelsLookup, row.strip())
            res2 += possible
            if possible > 0:
                res1 += 1

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
