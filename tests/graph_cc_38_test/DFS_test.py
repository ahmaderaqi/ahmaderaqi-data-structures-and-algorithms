import pytest
from code_challenges.graph.graph import Graph
from code_challenges.graph.node import Node
# Test class for pytest
class TestDepthFirst:
    def test_depth_first(self):
        # Create a graph and add nodes and edges
        graph = Graph()
        node_a = graph.add_node('A')
        node_b = graph.add_node('B')
        node_c = graph.add_node('C')
        node_d = graph.add_node('D')

        graph.add_edge(node_a, node_b)
        graph.add_edge(node_b, node_c)
        graph.add_edge(node_c, node_d)

        # Capture the output of the function to test the printed result
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the depth_first function with the starting node 'A'
        graph.depth_first(node_a)

        # Reset the standard output
        sys.stdout = sys.__stdout__

        # Get the printed output and check if it matches the expected result
        result = captured_output.getvalue()
        assert result.strip() == 'A B C D'

    def test_depth_first_single_node(self):
        # Test a graph with only one node
        graph = Graph()
        node_a = graph.add_node('A')

        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        graph.depth_first(node_a)

        sys.stdout = sys.__stdout__
        result = captured_output.getvalue()
        assert result.strip() == 'A'

    def test_depth_first_empty_graph(self):
        # Test an empty graph
        graph = Graph()

        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        graph.depth_first('A')  # Call with a non-existing node

        sys.stdout = sys.__stdout__
        result = captured_output.getvalue()
        assert result.strip() == 'this node does not exist'

    def test_depth_first_invalid_start_node(self):
        # Test with an invalid starting node
        graph = Graph()
        node_a = graph.add_node('A')
        node_b = graph.add_node('B')

        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        graph.depth_first(node_b)  # Call with a node that does not exist in the graph

        sys.stdout = sys.__stdout__
        result = captured_output.getvalue()
        assert result.strip() == 'this node does not exist'


# Run the pytest when executing the script directly
if __name__ == "__main__":
    import pytest
    pytest.main()
