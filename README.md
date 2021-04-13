# UniformCostSearch
Uniform Cost Search implemented for Artificial Intelligence course

## About The Project

It is a project for Akdeniz University Computer Science Department - Artificial Intelligence Lesson. 

Developed a program to find the best route based on cost between 2 cities of a map. Program takes cities from a .csv file. Example map & example lines of .csv file:

       city1,city2,distance
       Balıkesir,Çanakkale,95
       Çanakkale,İstanbul,125

[![Road Map](https://github.com/nidadinch/UniformCostSearch/blob/main/RoadMap.png)](https://github.com/nidadinch/UniformCostSearch/blob/main/RoadMap.png)


The program calculates all routes from starting city to destination city. Prints the best route between this cities and cost of this route in km. It was implemented using Uniform Cost Search.

## Uniform Cost Search

Uniform Cost Search is one of the best algorithms for a search problem. It is like Dijkstra Algorithm but it doesn’t store all route to queue, only stores the start point. When other cities were necessary, queue will store this cities. This algorithm gives the minimum cumulative cost the maximum priority. The pseudo code of algorithm using priority queue is:

    
    Insert the root into the queue While the queue is not empty
    Dequeue the maximum priority element from the queue
    (If priorities are same, alphabetically smaller path will chosen) 
        If the path is ending in the goal state, print the path and exit Else
        Insert all the children of the dequeued element,
        with the cumulative costs as priority
    
 

## Built With 

* Python

## Getting Started 

1. ```sh
   python3 ucs.py

   ```

  
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Nida Dinç - niddinc@gmail.com

Project Link: [https://github.com/nidadinch/UniformCostSearch](https://github.com/nidadinch/UniformCostSearch)

## Resources
 
https://thispointer.com/python-read-a-csv-file-line-by-line-with-or-without-header/ 

https://stackoverflow.com/questions/58157354/python-create-a-graph-from-a-dictionary

https://stackoverflow.com/questions/23179230/python-processing-each-row-independently-using-map-function

https://evanhahn.com/python-skip-header-csv-reader/

http://aima.cs.berkeley.edu/algorithms.pdf

https://www.section.io/engineering-education/graph-data-structure-python/

https://stackoverflow.com/questions/3483520/use-cases-for-the-setdefault-dict-method

https://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-python-dictionary

https://www.programiz.com/python-programming/exception-handling

https://docs.python.org/3/tutorial/errors.html

https://algorithmicthoughts.wordpress.com/2012/12/15/artificial-intelligence-uniform-cost-searchucs/