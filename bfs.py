"""Breadth First Search"""

graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def bfs(graph: dict, source_node: str) -> None:
    """Breadth First Search on graph and print nodes"""

    queue = [source_node]

    while queue:
        current_node = queue.pop(0)

        print(current_node)

        for node in graph[current_node]:
            queue.append(node)


bfs(graph, 'a')