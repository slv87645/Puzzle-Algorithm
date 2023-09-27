# Portfolio assignment from Analysis of Algorithms class. 
There is a 2-D puzzle of side M x N, that has N rows and M columns. Each cell in the puzzle is either empty or has a barrier. Empty cells are marked by '-' and ones with barriers are marked by '#'. 
* We are given two coordinates (a,b) and (x,y) where we start at (a,b) and want to reach (x,y). 
* We are only able to move into empty cells and cannot move into cells with a barrier. 
* Each move can be in one of 4 directions: up, down, right, and left.

The goal of the algorithm is to reach the destination cell covering the minimum number of cells as you travel from the starting cell. 
My approach utilized a breadth-first search.
