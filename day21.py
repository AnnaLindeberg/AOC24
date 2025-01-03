# Day 21 of Advent of Code 2024: Keypad Conundrum
# https://adventofcode.com/2024/day/21
import networkx as nx
from itertools import pairwise, combinations

class Keypad:
    def __init__(self, rows, cols, delNode, buttonLabels):
        self.memory = {}
        G = nx.DiGraph(nx.grid_2d_graph(cols, rows))
        G.remove_node(delNode)

        for edge in G.edges:
            u, v = edge
            if u[0] < v[0]:
                G.edges[edge]['press'] = '>'
            elif u[0] > v[0]:
                G.edges[edge]['press'] = '<'
            elif u[1] > v[1]:
                G.edges[edge]['press'] = '^'
            else:
                G.edges[edge]['press'] = 'v'
        self.G = nx.relabel_nodes(G, buttonLabels)

    def seqToPush(self, start, end):
        # output sequence of '<>^v' to traverse (shortest way) from start to end, then an 'A' to push end-button
        if (start, end) in self.memory:
            return self.memory[(start, end)]
        
        path = nx.shortest_path(self.G, start, end)
        res = ''
        for edge in zip(path, path[1:]):
            res += self.G.edges[edge]['press']
        res = self.fixSteps(res, start, end)
        res += 'A'
        self.memory[(start,end)] = res
        return res
    
    def pushAll(self, result):
        res = ''
        for s, e in pairwise('A'+result):
            res += self.seqToPush(s, e)
        return res
         

class numericKeypad(Keypad):
    def __init__(self):
        buttonLabels = {(0,0):'7', (1,0):'8', (2,0):'9', (0,1):'4',(1,1):'5',(2,1):'6',(0,2):'1',(1,2):'2',(2,2):'3',(1,3):'0', (2,3):'A'}
        delNode = (0,3)
        super().__init__(4, 3, delNode, buttonLabels)
    
    def fixSteps(self, seq, start, end):
        if '^' in seq:
            # going upwards
            if start in ['0', 'A'] and end in ['7', '4', '1']:
                # must avoid blank
                res = seq.count('^')*'^' + seq.count('<')*'<'
            elif '<' in seq:
                res = seq.count('<')*'<' + seq.count('^')*'^'
            else:
                res = seq.count('^')*'^' + seq.count('>')*'>'
        else:
            # going downwards
            if start in ['7', '4', '1'] and end in ['0', 'A']:
                # must avoid blank
                res = seq.count('>')*'>' + seq.count('v')*'v'
            elif '<' in seq:
                res = seq.count('<')*'<' + seq.count('v')*'v'
            else:
                res = seq.count('v')*'v' + seq.count('>')*'>'
        return res
        

class dirKeypad(Keypad):
    def __init__(self):
        buttonLabels = {(1,0):'^', (2,0):'A', (0,1):'<',(1,1):'v',(2,1):'>'}
        delNode = (0,0)
        super().__init__(2, 3, delNode, buttonLabels)
    
    def fixSteps(self, seq, start, end):
        if '^' in seq:
            # going upwards
            if start == '<':
                # must avoid blank
                res = seq.count('>')*'>' + seq.count('^')*'^'
            elif '<' in seq:
                res = seq.count('<')*'<' + seq.count('^')*'^'
            else:
                res = seq.count('^')*'^' + seq.count('>')*'>'
        else:
            # going downwards
            if start in ['^', 'A'] and end == '<':
                # must avoid blank
                res = seq.count('v')*'v' + seq.count('<')*'<'
            elif '<' in seq:
                res = seq.count('<')*'<' + seq.count('v')*'v'
            else:
                res = seq.count('v')*'v' + seq.count('>')*'>'
        return res

def part1(codes):
    res = 0
    num_keypad = numericKeypad()
    dkp1, dkp2 = dirKeypad(), dirKeypad()
    for code in codes:
        s1 = num_keypad.pushAll(code)
        s2 = dkp1.pushAll(s1)
        keystrokes = dkp2.pushAll(s2)
        res += len(keystrokes)*int(code[:-1])
    return res

def part2(codes):
    res = 0
    num_keypad = numericKeypad()
    nums = [str(i) for i in range(10)] + ['A']
    for l,r in combinations(nums, 2):
        num_keypad.seqToPush(l,r)
        num_keypad.seqToPush(r,l)
    for n in nums:
        num_keypad.seqToPush(n,n)
    print(num_keypad.memory)

    dir_keypad = dirKeypad()
    dirs = ['<', '>', 'v','^', 'A']
    for l,r in combinations(dirs, 2):
        dir_keypad.seqToPush(l,r)
        dir_keypad.seqToPush(r,l)
    for d in dirs:
        dir_keypad.seqToPush(d,d)
    print(dir_keypad.memory)
    return res

def main():
    res1, res2 = None, None
    codes = []
    with open("input21.txt") as file:
        for row in file:
            codes.append(row.strip())
    res1 = part1(codes)
    res2 = part2(codes)

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()