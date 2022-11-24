#pip install opencv-python
import cv2

#create a CascadeClassifier Object
face_cascade=cv2.CascadeClassifier("C:\\Users\\mahesh\\PycharmProjects\\haarcascade_frontalcatface.xml")

#Reading the image as it is
img=cv2.imread("C:\\Users\\mahesh\\Downloads\\WhatsApp Image 2022-11-24 at 6.22.11 AM.jpeg")
resized=cv2.resize(img,(600,500))

#Reading the image as gray scale image
gray_img=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)

#Search the coordinates of the image
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in faces:
    img=cv2.rectangle(resized,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

