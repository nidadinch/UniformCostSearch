import csv
from queue import PriorityQueue

# CSE 362 - Artificial Intelligence 
# Program for calculating distance between two cities & best route 
# using Uniform Cost Search algorithm 
# Ayşe Nida Dinç - 20160808047

class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)


def build_graph(path):

    file = open(path,'r')
    routes = {}
    next(file)
    for row in file:
        
        row = row.split(',')
        routes.setdefault(row[0], []).append((row[1],row[2]))
        routes.setdefault(row[1], []).append((row[0],row[2]))
        
    file.close()
    
   # print(routes)
    return routes
