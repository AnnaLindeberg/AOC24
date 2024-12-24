# Day 23 of Advent of Code 2024: LAN Party
# https://adventofcode.com/2024/day/23
import networkx as nx

def part1(graph, tnodes):
    res = 0
    for clique in nx.enumerate_all_cliques(graph):
        if len(clique) < 3:
            continue
        if len(clique) > 3:
            break
        for v in clique:
            if v in tnodes:
                res += 1
                break
    return res

def part2(graph):
    max_clique = []
    for c in nx.find_cliques(graph):
        if len(c) > len(max_clique):
            max_clique = c
    max_clique.sort()
    return ','.join(max_clique)

def main():
    res1, res2 = None, None
    tnodes = set()
    G = nx.Graph()
    with open("input23.txt") as file:
        for row in file:
            v1, v2 = row.strip().split('-')
            tnodes.update([v for v in [v1, v2] if v[0]=='t'])
            G.add_edge(v1, v2)
    
    res1 = part1(G,tnodes)
    res2 = part2(G)

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
