from email.mime import image
import imghdr
import cv2
import numpy as np 

bgr=np.zeros((800,800,3),dtype=np.uint8)
bgr[:,:,:]=(150,0,0)
#cv2.imshow("BRG",bgr)

img = cv2.circle(bgr,(230,230), 100, (0,50,70), 4)
#cv2.imshow("BRG2",img)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Hola,mundo',(50,100), font, 3,(0,100,255),2,cv2.LINE_AA)
#cv2.imshow("BRG3",img)

cv2.waitKey(0)
cv2.destroyAllWindows()





