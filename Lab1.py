from collections import deque

def exists_path(g, src, dst):
    queue = deque([src])
    seen = {src}
    while queue:
        node = queue.popleft()
        if node == dst:
            return True
        for nbr in g[node]:
            if nbr not in seen:
                seen.add(nbr)
                queue.append(nbr)
    return False

graph = {
    1: [2],
    2: [1, 5],
    5: [2],
    3: [6],
    6: [3, 4, 7],
    4: [6, 7],
    7: [6, 4]
}

start = int(input("Enter the start node: "))
end = int(input("Enter the end node: "))

print("True" if exists_path(graph, start, end) else "False")
