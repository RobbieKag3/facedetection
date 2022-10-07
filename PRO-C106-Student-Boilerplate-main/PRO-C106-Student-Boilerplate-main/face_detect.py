import cv2 
image=cv2.imread("PRO-C106-Student-Boilerplate-main/boy.jpg")
facecascade=cv2.CascadeClassifier("PRO-C106-Student-Boilerplate-main/haarcascade_frontalface_default.xml")
greyscale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=facecascade.detectMultiScale(greyscale,1.1,5)
for (x,y,w,h) in faces:
       cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow("face.jpg",image)
cv2.waitKey()