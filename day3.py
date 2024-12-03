# Day 3 of Advent of Code 2024: Mull It Over
# https://adventofcode.com/2024/day/3

def main():
    res1, res2 = 0, 0
    mulON = True 
    with open("input3.txt") as file:
        for row in file:
            pointer = 0
            while pointer < len(row):
                char = row[pointer]
                if row[pointer:pointer + 4] == 'mul(':
                    pointer += 4
                    try:
                        closingPar = row[pointer:pointer + 10].index(")")
                    except ValueError:
                        # no closing paranthesis found
                        continue
                    # expect a string xxxx,yyyy where x&y's are integers
                    twoNums = row[pointer:pointer + closingPar]
                    if ',' not in twoNums:
                        continue
                    left, right = twoNums.split(',')
                    if not left.isnumeric() or not right.isnumeric():
                        continue
                    
                    res1 += int(left)*int(right)
                    if mulON:
                        res2 += int(left)*int(right)

                    pointer += closingPar
                elif row[pointer:pointer + 4] == 'do()':
                    mulON = True
                    pointer += 4
                elif row[pointer:pointer + 7] == "don't()":
                    mulON = False
                    pointer += 7
                else:
                    pointer += 1

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
