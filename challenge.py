import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import imutils

# load image
img = cv2.imread("red.png", 1)

#convert the color and filter it for red pixels
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_upper_threshold = cv2.inRange(img_HSV, (0, 200, 130), (255, 255, 240))
mask = img_upper_threshold

#find contours on the image to identify the cones
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

coords = list()
for i in contours:

    
    #print(i)
    M = cv2.moments(i)
    #find the largest contours to single out the cones
    if(cv2.contourArea(i) > 200):
        try:
         cX = int(M['m10']/M['m00'])
         cY = int(M['m01']/M['m00'])
         coords.append((cX,cY))
         
        except:
         continue
       # print the center of each contour
        cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
       
# finding points that are on the left side and right side of the image to create the two lines
color = (0, 255, 0)
left_line = list()
right_line = list()
for point in coords:
    #print(point)
    if(point[0] < 900): 
        left_line.append(point)
    else:
        right_line.append(point)

#plot the lines
cv2.line(img, right_line[0], right_line[len(right_line) - 1], color, 4)
cv2.line(img, left_line[0], left_line[len(left_line) - 1], color, 4)
# display the answer
cv2.imshow("cones", img)
cv2.imshow("cones2", mask )

key = cv2.waitKey(0)
if key == ord('q') or key == 27:
    cv2.destroyAllWindows()

cv2.imwrite("answer.png", img)