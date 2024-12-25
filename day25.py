# Day 25 of Advent of Code 2024: Code Chronicle
# https://adventofcode.com/2024/day/25
from itertools import islice

def parse(rows):
    res = [0, 0, 0, 0, 0]
    isLock = rows[0].strip() == '#####'
    char = '#' if isLock else '.'
    for row in rows[1:-1]:
        res = [res[i] + (c == char) for i,c in enumerate(row.strip())]
    
    if not isLock:
        res = [5 - r for r in res]
    return isLock, res

def fits(lock, key):
    return len(list(filter(lambda t: t[0]+t[1] <=5, zip(lock, key)))) == 5

def part1(locks, keys):
    res = 0
    for lock in locks:
        for key in keys:
            if fits(lock, key):
                res += 1
    return res

def main():
    res1, res2 = None, None
    locks, keys = [], []
    with open("input25.txt") as file:
        while True:
            next_7_lines = list(islice(file, 7))
            file.readline()  # one blank
            if len(next_7_lines) != 7:
                break
            isLock, seq = parse(next_7_lines)
            if isLock:
                locks.append(seq)
            else:
                keys.append(seq)
            
    res1 = part1(locks, keys)
    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
