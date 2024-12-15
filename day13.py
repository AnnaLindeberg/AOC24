# Day 13 of Advent of Code 2024: Claw Contraption
# https://adventofcode.com/2024/day/13
import re
from math import gcd

def singleSol(a, b, c):
    # return a single solution (x,y) to ax + by = c, if there is one
    if a < b:
        print("NOPE")
    d = gcd(a, b)
    if c % d != 0 or c / b < 0:
        # no integer solutions
        # resp. no solutions in first quadrant 0≤x and 0≤y
        return 
    bigger, smaller = a//d, b//d
    substitutionRules = {}
    while smaller > 1:
        substitutionRules[bigger % smaller] = [(bigger, 1), (smaller, (bigger // smaller)*(-1))]
        bigger, smaller = smaller, bigger % smaller
    combination = substitutionRules[1]
    while combination[0][0] != a // d:
        bigger, smaller = combination
        subBigger, subSmaller = substitutionRules[smaller[0]]
        combination = [(subBigger[0], subBigger[1]*smaller[1]), (bigger[0], bigger[1]+subSmaller[1]*smaller[1])]
    
    x0, y0 = combination[0][1]*c//d, combination[1][1]*c//d
    sols = set()
    if x0 < 0:
        gap = abs(x0) // (b//d)
        x0, y0 = x0 + (gap+1)* b//d, y0 - (gap+1)*a//d
        while 0 <= x0 and 0 <= y0:
            sols.add((x0,y0))
            x0 += b//d
            y0 -= a//d
    elif y0 < 0:
        gap = abs(y0) // (a//d)
        x0, y0 = x0 - (gap+1)* b//d, y0 + (gap+1)*a//d
        while 0 <= x0 and 0 <= y0:
            sols.add((x0,y0))
            x0 -= b//d
            y0 += a//d
    else:
        print("didnt want this to happen")

    print(x0,y0)
    # res = combination[0][1]*c//d, combination[1][1]*c//d
    

def allSolutions(a, b, c, xInt, yInt):
    # return all solutions (x,y) to ax + by = c such that x is in the interval xInt and y in interval yInt
    sol1 = singleSol(a, b, c)
    if sol1 is None:
        return []
    x0, y0 = sol1
    d = gcd(a, b)
    u, v = b //d, a //d
    sols = []
    if x0 < xInt[0]:
        if u == 0:
            return []
        i = 0
        while x0 <= xInt[1]:
            if xInt[0] <= x0 <= xInt[1] and yInt[0] <= y0 <= yInt[1]:
                sols.append((x0,y0))
            if u < 0:
                i -= 1
            else:
                i += 1
            x0, y0 = x0 + i*u, y0 - i*v
    elif x0 > xInt[1]:
        if u == 0:
            return []
        i = 0
        while x0 >= xInt[0]:
            if xInt[0] <= x0 <= xInt[1] and yInt[0] <= y0 <= yInt[1]:
                sols.append((x0,y0))
            if u < 0:
                i += 1
            else:
                i -= 1
            x0, y0 = x0 + i*u, y0 - i*v
    else:
        print("in interval")

def stupidWay(x, y, p, aInt, bInt):
    # find all a,b s.t. ax+by = p with a,b in intervals aint, bint
    sols = set()
    for a in range(aInt[0], aInt[-1]+1):
        if( p - a*x )% y != 0:
            continue
        b = (p - a*x)//y
        if bInt[0] <= b <= bInt[1]:
            sols.add((a,b))
    
    return sols



class ClawMachine:
    def __init__(self, A, B, prize):
        self.A = A
        self.B = B
        self.prize = prize

    def __str__(self):
        return f"A: {self.A} B: {self.B} prize: {self.prize}"

    def __repr__(self):
        return str(self)
    
    def minTokens(self):
        # possibleX = stupidWay(self.A[0], self.B[0], self.prize[0], [0,100], [0,100])
        # possibleY = stupidWay(self.A[1], self.B[1], self.prize[1], [0,100], [0,100])
        # possible = possibleX.intersection(possibleY)
        # tokens = [3*sol[0] + sol[1] for sol in possible]
        # if tokens:
        #     return min(tokens)
        # else:
        #     return 0
        x1, y1 = self.A
        x2, y2 = self.B
        px, py = self.prize
        if x1*y2 == x2*y1:
            return 0
        det = x1*y2 - x2*y1
        a0, b0 = px*y2 - py*x2, py*x1-px*y1
        if a0 % det == 0 and b0 % det == 0:
            return 3* a0//det + b0//det
        return 0
        
        


def main():
    machines = []
    largeMachines = []
    with open("small_input13.txt") as file:
        for i, row in enumerate(file):
            if i % 4 == 3:
                machines.append(ClawMachine(A, B, prize))
                largeMachines.append(ClawMachine(A, B, (int('10000000000000' + str(prize[0])), int('10000000000000' + str(prize[1])))))
            
            coords = tuple(map(int, re.findall(r'(\d+)', row.strip())))
            if i % 4 == 0:
                A = coords
            elif i % 4 == 1:
                B = coords
            else:
                prize = coords
    res1, res2 = 0, 0
    for machine in machines:
        tokens = machine.minTokens()
        # print(tokens)
        res1 += tokens
    print(largeMachines)
    for machine in largeMachines:
        tokens = machine.minTokens()
        # print(tokens)
        res2 += tokens
    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    # print(stupidWay(94, 22, 8400, [0,100],[0,100]))
    # print(stupidWay(34, 67, 5400, [0,100],[0,100]))
    # print(singleSol(94, 22, 10000000008400))
    main()
