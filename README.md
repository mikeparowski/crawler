# Crawler
  - Our final project for Fall 2016 Data Structures is a .html visualization of a web crawler that 
  operates on the nd.edu domain. We used a python program, crawler.py, to create an **adjacency 
  list** from the link tags on each webpage. We ran crawler.py with a depth of 1 and 2 and 
  stored the results in two text files, a_list_large.txt and a_list_small.txt respectively. After 
  storing these results, we ran a simple server, server.py, and an .html page, index.html, that
  uses javascript and jquery to create a interactive, navigable web graph. This graph 
  displays a url on the center bubble with all links on the center's webpage surrounding it.
  In addition, we added a **shortest path** computation and visualization below the web 
  visualization using Dijkstra's algorithm.

## crawler.py
### main contributor : Michael Parowski
  - 

## index.html
### main contributor : Jasmine Walker
### assistant : Luigi Grazioso
  - This is the graphic representation of the adjacency list and shortest path between nodes. It
  stores the adjacency list in a node of nodes called "nodes". Each key stored in "nodes" stores
  the unedited adjacency list from the textfile, and a "clean" adjacency list that only holds
  nodes that are also in the main adjacency list. Our code uses the main adjacency list as the 
  graphical representation, but we can easily switch to the clean list by editing the "usingList" 
  global variable in the script. Graphically, the bubbles that are red are unclickable - they are 
  a leaf node, and have no branching nodes when clicked, making it impossible to navigate away 
  from. The light-blue bubbles have at least one node included in it, so are made clickable. The
  web outputs a graph that often exceeds the divider's margins, so we added a clickable navigator
  that allows the user to scroll up, down, left, and right of the graph in order to see the 
  entirety of the web graph.
  - On the lower half of the .html page, we use Dijkstra's algorithm using the specified adjacency 
  list to create a visualization of the shortest bubble path from user-specified start to finish. 
  This graph takes user input in the text-boxes below the graph, and handles errors such as having
  no path or having no end or start node by outputting a bubble that displays the error gracefully.