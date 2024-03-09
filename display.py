import matplotlib.pyplot as plt;
import networkx as nx
import sys
import pylab

""" Generate the edges label
    :param graph: The graph containing the edges
    :return: The lost of labels
"""
def edges_labels(graph):
    labels_dic = {}
    for edge in graph.edges:
        edgeData = graph.get_edge_data(edge[0], edge[1])
        labels_dic[edge] = (str(edgeData["capacity"] - edgeData["residual_capacity"])+"/"+str(edgeData["capacity"]))
    return labels_dic

""" Generate the edges label
    :param graph: The graph containing the edges
    :return: The lost of labels
"""
def nodes_labels(graph):
    labels_dic = {}
    for node in graph.nodes:
        labels_dic[node] = node
    return labels_dic

def edges_color_list(graph):
    l = []
    for edge in graph.edges:
        edge_data = graph.get_edge_data(edge[0], edge[1])
        capacity = edge_data["capacity"]
        flow = capacity - edge_data["residual_capacity"]
        pourcentage = flow / capacity
        l.append(pourcentage)
    return l

""" Display in a window the given graph
    :param graph: the graph to display
    :param maxFlow: the maximum flow of the network
"""
def display_graph(graph, fileName, source, sink, maxFlow):    
    # Set the background color to black
    plt.figure(facecolor='skyblue')

    try:
        if graph.number_of_nodes() > 30 or graph.number_of_edges() > 30:
            pos = nx.spring_layout(graph)
        else:
            pos = nx.shell_layout(graph)
    except:
        sys.exit("> Unable to layout the given graph")

    #Nodes
    nxNodes = nx.draw_networkx_nodes(graph, pos, node_size=300, node_color="indigo")
    nodesLabels = nodes_labels(graph)
    nxNodesLabels = nx.draw_networkx_labels(graph, pos, nodesLabels, font_color="white", font_size=10)

    #Edges
    cmap = plt.cm.plasma
    edges_color = edges_color_list(graph)
    nxEdges = nx.draw_networkx_edges(graph, pos, arrowstyle="->", width=4, alpha=0.8, edge_cmap=cmap,  edge_color=edges_color)
    edgesLabels = edges_labels(graph)
    nxEdgesLabels = nx.draw_networkx_edge_labels(graph, pos, edge_labels=edgesLabels, font_size=9, rotate=False, label_pos=0.6)

    #Remove the ugly black rectangle
    ax = plt.gca()
    ax.set_axis_off()

    pylab.gcf().canvas.manager.set_window_title(fileName+' - Maximum flow from '+source+' to '+sink+' is '+str(maxFlow))
    
    plt.show()
