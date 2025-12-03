

def count_power_groups(stations, lines):
    """
    Count how many connected groups of power stations exist.

    stations: list of station name strings.
    lines: list of (a, b) pairs, meaning there is an undirected line between a and b.

    Return: integer number of connected components (groups) in the network.
    """

    # Build adjacency map for all stations
    if not stations:
        return 0

    neighbors = {s: set() for s in stations}

    # Add undirected edges for lines (ignore lines referencing unknown stations)
    for a, b in lines:
        if a in neighbors and b in neighbors:
            neighbors[a].add(b)
            neighbors[b].add(a)

    visited = set()

    def dfs(start):
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for nbr in neighbors.get(node, ()):  # safe-get
                if nbr not in visited:
                    stack.append(nbr)

    groups = 0
    for s in stations:
        if s not in visited:
            groups += 1
            dfs(s)

    return groups


if __name__ == "__main__":
    # Optional manual test
    stations = ["A", "B", "C", "D"]
    lines = [("A", "B"), ("B", "C")]
    print(count_power_groups(stations, lines))  # expected 2
