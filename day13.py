# Day 13 of Advent of Code 2024: Claw Contraption
# https://adventofcode.com/2024/day/13
import re

class ClawMachine:
    def __init__(self, A, B, prize):
        self.A = A
        self.B = B
        self.prize = prize

    def __str__(self):
        return f"A: {self.A} B: {self.B} prize: {self.prize}"

    def __repr__(self):
        return str(self) 


def main():
    machines = []
    with open("small_input13.txt") as file:
        for i, row in enumerate(file):
            if i % 4 == 3:
                machines.append(ClawMachine(A, B, prize))
            
            coords = tuple(map(int, re.findall(r'(\d+)', row.strip())))
            if i % 4 == 0:
                A = coords
            elif i % 4 == 1:
                B = coords
            else:
                prize = coords

    print(machines)
    print(f"Task 1: {0}\nTask 2: {0}")


if __name__ == '__main__':
    main()
