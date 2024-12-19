# Day 17 of Advent of Code 2024: Chronospatial Computer
# https://adventofcode.com/2024/day/17
from math import trunc
from itertools import product

class FastSmallComputer:
    def __init__(self, A):
        self.A = A

    def runProgram(self):
        output = []
        while self.A != 0:
            print(f"A is {bin(self.A)} output {self.A % 8}")
            self.A = trunc(self.A / 8)
            output.append(self.A % 8)
        return output

class FastComputer:
    def __init__(self, A):
        self.A = A
        self.B = 0
        self.C = 0
    
    def runProgram(self):
        output = []
        while self.A != 0:
            self.B = (self.A % 8) ^ 2
            self.C = self.A // (2 ** self.B)
            self.A = self.A // 8
            self.B = (self.B ^ 7) ^ self.C
            output.append(self.B % 8)
        return output

class Computer:
    def __init__(self, A, B, C, program):
        self.regA = A
        self.regB = B
        self.regC = C
        self.program = program
        self.instrPtr = 0
        self.output = ''
    
    def __str__(self):
        return f"Computer(A:{self.regA} B:{self.regB} C:{self.regC})"
    
    def comboOperand(self, operand):
        comboOperands = {0:0, 1:1, 2:2, 3:3, 4:self.regA, 5:self.regB, 6:self.regC}
        return comboOperands[operand]    
    
    def oneOperation(self):
        opcode, operand = self.program[self.instrPtr], self.program[self.instrPtr + 1]
        if self.instrPtr < 0 or self.instrPtr >= len(self.program):
            print("Halt reached")
            return

        if opcode == 0:
            numerator = self.regA
            denominator = 2**self.comboOperand(operand)
            self.regA = numerator//denominator
            self.instrPtr += 2
        elif opcode == 1:
            self.regB = self.regB ^ operand
            self.instrPtr += 2
        elif opcode == 2:
            self.regB = self.comboOperand(operand) % 8
            self.instrPtr += 2
        elif opcode == 3:
            if self.regA != 0:
                self.instrPtr = operand
            else:
                self.instrPtr += 2
        elif opcode == 4:
            self.regB = self.regB ^ self.regC
            self.instrPtr += 2
        elif opcode == 5:
            out = self.comboOperand(operand) % 8
            self.output += str(out)
            self.instrPtr += 2
        elif opcode == 6:
            numerator = self.regA
            denominator = 2**self.comboOperand(operand)
            self.regB = numerator//denominator
            self.instrPtr += 2
        elif opcode == 7:
            numerator = self.regA
            denominator = 2**self.comboOperand(operand)
            self.regC = numerator//denominator
            self.instrPtr += 2
    
    def runProgram(self):
        n = len(self.program)
        while 0 <= self.instrPtr < n:
            self.oneOperation()
        return ','.join(self.output)

def wildTest(program):
    res = ''
    look = {5:"000", 4:"001", 7:"011", 1:"100", 0:"101",3:"110", 2:"111"}
    # look = {5:"101", 4:"100", 7:"111", 1:"001", 0:"000",3:"011", 2:"010"}
    for e in program[::-1]:
        res += look[e]
    return res


def main():
    with open("input17.txt") as file:
        A = int(file.readline().strip().split()[-1])
        for _ in range(3):
            file.readline()

        program = list(map(int, file.readline().strip().split()[-1].split(',')))
    # comp = Computer(A,0,0,program)
    fcomp = FastComputer(A)
    res1 = fcomp.runProgram()
    res1 = ','.join(map(str, res1))

    res2 = None
    # a = int(wildTest(program), base=2)
    # smallComp = FastSmallComputer(117440)
    # print(smallComp.runProgram())
    # print(program)
    # A = wildTest(program)
    # print(A, int(A, base = 2))
    # comp2 = FastComputer(int(A, base = 2))
    # res2 = comp2.runProgram()
    # print(program)
    # print(res2)
    # for tryA in range(190354025692175, 190354157812751):
    #     # if tryA % 8 != 5:
    #     #     continue
    #     comp = FastComputer(tryA)
    #     res = comp.runProgram()
    #     if res == program:
    #         print(res)
    #         print(bin(tryA))
    #         res2 = tryA
    #         break
    # fcomp2 = FastComputer(8**16-1)
    # print(fcomp2.runProgram())
    # print(program)

    # print(wildTest(program))
    # test = '101011010010000001000100111110010011110'
    start = '101011010010000001000'
    end = '101010011110000001111'
    print(start, '    ', end)
    for s in product('01', repeat=6):# 27
        Aval = int(start + ''.join(s) + end, base=2)
        c = FastComputer(Aval)
        res = c.runProgram()
        print(res)
        if res == program:
            res2 = Aval
            break
    print('--')
    print(program)
    
    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()


    # 0b11100101011000000
    # 000011100101001000

    11100101001000
    11100101011000000