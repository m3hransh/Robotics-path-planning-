def astar(map, start, end):
    
    # parent, postion, g(n)
    start_node = (None,start,0)
    #f(n)= g(n) + h(n)
    #h: manhatan distance
    #A* priority function
    f = lambda n: n[2]+ abs(n[1][0]-end[0]) + abs(n[1][1]-end[1])

    #postion that we've seen at each step
    closed =set()
    h =[]
    path = []
    hp.heappush(h, (f(start_node),id(start_node), start_node))
    while h:
        node = hp.heappop(h)[2]
        #add position of the node to the closed dict
        closed.add(node[1])
        #check if the end 
        if node[1]==end:
            path = optimal_path(m, node)
            break
            
        #get neighbors
        neighbors = get_neighbors(m,node, closed)
        #add neighbor to the priority queue
        for n in neighbors:
            hp.heappush(h, (f(n),id(n),n))
    for n in path:
        image[n[0]*winW+5:(n[0]+1)*winW-5, n[1]*winH+5:(n[1]+1)*winH-5] =gold
    
    return path
