# Day 9 of Advent of Code 2024: Disk Fragmenter
# https://adventofcode.com/2024/day/9

def checksum(s):
    res = 0
    for i, e in enumerate(s):
        e = int(e)
        print(i*e)
        res += i*e
    return res

def memory(s):
    fileContents = s[0::2]
    return sum([int(d) for d in fileContents])

def hardFragment(disk):
    diskIdx = 0
    diskMax = memory(disk)
    left = 0
    right = len(disk) if len(disk) % 2 == 0 else len(disk) - 1
    spaceLeft, notMovedRight = 0, int(disk[right])
    res1 = 0
    while diskIdx <= diskMax:
        if right - left == 1:
            for i in range(diskMax - diskIdx):
                # print((diskIdx + i)* (right // 2))
                res1 += (diskIdx + i)* (right // 2)
            break
        elif left % 2 == 0:
            # deal with files that remain in original place, at left pointer
            for i in range(int(disk[left])):
                # print((diskIdx + i) * (left // 2))
                res1 += (diskIdx + i) * (left // 2)
            diskIdx += int(disk[left])
            left += 1
            spaceLeft = int(disk[left])
        else:
            # move as much of the file contents from right pointer to the space where left pointer is
            if spaceLeft < notMovedRight:
                # can fill the space at left with file stuff from right
                for i in range(spaceLeft):
                    # print((diskIdx + i) * (right // 2))
                    res1 += (diskIdx + i) * (right // 2)
                diskIdx += spaceLeft
                notMovedRight -= spaceLeft
                left += 1
            elif spaceLeft >= notMovedRight:
                # move everything from right to left, but still place at the latter
                for i in range(notMovedRight):
                    # print((diskIdx + i) * (right // 2))
                    res1 += (diskIdx + i) * (right // 2)
                diskIdx += notMovedRight
                right -= 2
                if spaceLeft > notMovedRight:
                    spaceLeft -= notMovedRight
                else:
                    left += 1
                notMovedRight = int(disk[right])
    return res1

def sparseChecksum(L):
    res = 0
    for _, startIdx, files in L:
        for fileID, space in files:
            for i in range(space):
                res += (startIdx + i) * fileID
            startIdx += space
    return res


def softFragment(disk):
    permanentFiles, emptySlots = [], []
    # both above are lists of slots
    # each slot has three data points: [emptySpace, startIdx, files]
    # files is a list of tuples (fileID, size)
    diskIdx = 0
    for i, size in enumerate(disk):
        if i % 2 == 0:
            permanentFiles.append([0, diskIdx, [(i//2, int(size))]])
        else:
            emptySlots.append([int(size), diskIdx, []])
        diskIdx += int(size)
    
    moved = set()
    fileID = len(disk)//2
    for size in disk[-1::-2]:
        for slot in emptySlots:
            # slot has three data points: [emptyspace, startIdx, files]
            # files is a list of tuples (fileID, size)
            if slot[0] >= int(size):
                slot[0] -= int(size)
                slot[2].append((fileID, int(size)))
                moved.add(fileID)
                break
        fileID -= 1
    permanentFiles = [slot for slot in permanentFiles if slot[2][0][0] not in moved]
    res = sparseChecksum(permanentFiles) + sparseChecksum(emptySlots)
    return res
            



def main():
    # even parity of index = file content
    # odd parity of index = free space
    # ceil(n/2) is the no of files 
    with open("small_input9.txt") as file:
        for row in file:
            disk = row.strip()
    
    res1 = hardFragment(disk)

    # 8593662006385 too high
    res2 = softFragment(disk)

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    # print(checksum('0099811188827773336446555566'))
    # print('----')
    main()
