import pytest
import networkx as nx
import pgraph as pg


@pytest.fixture(scope="function")
def G():
    G = nx.random_geometric_graph(50, 0.125)
    nx.set_node_attributes(G, 3, "prop")

    return G


def test_plot_graph(G):

    pg.plot_graph(G)

    assert True


def test_plot_graph_fixed_size_color(G):

    pg.plot_graph(G, sizing_method="static", color_method="#ffffff")

    assert True


def test_plot_graph_property(G):

    pg.plot_graph(G, sizing_method="prop", color_method="prop")

    assert True


def test_plot_graph_text(G):

    pg.plot_graph(G, node_text=["prop"])

    assert True


def test_plot_graph_size_list(G):

    size = []

    for node in G.nodes():
        size.append(3)

    pg.plot_graph(G, sizing_method=size)

    assert True


def test_plot_graph_color_list(G):

    color = []

    for node in G.nodes():
        color.append(3)

    pg.plot_graph(G, color_method=color)

    assert True
