# Day 24 of Advent of Code 2024: Crossed Wires
# https://adventofcode.com/2024/day/24
from collections import deque
import networkx as nx

class Device:
    def __init__(self, inital_vals):
        G = nx.DiGraph()
        for reg, val in inital_vals:
            G.add_node(reg)
            G.nodes[reg]['val'] = val
        self.G = G
    
    def populate(self, f_handle):
        # ntg XOR fgs -> mjb
        # ntg OR fgs -> mjb
        # ntg AND fgs -> mjb
        for row in f_handle:
            if len(row.strip()) == 0:
                continue
            left, op, right, _, source = row.strip().split()
            self.G.add_edges_from([(source, left), (source, right)])
            self.G.nodes[source]['op'] = op
    
    def valueOf(self, vertex):
        if 'val' in self.G.nodes[vertex]:
            return self.G.nodes[vertex]['val']
        if len(self.G[vertex]) != 2:
            print('nåt fel', self.G[vertex])
            return
        left, right = self.G[vertex]
        op = self.G.nodes[vertex]['op']
        match op:
            case 'OR':
                res = self.valueOf(left) or self.valueOf(right)
            case 'AND':
                res = self.valueOf(left) and self.valueOf(right)
            case 'XOR':
                res = self.valueOf(left) ^ self.valueOf(right)
            case _ :
                print("odd case!")
        
        self.G.nodes[vertex]['val'] = res
        return res

    
    def run(self):
        for v in self.G:
            if v[0] == 'z':
                self.valueOf(v)

    def output(self):
        zeds = []
        for v in self.G:
            if v[0] == 'z':
                zeds.append((v, self.G.nodes[v]['val']))
        zeds.sort(reverse=True)
        bin = ''.join(str(z[1]) for z in zeds)
        return int(bin, base=2)
    
    def all_vals(self):
        nodes = sorted(self.G)
        for n in nodes:
            if 'val' in self.G.nodes[n]:
                print(n, self.G.nodes[n]['val'])
            else:
                print(n, None)

def part2():
    pass


def main():
    res1, res2 = None, None
    reading_initials, initial_vals = True, []
    with open("small_input24.txt") as file:
        for row in file:
            row = row.strip()
            if len(row) == 0:
                reading_initials = False
                device = Device(initial_vals)
                device.populate(file)
                break
            elif reading_initials:
                l, r = row.split(': ')
                initial_vals.append((l, int(r)))

    device.run()
    # device.all_vals()
    res1 = device.output()
    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
