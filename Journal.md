# GraphLab Project Journal

---

## Entry

**Date: 01/03/2026**  
**Stage / Topic: 0**  
**Time Spent: 1 hr**  
**Energy Level (1–5):**  

---

### 1. Objective Today

Today, I am going to understand the scope of the problem. This
will include basic definitions of graphs (directed/undirected and weighted/unweighted) and the adjacency matrix. Hopefully, I can get some ideas for defining the graph class.

---

### 2. Expectations Before Starting

I had encountered graphs, BFS, and Dijkstra's algorithm in a discrete maths class before.  It was a while back. But I do have
a vague impression of what the problem is about. However, it was purely mathematical. I have no clue how to represent the data structure
and implement the algorithm through coding. As for today, I think a quick skim through Wikipedia or some lecture notes would help me to refresh the basics

---

### 3. What Actually Happened

# Definitions relating to graph  
$G =(V, E)$, where $V=\\{v_1,\ldots ,v_n\\}$ is the vertex set and $E$ is the edge set. $E \subset E \times E$ where $(v_i,v_j) \in E$ if there is an edge between $v_i$ and $v_j$.  
# Adjacency matrix  
One can use the adjacency matrix $A = (a_{ij})$ to represent a graph. $a_{ij} = w$ if $(v_i, v_j) \in E$ and $w$ is the weight on the graph, and $0$ otherwise.  
- Note that $(v_i,v_j)$ and $(v_j,v_i)$ can have different weights if $G$ is directed.
- If $G$ is unweighted, then all weights are $1$ on the edges. 
- If $G$ is undirected, the adjacency matrix is symmetric
# Adjacency list
- The common solution one uses to represent a graph is to use an adjacency list. Roughly, it associates adjacency data with each vertex. The next step for me is to figure out exactly how to
represent this data structure in Python.
---

### 4. Confusion Log
None for today

---

### 5. Breakthrough (if any)

---

### 6. Code Reflection
There is no coding done today.

---

### 7. Smallest Next Step
Find out how to define adjacency lists.

---

---
## Entry

**Date: 02/03/2026**  
**Stage / Topic: 1 **  
**Time Spent: 30 mins **  
**Energy Level (1–5):**  

---

### 1. Objective Today
- Figure out how to use an adjacency list to represent a graph
- Define Graph class 

---

### 2. Expectations Before Starting
Not aiming for anything heavy today, should be a light but solid small step.
 

---

### 3. What Actually Happened
- Defined Graph class and add_edge method
- Basically, it is a dictionary with values that are a list of tuples. Each key is a vertex, and the list of tuples specifies the adjacent vertices and the weights of the connecting edges.
- Initially thought to distinguish between weighted/unweighted (for the input, includes a weighted = True/False parameter), but figured out it is not needed since we can just give weight 1 in the unweighted case.


---

### 4. Confusion Log
- I would like to integrate the use of linked lists learned in 6.006. However, it seems that using a dictionary is enough for now.

---

### 5. Breakthrough (if any)


### 6. Code Reflection
Only defined the class and a method today

---

### 7. Smallest Next Step

Figure out what BFS is

---

---
## Entry

**Date: 03/03/2026**  
**Stage / Topic: 1 **  
**Time Spent: 30 mins **  
**Energy Level (1–5):**  

---

### 1. Objective Today

---

### 2. Expectations Before Starting

 

---

### 3. What Actually Happened



---

### 4. Confusion Log


---

### 5. Breakthrough (if any)


### 6. Code Reflection


---

### 7. Smallest Next Step



---

---
# Weekly Reflection (Every 7 Days)

### What improved this week?

### What still feels uncomfortable?

### What algorithm can I now implement confidently?

### Did frustration decrease compared to last week?

---

# Monthly Reflection

### What would have scared me one month ago but doesn’t now?

### What structural thinking improved?

### What still feels like “dark forest”?

---




