import cv2
import numpy as np
import os
from cv2 import cvtColor 
#image = cv2. imread((os.path.join("/root/Desktop/Anil","image.jpg"))
image = cv2.imread('/root/project/DATA/data/data/training/rose/a.jpg')
image= cv2.resize(image,(480,480))

                   
                   
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
hsvl = np.array([0,0,0])
hsvh = np.array([180,255,170])
mask = cv2.inRange(hsv, hsvl, hsvh)
masked = cv2.bitwise_or(image,image, mask= mask)
cv2.imwrite(os.path.join('/root/Desktop/Anil','gray.jpg'),masked)
cv2.imshow('masked',masked)
gray_image = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray_image.png',gray_image)
cv2.imshow('color_image',image)
cv2.imshow('gray_image',gray_image) 
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows
 
#End of Code
