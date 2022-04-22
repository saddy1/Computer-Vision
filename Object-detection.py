#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:



#create a window
cv2.namedWindow('Track')
cv2.resizeWindow('Track', 700, 512)

#trackbar
def track(x):
    pass

cv2.createTrackbar('hue min', 'Track', 87, 179, track)
cv2.createTrackbar('hue max', 'Track', 103, 179, track)
cv2.createTrackbar('sat min', 'Track', 103, 255, track)
cv2.createTrackbar('sat max', 'Track', 244, 255, track)
cv2.createTrackbar('val min', 'Track', 63, 255, track)
cv2.createTrackbar('val max', 'Track', 213, 255, track)



# In[3]:



cap = cv2.VideoCapture(0)

while(True):

    # Take each frame
    _, frame = cap.read()
    frame = cv2.flip(frame, +1)     ##Mirror image frame
    
    h_min = cv2.getTrackbarPos('hue min', 'Track')
    h_max = cv2.getTrackbarPos('hue max', 'Track')
    s_min = cv2.getTrackbarPos('sat min', 'Track')
    s_max = cv2.getTrackbarPos('sat max', 'Track')
    val_max = cv2.getTrackbarPos('val max', 'Track')
    val_min = cv2.getTrackbarPos('val min', 'Track')
    print(f'HUE MIN : {h_min} HUE MAX : {h_max} SAT MIN : {s_min} SAT MAX : {s_max} VAL MIN : {val_min} VAL MAX : {val_max}')

    
   

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_red = np.array([h_min,s_min,val_min])
    upper_red = np.array([h_max,s_max,val_max])

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27 :
        break

cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




