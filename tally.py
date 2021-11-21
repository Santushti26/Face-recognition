import cv2 
#import cv library
#import numpy
#import PIL as image

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
detector = cv2.CascadeClassifier(r"C:\Users\Santushti\OneDrive\Desktop\Sixth sense\haarcascade_frontalface_default.xml")
# cascade classifier -> algorithm
Id = input("Enter your id: \n")

sampleno = 0 

while True:
    ret , img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = detector.detectMultiScale(gray,1.3,5)  #scale of image

    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #x,y,w,h are diagonal cordinates
        sampleno =sampleno+1

        cv2.imwrite("dataSet/User."+Id+"."+"."+str(sampleno)+"jpg",gray[x:x+w,y:y+h])

        cv2.imshow("frame",img)

    if cv2.waitKey(100) == ord("q"):
        break

    elif sampleno >=30:
        break
cam.release()
cv2.destroyAllWindows()




