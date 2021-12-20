# import string
from collections import defaultdict, deque
# from functools import partial
from pathlib import Path

# import networkx as nx
# from matplotlib import pyplot


if __name__ == "__main__":
    # caves = [
    #     "start-A",
    #     "start-b",
    #     "A-c",
    #     "A-b",
    #     "b-d",
    #     "A-end",
    #     "b-end",
    # ]
    # caves = [
    #     "dc-end",
    #     "HN-start",
    #     "start-kj",
    #     "dc-start",
    #     "dc-HN",
    #     "LN-dc",
    #     "HN-end",
    #     "kj-sa",
    #     "kj-HN",
    #     "kj-dc",
    # ]
    input_file = Path(__file__).parent / Path("p1_input")
    caves = input_file.open().readlines()
    caves = map(str.strip, caves)


    # string_split = partial(str.split, sep="-")
    # caves = map(string_split, caves)

    # # Step 1 : Build the graph
    # graph = nx.DiGraph()

    # for start, end in caves:
    #     if end in graph.nodes:
    #         start, end = end, start
    #     if end == "start":
    #         start, end = end, start
    #     graph.add_edge(start, end)

    # # Step 2 : Inspect the graph for all possible paths
    # # The first node to inspect is "start"
    # start = "start"
    # # We need to build a list of all possible paths
    # paths = []

    # paths = nx.all_simple_paths(graph, "start", "end")

    # print(list(paths))

    def trace(map, dbls):
        ct = 0
        tracker = deque([("start", set(["start"]), False)])
        while tracker:
            p, seen, visited = tracker.popleft()
            if p == "end":
                ct += 1
                continue
            for c in map[p]:
                if c not in seen:
                    seen_cp = set(seen)
                    if c.islower():
                        seen_cp.add(c)
                    tracker.append((c, seen_cp, visited))
                elif c in seen and not visited and c not in ["start", "end"] and dbls:
                    tracker.append((c, seen, c))
        return ct



    map = defaultdict(list)
    for line in caves:
        p, c = line.split("-")
        map[p].append(c)
        map[c].append(p)
    print(f"Part 1: {trace(map, False)}")
    print(f"Part 2: {trace(map, True)}")