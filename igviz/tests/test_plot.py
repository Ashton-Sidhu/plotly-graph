import pytest
import networkx as nx
import igviz as ig


@pytest.fixture(scope="function")
def G():
    G = nx.random_geometric_graph(50, 0.125)
    nx.set_node_attributes(G, 3, "prop")

    return G


@pytest.fixture(scope="function")
def DG():
    # Create a directed graph (digraph) object; i.e., a graph in which the edges
    # have a direction associated with them.
    G = nx.DiGraph()

    # Add nodes:
    nodes = ["A", "B", "C", "D", "E"]
    G.add_nodes_from(nodes)

    # Add edges or links between the nodes:
    edges = [("A", "B"), ("B", "C"), ("B", "D"), ("D", "E")]
    G.add_edges_from(edges)
    return G


@pytest.fixture(scope="function")
def MG():
    G = nx.MultiGraph()
    G.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5)])

    return G


def test_plot(G):

    ig.plot(G)

    assert True


def test_plot_fixed_size_color(G):

    ig.plot(G, show_edgetext=True, size_method="static", color_method="#ffffff")

    assert True


def test_plot_property(G):

    ig.plot(G, size_method="prop", color_method="prop")

    assert True


def test_plot_text(G):

    ig.plot(G, node_text=["prop"])

    assert True


def test_plot_size_list(G):

    size = []

    for node in G.nodes():
        size.append(3)

    ig.plot(G, size_method=size)

    assert True


def test_plot_color_list(G):

    color = []

    for node in G.nodes():
        color.append(3)

    ig.plot(G, color_method=color)

    assert True


def test_plot_layout(G):

    color = []

    for node in G.nodes():
        color.append(3)

    ig.plot(G, layout="kamada")

    assert True


def test_digraph(DG):

    ig.plot(DG)

    assert True


def test_multigraph(MG):

    ig.plot(MG)

    assert True
