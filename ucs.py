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


def uniform_cost_search(graph, start_city, destination_city):

    visited = set() 
    route = [] 
    priority_queue = PriorityQueue() 
    priority_queue.put((0, [start_city])) 
    
    while priority_queue:

        if priority_queue.empty(): 
            print ('distance: infinity \nroute: \nnone')
            break

        distance, route = priority_queue.get() 
        city = route[len(route)-1]

        if city not in visited:
            visited.add(city) 

            if city == destination_city: 
                route.append(distance)
                display_route(graph,route)
                return route

        childs = graph[city]
        neighbor=[i[0] for i in childs] 

        for i in neighbor:
            if i not in visited: 
            
                totaldistance = distance + int(city_to_neighbor(graph, city, i))
                temp = route[:]
                temp.append(i)
                priority_queue.put((totaldistance, temp)) 

    return priority_queue


def city_to_neighbor(graph, current, neighbor):
    index = [i[0] for i in graph[current]].index(neighbor)
    return graph[current][index][1]


def display_route(graph,route):
    length = len(route)
    distance = route[-1]
    print()
    print('Distance between cities: %s km'%(distance))
    print()
    print('Best route: ')
    count = 0
    while count < (length-2):
        km = city_to_neighbor(graph, route[count], route[count+1]) 
        print('%s -> %s %s' %(route[count],route[count+1],km))
        count+=1
    return




if __name__ == "__main__":
    
    while True:
        try:
            inputFile = input("Enter road map path: ")
            test = open(inputFile, 'r').readlines()
        except FileNotFoundError:
            print("Wrong file or file path, please try again!")
        else:
            break
       
    graph = build_graph(inputFile)

    while True:
        try:
            start_city = input("Enter the start city: ")
            if start_city not in graph: 
                raise CityNotFoundError(start_city)
            break
        except CityNotFoundError:
            print("City not found on map, try again!")
    
    while True:
        try:
            destination_city = input("Enter the destination city: ")
            if destination_city not in graph: 
                raise CityNotFoundError(destination_city)
            break
        except CityNotFoundError:
            print("City not found on map, try again!")

   
    uniform_cost_search(graph, start_city, destination_city) 
         
    pass