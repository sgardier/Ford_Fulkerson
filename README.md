# Ford-Fulkerson algorithm in Python
![Release](https://img.shields.io/badge/Release-v1.0-blueviolet?style=for-the-badge)
![Language](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Python project developped for the course of Graph theory (MATH0499) given by Pr. Rigo, ULiège.<br>
The final mark for this project is 18/20.

<div style="display: flex; justify-content: space-around; align-items: center;">
  <img src="ressources/flow1.png" alt="Encrypted pixel art of a city, noisy image" style="width: 60%;"/>
</div>

The Ford-Fulkerson algorithm is a graph algorithm used to determine the maximum flow from a source node to a sink node. It can also be used to calculate if a minimum flow can flow through an entire network.

Using the -g option (see [Examples of usages](#examples-of-usage)), you can visualize the flow in the graph.
The lighter the color of an edge, the more saturated it is.


## Summary
1. [Required Modules](#required-modules)
2. [Project structure](#project-structure)
3. [Examples of usages](#examples-of-usage)
4. [Technical Specifics](#technical-specifics)
5. [Credits](#credits)

## Required modules
- NetworkX [https://pypi.org/project/networkx/](https://pypi.org/project/networkx/)
- Matplotlib
- Pylab

## Project structure
- ./
  - main.py: Main script
  - ford_fulkerson.py: Script containing the Ford-Fulkerson algorithm and pre-processing functions for loading files into Graph() objects
  - display.py: Script for displaying graphs via matplotlib
  - utils.py: Script for creating random graphs of any size

## Examples of usage
1. **Finding the maximum flow from s to t in an existing file**
    ```console
    python3 main.py -i filename.txt -s s -t t
    ```

2. **Finding the maximum flow from s to t in an existing file and displaying the residual graph in a window**
    ```console
    python3 main.py -i filename.txt -s s -t t -g
    ```

3. **Finding the maximum flow from multiple sources to t in an existing file**
    ```console
    python3 main.py -i filename.txt -s "s_1 s_2 s_3 s_n" -t t
    ```

4. **Finding the maximum flow from multiple sources to multiple sinks in an existing file**
    ```console
    python3 main.py -i filename.txt -s "s_1 s_2 s_3 ... s_n" -t "t_1 t_2 ... t_k"
    ```

5. **Finding the maximum flow from s to t in a randomly generated file with n vertices**
    ```console
    python3 main.py -r n -s s -t t
    ```

## Technical specifics
- Randomly generated graphs are systematically stored in ./example_random_graph.txt
- Graphs are stored in Edge List files (see [NetworkX Edge List documentation](https://networkx.org/documentation/stable/reference/readwrite/edgelist.html))

## Credits
- [Simon Gardier](https://github.com/sgardier) (Co-author)
- Camille Trinh (Co-author)
