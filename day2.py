# Day 2 of Advent of Code 2024: Red-Nosed Reports
# https://adventofcode.com/2024/day/2

def main():
    with open("input2.txt") as file:
        safeCount1 = 0
        safeCount2 = 0
        for row in file:
            report = list(map(int, row.strip().split()))
            distinctDiffs = set(second - first for first, second in zip(report, report[1:])) 
            if distinctDiffs.issubset({1,2,3}) or distinctDiffs.issubset({-1,-2,-3}):
                safeCount1 += 1
            else:
                for i in range(len(report)):
                    revisedReport = report[:i] + report[i+1:]
                    revisedDiffs = set(second - first for first, second in zip(revisedReport, revisedReport[1:])) 
                    if revisedDiffs.issubset({1,2,3}) or revisedDiffs.issubset({-1,-2,-3}):
                        safeCount2 += 1
                        break
            

    print(f"Task 1: {safeCount1}\nTask 2: {safeCount1 + safeCount2}")


if __name__ == '__main__':
    main()
