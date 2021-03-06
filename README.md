# Task 3 Object-Oriented Programming
Directed Weighted Graph Algorithms, designing a graph interface in python.
* [Link to our Wiki page](https://github.com/ShauliTaragin/OOP_Ex3/wiki)
* ####Note: inorder to run our program the user must have the pygame library.
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Content</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#about-the-project">Plan and design of The Project</a></li>
    <li><a href="#Gui">GUI with pygame and manual</a></li>
    <li><a href="#the-algorithm">The Algorithm</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#UML">Uml</a></li>
    <li><a href="#languages-and-tools">Languages and Tools</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

#### Task 3 Object-Oriented Programming

***Authors : Shauli Taragin & Ido Bar***  

In this project we implemented algorithms for developing a data structure into a directional weighted graph which implements many algorithms.


We also created a Graphical User Interface to visualize any given directed weighted graph, and it's implemented methods and algorithms.

As opposed to Task 2 this task is written in python


---------

## Plan and design of The Project

Upon planning are project we would like to focus on 3 fields for which we wish to plan elaborately before we begin implementing code.
<li> Planning the main classes:</li>
We will implement a class for each interface. Our GraphAlgo and DiGraph classes will hold all the functions it implements from the interface as well as other functions which we will elaborate on in the next paragraph.
We will also implement a Node class which implements A basic node class. In the GraphAlgo class we will also create our main algorithms.
<li> Planning the method of implementation:</li>
We will create a dictionary that every key is the Node Id and the value is the Node Object.
Every NodeData will contain two dict's :1. A dict of the out edges that the current node is their source, the key of the HashMap will be the Id of the destination node and the value will be the Edge's weight.
2. A dict of the in Edges that the current node is their destination the key is the src and the weight of the edge.
The key will be the Id of the source node and the value will be the weight of the edge.
<li> Planning the dijkstra algorithm:</li>
We wanted to implement the dijkstra algorithm in the most elegant ,most efficient way possible. Obviously the dijkstra algorithm is needed for calculating the center, shortest path, and tsp methods.
So we will achieve this by creating an instance of a MinHeapDijkstra. e.g Instead of implemnting dijkstra with a priority queue we will apply the min heap data structure which we will create on the dijkstra algorithm.
<li> Laying out testing methods :</li>
Beyond testing all the implemented methods from the interface We would like to check the next methods:1. Create graph by adding nodes and edges.
2. Connect two nodes. 3. Delete node. 4. Delete edge from the graph. 5. Get the correct mode count.
6. Get the correct size of edges and the correct size of nodes.










---------

## GUI
#### We will explain about our gui as well as give a short and easy manual of how the user can use it easily.

![Screenshot](images/graph_A.png)

| *Our gui representation of the graph A5.json* |


* About our GUI :
In our display of the graph the user must create a graph(either load or create) for the GraphAlgo method, and call the plot_graph function.

The graph is represented in the following manner : 

Nodes are represented by black circles. Each node's key is written above it in blue.

Edges are represented by red lines with an arrow at the end showing the direction of the edge.

Inorder to run a gui performance for a graph of you're choice, the user must work from the main class.

The user can either create a graph by adding nodes and edges e.g. check0 or load a graph of their choice which is located in the data package.

Either way the gui implementation is called from the interface function plot_graph

![Screenshot](images/graph_check.png)
| *Our gui representation of check3 graph* |

#### Note : This graph will change everytime we call it. Since there was no geolocatoin inserted for the nodes we randomly inserted proper locations for each node. More information on how we did that can be found in our DiGraph class 

---------

## The Algorithm
***The GraphAlgoInterface interface is implemented in GraphAlgo class:***
***The GraphAlgo object contains a class member of A graph of type DiGraph inorder to activate the algorithms on.***

We will lay out our graph Theory algorithms and explain how we implemented them:

1. **init**- Initializes the graph from a json file .
2. **load_from_json**- Load from a json file a graph to work our algorithms on .
3. **save_to_json**- Saves the graph to a json file.
6. **shortestPath**- Calculates the shortest path distance between 2 given nodes.
   1. We implement this algorithm as well as the shortestpath and tsp algorithm in the following manner.
   2. In order to find the shortest path between two nodes we run the dijkstra algorithm using a data structure of Min Heap.Both these methods are implemnted in the DijkstraUsingMinHeap class
   3. Then fitting the algorithm to our data structures that we are using to represent the graph.
   4.    We hold with lists the path we took to reach the shortest distance
   2. We iterate over our lists and hold in a list the path the algorithm traveled.
   5. Finally, returning a tuple of a pair of the weight of the shortest path and the list of the path we took.
8. **Center** - Finds the shortest path (at what edges should we use the path) between 2 given nodes in the graph.   
9. **TSP**- Computes a relatively short path which visit each node in the cities List.
   1. We run the same methods as 5. With additions that we run each of the cities as a src and find in a greedy way the shortest path to travel through all the cities
   2. In this solution we also hold with arrays the path we took to reach the shortest distance.
   3. We iterate over our arrays and return in a list the path the algorithm traveled.
5. **isConnected** - Altough this function is not part of the interface we implemented it inorder to help our other algorithms check whether the graph is strongly connected.
   1. We implemented this algorithm by running a bfs on the graph. Then traversing the graph. And then another bfs.
   2. Then we iterated through all the nodes in the graph if we find that some node has not been visited we know the graph is not connected.





---------
<!-- results -->
## Results

#### For our enhanced comparison between java and python results please visit our wiki page for this project.

These are our best Results. The computer which ran this program is a MacBook with 16GB ram , Macintosh startup disk , 8-core CPU (4 performance and 4 efficiency)
:

|Algorithms|Small graph up to 1000 nodes|10000 nodes|100000 nodes|1000000 nodes|
|---------|---------|---------|---------|---------|
|**Get Graph**|10 ms|160 ms|1 second|Not enough ram to create |
|**load_from_json**|20 ms|160 ms|1.2 seconds|Not enough ram to create |
|**save_to_json**|70 ms|400 ms|10 seconds|Not enough ram to create
|**shortestPath**|50 ms|440 ms|10 seconds|Not enough ram to create
|**center**|7 seconds|16 minutes|Time Out|Not enough ram to create
|**tsp**|for 30 nodes in node list in 1000 graph - 1.50 minutes|for 30 nodes in node list in 10000 graph - 120 minutes|Time out|Not enough ram to create


As you can see our results after analyzing the code,our code is efficient. Besides running in good times our tsp algorithm returns a very accurate result.

---------

## UML

![Screenshot](images/z.png)
| *Our Unified Modeling Language representation* |
---------


## Languages and Tools

  <div align="center">

 <code><img height="40" width="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png"></code> 

 <code><img height="40" height="40" src="https://jupyter.org/assets/main-logo.svg"/></code>
<code><img height="40" width="70" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/UML_logo.svg"/></code>
 <code><img height="40" width="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1024px-PyCharm_Icon.svg.png"/></code>
<code><img height="40" height="40" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png"></code>
<code><img height="40" height="40" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png"></code>
<code><img height="40" height="40" src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Pygame_logo.gif"></code>

  </div>


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Python](https://www.python.org/)
* [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language)
* [Git](https://git-scm.com/)
* [Jupyter](https://jupyter.org/)
* [Pygame](https://www.pygame.org/)
* [Git-scm](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


<!-- CONTACT -->
## Contact

Ido - [here](https://github.com/idobar1403/)

Shauli - [here](https://github.com/ShauliTaragin/)

Project Link: [here](https://github.com/ShauliTaragin/OOP_Ex3)