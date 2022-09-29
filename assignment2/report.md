# TDT4136 Assignment 2

In this assignment, we have implemented the A* algorithm with the example problem of navigating Samfundet under different circumstances.

I have solved all four tasks with the same Python file `a-star.py`. I have also slightly modified `Map.py` to add more color options when drawing the map. To switch between the different tasks, there is a global variable `TASK_NUMBER` at the top of `a-star.py` that can be changed to run the algorithm for the different tasks. The algorithm runs with Manhattan distance as the default heuristic function, but there is a global variable at the top of the file that can be changed to use Euclidian distance instead.

When running the program, two images will open: the first one is a map of the environment before the algorithm runs, and the second one shows the shortest path with green tiles and every expanded tile in yellow.

## Results

### Task 1

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cbf4703a-ff9f-4694-9a76-e52156e43f0d/Untitled.png)

### Task 2

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f4e4b9a9-e5a1-45ec-8977-eda8901ba3e4/Untitled.png)

### Task 3

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c81a2c99-6ec4-40dd-b61a-004360f3002f/Untitled.png)

### Task 4

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2204e201-9d0a-495f-b8a1-6b43c3e2600d/Untitled.png)
