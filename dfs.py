"""Depth First Search"""

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def dfs(graph: dict, source_node: str) -> None:
    """Depth First Search on graph and print nodes"""

    stack = [source_node] 
    while stack:
        current_node = stack.pop()

        print(current_node)

        for node in graph[current_node]:
            stack.append(node)


dfs(graph, 'a')