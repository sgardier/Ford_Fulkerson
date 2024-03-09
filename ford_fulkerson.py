import networkx as nx
import sys

import utils

""" Find a path between a given souce and a sink and fill pathTaken with the path taken

    :param graph: The graph
    :param source: The source node (example for the node 2, it is the string : '2')
    :param sink: The sink node
    :param pathTaken: The path taken from source to sink

    :returns:   True if there is a path between source and sink
                False otherwise
"""
def edmonds_karp_bfs(graph, source, sink, pathTaken):
    visited = [False]*(graph.number_of_nodes())
    queue = []
    queue.append(source)
    visited[source-1] = True

    while queue:
        currentNode = queue.pop(0)
        for neighborNode in graph.neighbors(currentNode):
            if visited[neighborNode-1] == False and graph[currentNode][neighborNode]['residual_capacity'] > 0:
                queue.append(neighborNode)
                visited[neighborNode-1] = True
                pathTaken[neighborNode-1] = currentNode
                if neighborNode == sink:
                    return True

    return False

""" Find the maximum flow between two nodes (the source and the sink) in an oriented graph

    :param graph: The graph
    :param source: The source node (example for the node 2, it is the string : '2')
    :param sink: The sink node

    :returns: The maximum flow between the source and the sink
"""
def ford_fulkerson_max_flow(graph, source, sink):

    #Create a new variable in each edge of the graph : their residual capacity
    capacities = nx.get_edge_attributes(graph, 'capacity')
    nx.set_edge_attributes(graph, capacities, "residual_capacity")

    #List filled by edmonds_karp_bfs() with the trace of the path taken. 
    #Each node at i, an index, is the predecessor of the node represented by 'i'.
    #Example for pathTaken = [None, None, '1', '2'] :
    #   The value at index 2 is '1', it means that the path (from source to sink) has passed by node '1' 
    #   and then by node '2', in other words '1' is the predecessor of '2' in this path.
    #   The full path is : node 1 -> node 2 -> node 3
    pathTaken = [None]*(graph.number_of_nodes())

    maxFlow = 0

    while edmonds_karp_bfs(graph, source, sink, pathTaken):
        currentPathFlow = float("Inf")
        currentNode = sink
        #find the minimum flow in the current path by going up the path
        while currentNode != source:
            prevNode = pathTaken[currentNode-1]
            currentPathFlow = min(currentPathFlow, graph[prevNode][currentNode]['residual_capacity'])
            currentNode = prevNode

        maxFlow += currentPathFlow

        #update the residual capacities of the edges
        currentNode = sink
        while currentNode != source:
            actualResidualCapacity = graph[pathTaken[currentNode-1]][currentNode]['residual_capacity']
            graph[pathTaken[currentNode-1]][currentNode]['residual_capacity'] = actualResidualCapacity - currentPathFlow
            currentNode = pathTaken[currentNode-1]

    return maxFlow

""" Add a super source to a graph and link it to the sources with an infinite capacity

    :param graph: The graph
    :param sources: The sources node

    :returns: The newly created super source linked to the sources
"""
def add_super_source(graph, sources):

    superSource = 0
    graph.add_node(superSource)

    for source in sources:
        graph.add_edge(superSource, source)
        graph[superSource][source]['capacity'] = float("Inf")

    return superSource

""" Add a super sink to a graph and link it to the sinks with an infinite capacity

    :param graph: The graph
    :param sinks: The sinks node

    :returns: The newly created super sink linked to the sinks
"""
def add_super_sink(graph, sinks):

    superSink = max(graph.nodes()) + 1
    graph.add_node(superSink)

    for sink in sinks:
        graph.add_edge(sink, superSink)
        graph[sink][superSink]['capacity'] = float("Inf")

    return superSink

""" Check if a node is in a given graph, exit the program in not
    :param graph: The graph
    :param node: The node
"""
def check_node_in_graph(graph, node):
    if not node in list(graph.nodes()):
        sys.exit("> Node '"+str(node)+"' isn't in the graph")
    return node

""" Split a string representing nodes and put them in a list
    :param graph: The graph
    :param nodesString: The string representing the nodes
    :nodesListName: The name of the nodes string

    :return: The nodes list
"""
def split_nodes_string(graph, nodesString):
    nodesList = []
    #Check the string validity
    if nodesString == None:
        sys.exit("> '"+nodesString+"' is invalid")
    for node in nodesString.split():
        nodesList.append(check_node_in_graph(graph, int(node)))
    return nodesList

""" Load a graph from a given file and prepare it to be used in the Ford-Fulkerson algorithm
    :param inputFile: The file representing the graph
    :param sourceString: The string representing the source
    :param sinkString: The string representing the sink

    :return: The prepared graph, the source and the sink
"""
def prepare_graph_for_max_flow_finding(inputFile, sourceString, sinkString):
    utils.check_validity_file(inputFile)

    if sourceString is None:
        sys.exit("> Empty source")
    if sinkString is None:
        sys.exit("> Empty sink")

    try:
        graph = nx.read_edgelist(inputFile, create_using=nx.DiGraph(), nodetype=int, data=(('capacity', int), ))
    except:
        sys.exit("Please provide an edgelist file as argument.\n(Doc : https://networkx.org/documentation/stable/reference/readwrite/edgelist.html#format)")

    source = None
    sink = None

    if len(sourceString.split()) > 1:
        source = add_super_source(graph, split_nodes_string(graph, sourceString))
    else:
        source = check_node_in_graph(graph, int(sourceString))
    if len(sinkString.split()) > 1:
        sink = add_super_sink(graph, split_nodes_string(graph, sinkString))
    else:
        sink = check_node_in_graph(graph, int(sinkString))

    return graph, source, sink

""" Remove the super source / super sink if there is any in the graph provided
    :param graph: The graph in which remove the node(s)
    :param sourceString: The string representing the source node (or the list of source nodes)
    :param sourceString: The string representing the sink node (or the list of sink nodes)
    
    :return: The modified graph
"""
def prepare_graph_for_display(graph, sourceString, source, sinkString, sink):
    if len(sourceString.split()) > 1:
        graph.remove_node(source)
    if len(sinkString.split()) > 1:
        graph.remove_node(sink)
    return graph
