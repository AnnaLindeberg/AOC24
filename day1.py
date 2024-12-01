# Day 1 of Advent of Code 2024: Historian Hysteria
# https://adventofcode.com/2024/day/1
from collections import Counter

def main():
    with open("input1.txt") as file:
        left, right = [], []
        for row in file:
            l, r  = list(map(int, row.strip().split()))
            left.append(l)
            right.append(r)
        
        left.sort()
        right.sort()
        res1 = 0
        for x, y in zip(left,right):
            res1 += abs(x - y)
        
        rightCount = Counter(right)
        res2 = 0
        for x in left:
            res2 += x*rightCount[x]


    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
