import pytest
import networkx as nx
import igviz as ig


@pytest.fixture(scope="function")
def G():
    G = nx.random_geometric_graph(50, 0.125)
    nx.set_node_attributes(G, 3, "prop")

    return G


def test_plot(G):

    ig.plot(G)

    assert True


def test_plot_fixed_size_color(G):

    ig.plot(G, sizing_method="static", color_method="#ffffff")

    assert True


def test_plot_property(G):

    ig.plot(G, sizing_method="prop", color_method="prop")

    assert True


def test_plot_text(G):

    ig.plot(G, node_text=["prop"])

    assert True


def test_plot_size_list(G):

    size = []

    for node in G.nodes():
        size.append(3)

    ig.plot(G, sizing_method=size)

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
