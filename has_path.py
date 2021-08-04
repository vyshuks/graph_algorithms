"""Check a graph contain a particular path"""


graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def has_path(graph: dict, source_node: str, destination_node: str) -> bool:
    """This function check whether graph contain a given path (source_node to destination_node)"""
    if source_node == destination_node:
        return True
    
    for node in graph[source_node]:
        if has_path(graph, node, destination_node):
            return True
    return False


print(has_path(graph, 'a', 'd'))
print(has_path(graph, 'a', 'f'))
print(has_path(graph, 'c', 'a'))