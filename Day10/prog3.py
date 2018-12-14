'''
minimum cost of shortest path

2 8 6
3 5 4
4 3 2
'''

import cv2
import numpy as np

arr = np.array([[2,8,6],[3,5,4],[4,3,2]])

H = 8
#edge_costs = H - (f(p) - f(q))

edge_costs = np.array([[-1,14,-1,9,-1,-1,-1,-1,-1],
                        [2,-1,6,-1,5,-1,-1,-1,-1],
                        [-1,10,-1,-1,-1,6,-1,-1,-1],
                        [7,-1,-1,-1,10,-1,9,-1,-1],
                        [-1,11,-1,6,-1,7,-1,6,-1],
                        [-1,-1,10,-1,9,-1,-1,-1,6],
                        [-1,-1,-1,7,-1,-1,-1,7,-1],
                        [-1,-1,-1,-1,10,-1,9,-1,7],
                        [-1,-1,-1,-1,-1,10,-1,9,-1]])
                        
#min_cost = 1 - 4 - 7 - 8 - 9
min_cost = edge_costs[0,3] + edge_costs[3,6] + edge_costs[6,7] + edge_costs[7,8]

print ("Minimum cost from top left to bottom right: ")
print (min_cost)                      
                   
