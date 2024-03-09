import sys
import os
import networkx as nx
import random

""" Check the validity of a given file
    :param inputFile: The file path
"""
def check_validity_file(inputFile):
    if inputFile == None :
        sys.exit("> No given file.")
    elif not os.path.exists(inputFile):
        sys.exit("> The file \""+inputFile+"\" does not exists.")

""" Create a directed graph with random edges and edge capacity with
    a given number of nodes
    :param nbNodes: Number of nodes wanted

    :returns: The name of the file with the random graph
"""
def create_random_graph(nbNodes):
    if (nbNodes < 1):
        sys.exit("> The number of nodes has to be > 1.")

    #Create a random graph with the number of nodes given
    graph = nx.DiGraph()
    graph.add_nodes_from(range(1, nbNodes+1))

    for node in list(graph.nodes):
        ProbabilityEdge = random.randint(1, 2)
        for i in range(1, ProbabilityEdge+1):
            connectedNode = random.choice(list(graph.nodes))
            #Choose a new node to connect to if the one chosen was the same, already had the same edge
            #or had an edge going the other way (v,u)
            while(node == connectedNode or (node, connectedNode) in list(graph.edges) or (connectedNode, node) in list(graph.edges)):
                connectedNode = random.choice(list(graph.nodes))
            graph.add_edge(node, connectedNode)

    #Create a file named example_random_graph.txt or re-write over it
    #with the new graph made
    fileName = "example_random_graph.txt"
    file = open(fileName, "w")

    for (x, y) in list(graph.edges):
        file.write(str(x) + ' ' + str(y) + ' ' + str(random.randint(1,50)))
        file.write("\n")

    file.close()
    return fileName
