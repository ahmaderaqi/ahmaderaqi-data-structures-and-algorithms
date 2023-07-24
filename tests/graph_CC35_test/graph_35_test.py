import pytest
from code_challenges.graph.graph import Graph
from code_challenges.graph.node import Node


@pytest.fixture
def create_graph():
    graph = Graph()
    vertex_a = graph.add_node('A')
    vertex_b = graph.add_node('B')
    vertex_c = graph.add_node('C')
    vertex_d = graph.add_node('D')
    return graph, vertex_a, vertex_b, vertex_c, vertex_d

def test_add_node(create_graph):
    graph, vertex_a, vertex_b, vertex_c, vertex_d = create_graph
    assert graph.get_vertices() == {vertex_a, vertex_b, vertex_c, vertex_d}

def test_add_edge(create_graph):
    graph, vertex_a, vertex_b, vertex_c, vertex_d = create_graph
    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_b, vertex_c, 5)
    assert graph.get_neighbors(vertex_a) == [vertex_b]
    assert graph.get_neighbors(vertex_b) == [vertex_a, vertex_c]
    assert graph.get_neighbors(vertex_c) == [vertex_b]
    assert graph.get_neighbors(vertex_d) == "does not exist"

def test_get_vertices(create_graph):
    graph, vertex_a, vertex_b, vertex_c, vertex_d = create_graph
    assert graph.get_vertices() == {vertex_a, vertex_b, vertex_c, vertex_d}

def test_get_neighbors(create_graph):
    graph, vertex_a, vertex_b, vertex_c, vertex_d = create_graph
    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_b, vertex_c, 5)
    assert graph.get_neighbors(vertex_a) == [vertex_b]
    assert graph.get_neighbors(vertex_b) == [vertex_a, vertex_c]
    assert graph.get_neighbors(vertex_c) == [vertex_b]
    assert graph.get_neighbors(vertex_d) == "does not exist"

def test_size(create_graph):
    graph, vertex_a, vertex_b, vertex_c, vertex_d = create_graph
    assert graph.size() == 4

def test_str(create_graph, capsys):
    graph, vertex_a, vertex_b, vertex_c, vertex_d = create_graph
    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_b, vertex_c, 5)
    graph_str = str(graph)
    assert f'{vertex_a} -> {vertex_b} -----> \n{vertex_b} -> {vertex_a} -----> {vertex_c} -----> \n{vertex_c} -> {vertex_b} -----> \n{vertex_d} -> ' in graph_str
