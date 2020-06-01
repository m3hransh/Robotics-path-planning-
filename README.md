# Path Planning

## intro
Path-planning is an important primitive for autonomous mobile
robots that lets robots find the shortest—or otherwise optimal—
path between two points. Optimal paths could be paths that
minimize the amount of turning, the amount of braking or
whatever a specific application requires. Algorithms to find
a shortest path are important not only in robotics, but also in
network routing, video games and understanding protein fold-
ing.
## Python Implementation
A* and Dijkstra are implemented in python. To run the code in python you need opencv and numpy. The easiest way to install is using Anaconda or conda. The code has been executed on linux machine. you can install opencv with this:
```bash
conda install -c conda-forge opencv=4.1.0
``` 
## Code Explanation
There is a map.png file in test_images folder that represent our map. First, using opencv the image represents using a matrix and then the path planning algorithm will run on the matrix.
### A* algorithm simulation
This gif shows the execution of the program. the green rectangle is the starting point and red one is our end goal.
![Alt text](./astar.gif)

### Dijkstra algorithm simulation
To run the Dijkstra algorithm you can use A* algorithm but the only thing that you need to change is to change f(n) function to f(n) = g(n).
![Alt text](./dijkstra.gif)
