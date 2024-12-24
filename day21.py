# Day 21 of Advent of Code 2024: Keypad Conundrum
# https://adventofcode.com/2024/day/21
import networkx as nx
import re
from itertools import pairwise

class Keypad:
    def __init__(self, rows, cols, delNode, buttonLabels, dirW=None):
        if dirW is None:
            # directionWeights = {'<':4,'^':2,'>':2,'v':3}
            directionWeights = {'<':1,'^':1,'>':1,'v':1}
        else:
            directionWeights = dirW
        self.memory = {}
        G = nx.DiGraph(nx.grid_2d_graph(cols, rows))
        G.remove_node(delNode)
        for node in G:
            G.nodes[node]['button'] = buttonLabels[node]
        for edge in G.edges:
            u, v = edge
            if u[0] < v[0]:
                G.edges[edge]['press'] = '>'
                G.edges[edge]['weight'] = directionWeights['>']
            elif u[0] > v[0]:
                G.edges[edge]['press'] = '<'
                G.edges[edge]['weight'] = directionWeights['<']
            elif u[1] > v[1]:
                G.edges[edge]['press'] = '^'
                G.edges[edge]['weight'] = directionWeights['^']
            else:
                G.edges[edge]['press'] = 'v'
                G.edges[edge]['weight'] = directionWeights['v']
        self.G = nx.relabel_nodes(G, buttonLabels)

    def seqToPush(self, start, end):
        # output sequence of '<>^v' to traverse (shortest way) from start to end, then and 'A' to push end-button
        if (start, end) in self.memory:
            return self.memory[(start, end)]
        
        path = nx.shortest_path(self.G, start, end, weight='weight')
        res = ''
        for edge in zip(path, path[1:]):
            res += self.G.edges[edge]['press']
        res = res + 'A'
        self.memory[(start,end)] = res
        return res
    
    def pushAll(self, toBePressed):
        res = ''
        for s, e in pairwise('A'+toBePressed):
            res += self.seqToPush(s, e)

        res = self.cleanUp(res)
        return res
    

    def cleanUp(self, strokes):
        # strokes = '<vA<AA>^>AvAA<<^<A>A<v<A^>^^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA^<^A>A'
        # between A's want no >^> or ^>^ etc patterns
        def caretRep(matchobj):
            # s = list(matchobj[0])
            # s.sort(reverse=True)
            # return "".join(s)
            s = matchobj[0]
            res = '>'*s.count('>') + 'v'*s.count('v') + '^'*s.count('^') + '<'*s.count('<')
            return res
        # return re.sub(r'\^+<+\^+|\^+>+\^+|<+\^+<+|>+\^+>+|v+<+v+|v+>+v+|<+v+<+|>+v+>+', caretRep, strokes)
        return re.sub(r'[<>\^v]*', caretRep, strokes)

        

class numericKeypad(Keypad):
    def __init__(self):
        
        buttonLabels = {(0,0):'7', (1,0):'8', (2,0):'9', (0,1):'4',(1,1):'5',(2,1):'6',(0,2):'1',(1,2):'2',(2,2):'3',(1,3):'0', (2,3):'A'}
        delNode = (0,3)
        super().__init__(4, 3, delNode, buttonLabels)
        

class dirKeypad(Keypad):
    def __init__(self, dirW=None):
        buttonLabels = {(1,0):'^', (2,0):'A', (0,1):'<',(1,1):'v',(2,1):'>'}
        delNode = (0,0)
        super().__init__(2, 3, delNode, buttonLabels, dirW)

def part1(codes):
    res = 0
    num_keypad = numericKeypad()
    dkp1, dkp2 = dirKeypad(), dirKeypad({'<':1,'^':1,'>':1,'v':1})
    for code in codes:
        s1 = num_keypad.pushAll(code)
        s2 = dkp1.pushAll(s1)
        keystrokes = dkp2.pushAll(s2)
        # print(f'code {code} of complexity {len(keystrokes)}*{int(code[:-1])}')
        res += len(keystrokes)*int(code[:-1])
    return res

def main():
    res1, res2 = None, None
    codes = []
    with open("small_input21.txt") as file:
        for row in file:
            codes.append(row.strip())
    res1 = part1(codes)

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    # nk = numericKeypad()
    # dk = dirKeypad()
    # dk2 = dirKeypad()
    # step1 = nk.pushAll('029A')
    # step2 = dk.pushAll(step1)
    # print(step1)
    # print(step2)
    # print(dk2.pushAll(step2))

    main()