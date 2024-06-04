
from collections import defaultdict
from algos.BreadthFirstSearch import BreadthFirstSearch
import unittest


class BreadthFirstSearch_test(unittest.TestCase):
    def test_breadth_first_search(self):
        graph = defaultdict(list)
        graph['A'] = ['B', 'C', 'D']
        graph['B'] = ['A', 'E', 'F']
        graph['C'] = ['A']
        graph['D'] = ['A', 'G']
        graph['E'] = ['B']
        graph['F'] = ['B']
        graph['G'] = ['D']

        start_node = 'A'
        end_node = 'G'

        shortest_path = BreadthFirstSearch().shortest_path(graph, start_node, end_node)

        if shortest_path:
            print(f'Shortest path from {start_node} to {end_node} is: {shortest_path}')
        else:
            print(f'No path exists from {start_node} to {end_node}')
