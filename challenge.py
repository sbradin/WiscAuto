import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import imutils


img = cv2.imread("red.png", 1)

img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_upper_threshold = cv2.inRange(img_HSV, (0, 200, 130), (255, 255, 240))
mask = img_upper_threshold

contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cv2.drawContours(img, contours, -1, (0,255,0), 3)

#contours = imutils.grab_contours(contours)
coords = list()
for i in contours:
    # area = dict()
    # print(cv2.contourArea(i))
    # area[i]=(cv2.contourArea(i))
    
    #print(i)
    M = cv2.moments(i)
    if(cv2.contourArea(i) > 200):
        try:
         cX = int(M['m10']/M['m00'])
         cY = int(M['m01']/M['m00'])
         coords.append((cX,cY))
         
        except:
         continue
        #print( M )
        #cv2.drawContours(img, [i], -1, (0, 255, 0), 2)
        cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
        #cv2.putText(img, "center", (cX - 20, cY - 20),
		    #cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

color = (0, 255, 0)
left_line = list()
right_line = list()
for point in coords:
    #print(point)
    if(point[0] < 900): 
        left_line.append(point)
    else:
        right_line.append(point)

# for index in range(len(right_line) - 1):
#     cv2.line(img, right_line[index], right_line[index+1], color, 4)
# for index2 in range(len(left_line)-1):
#     cv2.line(img, left_line[index], left_line[index2+1], color, 4)
cv2.line(img, right_line[0], right_line[len(right_line) - 1], color, 4)
cv2.line(img, left_line[0], left_line[len(left_line) - 1], color, 4)
cv2.imshow("cones", img)
cv2.imshow("cones2", mask )

key = cv2.waitKey(0)
if key == ord('q') or key == 27:
    cv2.destroyAllWindows()

cv2.imwrite("answer.png", img)