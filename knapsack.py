##
## =======================================================
## Joshua Ng (20786371)
## CS 231 Spring 2020
## Assignment 03, Problem 1
## =======================================================
##

from grids import *
from sess2q3pair import *

## find(lst,grid,bound,total): returns the positions of objects in lst that are selected to maximaze the total value
##                             with at most the bound in Grid.
## find: (listof Pair) Grid Int Int -> (listof Int)
def find(lst,grid,bound,total):
    l = []
    for i in range(len(lst),0,-1):
        if total<=0:
            break
        if total != grid.access(i-1,bound):
            l.append(i-1)
            total = total - lst[i-1].value
            bound = bound - lst[i-1].item
    return l

## knapsack(lst,bound): returns a list of positions, indicating the objects selected that 
##                      determine the subset of objects with total weight at most the 
##                      bound that maximizes the total value
## knapsack: (listof Pair) Int -> (listof Int)
## Requires: bound > 0
def knapsack(lst, bound):
    grid = Grid(len(lst)+1, bound+1) 
    for i in range(0,len(lst) + 1):
        for j in range(bound + 1):
            if i ==0 or j ==0:
                grid.enter(i,j,0)
            elif lst[i-1].item <= j:
                m = max(lst[i-1].value + grid.access(i-1,j - lst[i-1].item), grid.access(i-1,j))
                grid.enter(i,j,m)
            else:
                grid.enter(i,j,grid.access(i-1,j))
    return find(lst,grid,bound,grid.access(i,j))



 

