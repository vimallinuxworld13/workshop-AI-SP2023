import os
import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture( 0 )

# click photo
status , photo = cap.read()

detector = HandDetector()

# show the pic, from python code
cv2.imshow("my photo" , photo)
cv2.waitKey()
cv2.destroyAllWindows()


handphoto = detector.findHands(photo , draw=False)
lmlist = handphoto[0]
fingerstatus = detector.fingersUp(lmlist)



if fingerstatus == [1,1,1,1,1]:
    print("all up")
    os.system("chrome")

elif fingerstatus == [ 0 ,1 ,0 , 0, 0]:
    print("index finget up")
    os.system("chrome https://www.google.com/search?q=vimal+daga")
    
elif fingerstatus == [ 0 , 1, 1, 0 , 0 ]:
    print("index and middle finger up")
    os.system("notepad") 
else:
    print("idk")
