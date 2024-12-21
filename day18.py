# Day 18 of Advent of Code 2024: RAM Run
# https://adventofcode.com/2024/day/18
import networkx as nx

def part1(coords, dimensions):
    G = nx.grid_graph(dim=dimensions)
    for coord in coords:
        G.remove_node(coord)
    return nx.shortest_path_length(G, source=(0,0),target=(dimensions[0]-1, dimensions[1]-1))

def part2(coords, dimensions):
    G = nx.grid_graph(dim=dimensions)
    for coord in coords:
        G.remove_node(coord)
        try:
            nx.shortest_path_length(G, source=(0,0),target=(dimensions[0]-1, dimensions[1]-1))
        except nx.NetworkXNoPath:
            return coord
            

def main():
    res1, res2 = None, None
    coords1, coords2 = [], []
    # rows2read, dim = 12, (7,7)
    rows2read, dim = 1024, (71,71)
    with open("input18.txt") as file:
        for byte, row in enumerate(file):
            coord = tuple(map(int, row.strip().split(',')))
            if byte < rows2read:
                coords1.append(coord)
            coords2.append(coord)
    res1 = part1(coords1, dim)
    res2 = part2(coords2, dim)

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
