import sys
import getopt
import os

import utils
import ford_fulkerson
import display

def main(argv):
    inputFile = None
    outputFile = None
    sourceString = None
    sinkString = None
    displayGraph = False
    nbNode = None
    randomGraph = False

    try:
        opts, args = getopt.getopt(argv, "hi:s:t:gr:")
    except getopt.GetoptError:
        sys.exit("> Error while retrieving the program args\n> Please use the program as follow : python3 "+os.path.basename(__file__)+" (-i <inputfile>) -s <sourcenode> -t <sinknode> (-g) (-r <numberofnodes>)")

    for opt, arg in opts:
        if opt == '-h':
            sys.exit("> [Maximum flow finder by Trinh Camille and Gardier Simon]\n> ULiege - Computer sciences B2 - MATH0499 project\n> December 2021\n> Here is how to use the program : python3 "+os.path.basename(__file__)+" (-i <inputfile>) -s <sourcenode(s)> -t <sinknode(s)> (-g) (-r <numberofnodes>)")
        elif opt in ("-i"):
            inputFile = arg
        elif opt in ("-s"):
            sourceString = arg
        elif opt in ("-t"):
            sinkString = arg
        elif opt in ("-g"):
            displayGraph = True
        elif opt in ("-r"):
            if(arg.isdigit()):
                nbNode = int(arg)
                randomGraph = True
            else:
                sys.exit("> The number of nodes is not being given in int.")
        else:
            sys.exit("> Unknow option", opt)

    if(inputFile != None and randomGraph == True):
        sys.exit("> You cannot create a random graph while giving a pre-existing one.")
    elif(randomGraph):
        inputFile = utils.create_random_graph(nbNode)

    graph, source, sink = ford_fulkerson.prepare_graph_for_max_flow_finding(inputFile, sourceString, sinkString)

    maxFlow = ford_fulkerson.ford_fulkerson_max_flow(graph, source, sink)

    print("> The maximum flow from",sourceString,"to",sinkString,"is",maxFlow)

    if displayGraph:
        graph = ford_fulkerson.prepare_graph_for_display(graph, sourceString, source, sinkString, sink)
        display.display_graph(graph, inputFile, sourceString, sinkString, maxFlow)

if __name__ == "__main__":
   main(sys.argv[1:])
