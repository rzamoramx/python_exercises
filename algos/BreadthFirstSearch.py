
from collections import defaultdict, deque


class BreadthFirstSearch:
    def shortest_path(self, graph, start, end):
        # Create a queue for BFS
        queue = deque()
        # Create a dictionary to store parent-child relationships
        parent = {}
        # Initialize the queue with the start node
        queue.append(start)
        parent[start] = None

        while queue:
            current_node = queue.popleft()

            # If we've reached the end node, reconstruct and return the path
            if current_node == end:
                path = []
                while current_node is not None:
                    path.insert(0, current_node)
                    current_node = parent[current_node]
                return path

            # Explore neighbors
            for neighbor in graph[current_node]:
                if neighbor not in parent:
                    parent[neighbor] = current_node
                    queue.append(neighbor)

        # If no path exists from start to end
        return None
