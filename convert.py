import numpy as np #Math lib
import cv2 #Image manipulation lib
import os #Os commands

if not os.path.exists('small'): #Does the folder "small" exists ?
   os.makedirs('small') #If not, create it
pic_num=1   #Initialize var pic_num with value 1

for i in ['test']: #For every element of this list (containing 'test' only atm)

 try: #Try to
  if os.path.exists(str(pic_num)+'.jpg'): #If the image pic_num (= 1 at first) exists
      print(i) #Prints 'test' (because it's only element of the list)
      #Initialize var img with image content (opened with lib cv2)
      img=cv2.imread(str(pic_num)+'.jpg') 
      #We resize the image to dimension 100x100 and store result in var resized_image
      resized_image=cv2.resize(img,(100,100)) 
      #Save the result on disk in the "small" folder
      cv2.imwrite("small/"+str(pic_num)+'.jpg',resized_image)
  pic_num+=1 #Increment variable pic_num
 except Exception as e: #If there was a problem during the operation
      print(str(e)) #Prints the exception
