## Overview

Implements a graph structure as well as three graph searching algorithms.

The program reads graph data from a text file, constructs the graph, and uses user input to find the path from one vertex to another using Greedy Best First Search, A*, and Dijkstra's Algorithm

---

## Author(s)

* **Name:** Petros Blankenstein
* **Course:** CS-351
* **Instructor:** Lucas Cordova

---

## How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/PetrosB123/cs351-project-2.git
cd cs351-assignment-3
```

### Step 2: Ensure the Data Files Exist

Check that `graph_v2.txt` exists in the project root.

Example content:

```
source,destination,highway,distance
Portland,Salem,I-5S,47
Salem,Portland,I-5N,47
Salem,Eugene,I-5S,64
Eugene,Salem,I-5N,64
Eugene,Corvallis,OR-99W-W,45
Corvallis,Eugene,OR-99W-E,45
Eugene,Bend,US-20E,130
Bend,Eugene,US-20W,130
Eugene,Crater_Lake,OR-58E,110
Crater_Lake,Eugene,OR-58W,110
Eugene,Roseburg,I-5S,70
Roseburg,Eugene,I-5N,70
Roseburg,Medford,I-5S,87
Medford,Roseburg,I-5N,87
Medford,Ashland,I-5S,15
Ashland,Medford,I-5N,15
Portland,Astoria,US-30NW,96
Astoria,Portland,US-30SE,96
Portland,Hood_River,I-84E,62
Hood_River,Portland,I-84W,62
Hood_River,The_Dalles,I-84E,20
The_Dalles,Hood_River,I-84W,20
The_Dalles,Pendleton,I-84E,126
Pendleton,The_Dalles,I-84W,126
Portland,Newport,US-20W,117
Newport,Portland,US-20E,117
Newport,Corvallis,US-20E,49
Corvallis,Newport,US-20W,49
Bend,Redmond,US-97N,16
Redmond,Bend,US-97S,16
Redmond,Madras,US-97N,33
Madras,Redmond,US-97S,33
Madras,The_Dalles,US-26NW,90
The_Dalles,Madras,US-26SE,90
Salem,Corvallis,OR-99W-S,37
Corvallis,Salem,OR-99W-N,37
Crater_Lake,Medford,OR-62SW,75
Medford,Crater_Lake,OR-62NE,75
Bend,Burns,US-20E,130
Burns,Bend,US-20W,130
Pendleton,Ontario,I-84E,142
Ontario,Pendleton,I-84W,142
Astoria,Seaside,US-101S,17
Seaside,Astoria,US-101N,17
Seaside,Tillamook,US-101S,66
Tillamook,Seaside,US-101N,66
Tillamook,Newport,US-101S,78
Newport,Tillamook,US-101N,78
Newport,Florence,US-101S,50
Florence,Newport,US-101N,50
Florence,Coos_Bay,US-101S,56
Coos_Bay,Florence,US-101N,56
Coos_Bay,Roseburg,OR-42E,87
Roseburg,Coos_Bay,OR-42W,87
```

Check that `vertices_v1.txt` exists in the project root.

Example content:

```
vertex,latitude,longitude
Portland,45.5152,-122.6784
Salem,44.9429,-123.0351
Eugene,44.0521,-123.0868
Corvallis,44.5646,-123.2620
Bend,44.0582,-121.3153
Crater_Lake,42.8684,-122.1685
Roseburg,43.2165,-123.3417
Medford,42.3265,-122.8756
Ashland,42.1946,-122.7095
Astoria,46.1879,-123.8313
Hood_River,45.7054,-121.5212
The_Dalles,45.5946,-121.1787
Pendleton,45.6721,-118.7886
Newport,44.6368,-124.0534
Redmond,44.2726,-121.1739
Madras,44.6332,-121.1294
Burns,43.5863,-119.0541
Ontario,44.0266,-116.9629
Seaside,45.9932,-123.9226
Tillamook,45.4562,-123.8426
Florence,43.9826,-124.0984
Coos_Bay,43.3665,-124.2179
```

### Step 3: Run the Program

Run program.py

The program will:
* Load the graph from `graph_v2.txt` and the data from `vertices_v1.txt`
* Ask for your input. Make sure you input a valid starting vertex name and goal vertex name.
* Print the results for each algorithm

---

## Example Output

```
Enter the start vertex name: Portland
Enter the goal vertex name: Burns
Greedy Best First Search
Portland -> Hood_River -> The_Dalles -> Pendleton -> Ontario -> Madras -> Redmond -> Bend -> Burns
Distance: 529.0
Time Taken: 0.00018644332885742188
Edges Evaluated: 19
Vertices Explored: 9


Dijkstra's Algorithm
Portland -> Hood_River -> The_Dalles -> Madras -> Redmond -> Bend -> Burns
Distance: 351.0
Time Taken: 0.00020456314086914062
Edges Evaluated: 53
Vertices Explored: 22


A*
Portland -> Hood_River -> The_Dalles -> Madras -> Redmond -> Bend -> Burns
Distance: 373.93369999999993
Time Taken: 0.000156402587890625
Edges Evaluated: 53
Vertices Explored: 22


Run algorithms again?
```