

def count_power_groups(stations, lines):
    """
    Count how many connected groups of power stations exist.

    stations: list of station name strings.
    lines: list of (a, b) pairs, meaning there is an undirected line between a and b.

    Return: integer number of connected components (groups) in the network.
    """

    # Build adjacency list
    graph = {station: [] for station in stations}
    for a, b in lines:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    def dfs(station):
        stack = [station]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    count = 0
    for station in stations:
        if station not in visited:
            dfs(station)
            count += 1
    return count


if __name__ == "__main__":
    # Optional manual test
    stations = ["A", "B", "C", "D"]
    lines = [("A", "B"), ("B", "C")]
    print(count_power_groups(stations, lines))  # expected 2
