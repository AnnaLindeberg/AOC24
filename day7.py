# Day 7 of Advent of Code 2024: Bridge Repair
# https://adventofcode.com/2024/day/7
from collections import deque

def canBeValid(goal, ints, withConcat=False):
    Q = deque()
    Q.append(ints)
    while Q:
        version = Q.pop()
        if len(version) == 2:
            l, r = version
            if withConcat and int(str(l)+str(r)) == goal:
                return True
            if goal in [l + r, l * r]:
                return True
        elif len(version) > 2:
            Q.append([version[0] + version[1]] + version[2:])
            Q.append([version[0] * version[1]] + version[2:])
            if withConcat:
                Q.append([int(str(version[0]) + str(version[1]))] + version[2:])
    return False


def main():
    res1, res2 = 0, 0
    with open("input7.txt") as file:
        for row in file:
            goal, rest = row.strip().split(':')
            goal = int(goal)
            ints = list(map(int,rest.strip().split()))
            if canBeValid(goal, ints):
                # print(goal, ints)
                res1 += goal
            elif canBeValid(goal, ints, withConcat=True):
                # print(goal, ints, 'with ||')
                res2 += goal

    print(f"Task 1: {res1}\nTask 2: {res1+res2}")


if __name__ == '__main__':
    main()
