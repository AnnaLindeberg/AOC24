# Day 5 of Advent of Code 2024: Print Queue
# https://adventofcode.com/2024/day/5
from collections import deque

def correctOrder(graph, pageOrder):
    for idx, page in enumerate(pageOrder):
        for otherPage in pageOrder[idx+1:]:
            if otherPage in graph and page in graph[otherPage]:
                return False
    return True

def graphSort(graph, pages):
    pages = set(pages)
    smallerGraph = {key: value.intersection(pages) for key, value in graph.items() if key in pages}
    for page in pages:
        if page not in smallerGraph:
            smallerGraph[page] = set()
    
    res = deque()
    while smallerGraph:
        elt = min(smallerGraph, key=lambda k: len(smallerGraph[k]))
        res.appendleft(elt)
        del smallerGraph[elt]
        for afterThis in smallerGraph.values():
            if elt in afterThis:
                afterThis.remove(elt)
    return list(res)



def main():
    graph = {}
    res1, res2 = 0, 0
    with open("input5.txt") as file:
        inFirstPart = True
        for row in file:
            row = row.strip()
            if row == '':
                inFirstPart = False
                continue
            if inFirstPart:
                parent, child = row.split('|')
                if parent in graph:
                    graph[parent].add(child)
                else:
                    graph[parent] = {child}
            else:
                pages = row.split(',')
                if correctOrder(graph, pages):
                    # print(pages, 'OK')
                    res1 += int(pages[len(pages)//2])
                else:
                    pages = graphSort(graph, pages)
                    res2 += int(pages[len(pages)//2])
    print(graph)
    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
