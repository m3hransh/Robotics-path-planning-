import cv2
import numpy as np 
import time


import astarsearch
import traversal


def main(image_filename):

    #array for storing path
    path=[]
    #default start and end indexes
    start = (0,0)
    end = (1,1)

    #load the image
    image = cv2.imread(image_filename)
    (winW, winH) = (60, 60)

    obstacles = []
    #starting index for represnting map using matrix
    index = [1, 1]

    #create a blank, initialized a matrix of 0s
    blank_image = np.zeros((60,60,3), np.uint8)
    #create an array of 100 blank images
    list_images = [[blank_image for i in range(10)] for i in range(10)]

    #matrix for representing map
    maze = [[0 for i in range(10)] for i in range(10)]

    #traversal map using sliding square of the grid size 60
    for (x, y, window) in traversal.sliding_window(image, stepSize=60, windowSize=(winW, winH)):
        if window.shape[0] != winH or window.shape[1] != winW:
            continue
        #cloning image for showing the map analyze phase
        clone = image.copy()
        #format square for openCV
        cv2.rectangle(clone, (x, y), (x+ winW, y + winH), (0, 255, 0), 2)
        clone[ y:y + winH,x:x + winW] = (200,250,200)
        crop_img = image[ y:y + winH,x:x + winW]
        list_images[index[0]-1][index[1]-1] = crop_img.copy()

        #we want to print occupied grids, need to check if white or not
        average_color_per_row = np.average(crop_img, axis=0)
        average_color = np.average(average_color_per_row, axis=0)
        average_color = np.uint8(average_color)

        #finding end by recognizing red average
        if (average_color[2]>200 and average_color[1]<100 and average_color[0]<100):
            end = (index[0]-1,index[1]-1)
        #finding start by recognizing green average
        if (average_color[0]<200 and average_color[1]>200 and average_color[2]<200):
            start = (index[0]-1,index[1]-1)    
            
        #Obstacle are black
        if (all(i <= 20 for i in average_color)):
            obstacles.append(tuple(index))
            maze[index[0]-1][index[1]-1] = 1
        

        #show this iteration
        cv2.imshow("Window", clone)
        cv2.waitKey(1)
        time.sleep(0.025)
       

        #iterate
        index[1] = index[1]+1
        if(index[1]>10):
            index[0] = index[0] + 1
            index[1] = 1

    #get object list
      
   
    path = astarsearch.astar(maze, start, end,clone,winW, winH)

    return path
