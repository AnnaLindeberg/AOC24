## Example
0,3,
1)  take regA // 2^3 and store in regA

5,4,
2) output regA % 8

3,0
3)  if regA = 0 then nothing except next opCode (which will halt program)
    else start over

## Actual computer
2,4,
1)  take regA % 8 and store in regB

1,2,
2)  take regB XOR 2 and store in regB

7,5,
3)  take regA // 2^regB and store in regC

0,3,
4)  take regA // 2^3 and store in regA

1,7,
5) take regB XOR 7 and store in regB

4,1,
6) take regB XOR regC and store in regB

5,5,
7) output regB % 8

3,0
8)  if regA = 0 then nothing except next opCode (which will halt program)
    else start over