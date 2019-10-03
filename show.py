
import os
import cv2
while(1):
    image = cv2.imread('capture.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('captured.png',gray_image)
    cv2.imshow('color_image',image)
    cv2.imshow('gray_image',gray_image)   
    img =cv2.imread(os.path.join('/root/Desktop/Anil','capture1.jpg')
#cv2.imwrite(os.path.join('/root/Desktop/Anil1','captured.jpg'),img)
#cv2.waitkey(0)
cv2.destroyALlWindows()
