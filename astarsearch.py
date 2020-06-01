import heapq as hp
import cv2
import time


def get_neighbors(m, n, closed):
    #position of the node
    x,y = n[1]
    neighbors = []
    if x-1 >= 0 and m[x-1][y]!=1 and (x-1,y) not in closed:
        neighbors.append((n,(x-1,y),n[2]+1))

    if x+1 < len(m) and m[x+1][y] !=1 and (x+1,y) not in closed:
        neighbors.append((n,(x+1,y),n[2]+1))

    if y+1 < len(m) and m[x][y+1] !=1 and (x,y+1) not in closed:
        neighbors.append((n,(x,y+1),n[2]+1))

    if y-1 >= 0 and m[x][y-1] !=1 and (x,y-1) not in closed:
        neighbors.append((n,(x,y-1),n[2]+1))
    
    return neighbors
    
def optimal_path(m, n):
    path = []
    while n != None:
        path.append(n[1])
        n = n[0] 
    return path

def draw(neighbors, image, winW, winH,color):
    for n in neighbors:
        image[n[1][0]*winW+5:(n[1][0]+1)*winW-5, n[1][1]*winH+5:(n[1][1]+1)*winH-5] =color

def astar(m, start, end, image, winW, winH):
    red = (250,200,200)
    green = (200,250,200)
    gold = (0,255,255)

    # parent, postion, g(n)
    start_node = (None,start,0)
    #f(n)= g(n) + h(n)
    #h: manhatan distance
    # A* priority function
    # f = lambda n: n[2]+ abs(n[1][0]-end[0]) + abs(n[1][1]-end[1])

    # Dijkstra
    f = lambda n: n[2] 
    #postion that we've seen at each step
    closed =set()
    h =[]
    path = []
    hp.heappush(h, (f(start_node),id(start_node), start_node))
    while h:
        node = hp.heappop(h)[2]
        draw([node],image,winW,winH,red)
        #add position of the node to the closed dict
        closed.add(node[1])
        #check if the end 
        if node[1]==end:
            path = optimal_path(m, node)
            break
            
        #get neighbors
        neighbors = get_neighbors(m,node, closed)
        #add neighbor to the priority queue
        draw(neighbors, image,winW,winH,green)
        cv2.imshow("Window", image)
        cv2.waitKey(1)
        time.sleep(0.25)
        for n in neighbors:
            hp.heappush(h, (f(n),id(n),n))
    for n in path:
        image[n[0]*winW+5:(n[0]+1)*winW-5, n[1]*winH+5:(n[1]+1)*winH-5] =gold
    cv2.imshow("Window", image)
    
    cv2.waitKey(0)
    
      
    
    return path
