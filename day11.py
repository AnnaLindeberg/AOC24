# Day 11 of Advent of Code 2024: Plutonian Pebbles
# https://adventofcode.com/2024/day/11
from collections import defaultdict

class PebbleLine:
    def __init__(self, initialPebbles):
        self.initialPebbles = initialPebbles
        self.initialPebbles.sort()
        self.memory = defaultdict(dict)
    
    def transformPebble(self, pebble, blinks):
        if blinks == 0:
            return 1
        if blinks in self.memory[pebble]:
            return self.memory[pebble][blinks]
        if pebble == 0:
            res = self.transformPebble(1, blinks - 1)
        elif len(str(pebble)) % 2 == 0:
            sPebble = str(pebble)
            half = len(sPebble) // 2
            res = self.transformPebble(int(sPebble[:half]), blinks - 1)
            res += self.transformPebble(int(sPebble[half:]), blinks - 1)
        else:
            res = self.transformPebble(pebble*2024, blinks - 1)
        self.memory[pebble][blinks] = res
        return res

    def transformAll(self, blinks):
        res = 0
        for pebble in self.initialPebbles:
            res += self.transformPebble(pebble, blinks)
        return res



def main():
    with open("input11.txt") as file:
        for row in file:
            pebbles = list(map(int, row.strip().split()))
        
        pebbleLine = PebbleLine(pebbles)
        res1 = pebbleLine.transformAll(25)
        res2 = pebbleLine.transformAll(75)
        
    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
