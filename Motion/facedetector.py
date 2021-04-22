import cv2 , time

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("frontalface.xml")

a = 0

while True:
  a = a + 1
  _ , gray = video.read()
  if a==1:
    time.sleep(2)


  # gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

  faces = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

  for x , y , w, h in faces:
    gray = cv2.rectangle(gray , (x,y) , (x + w , y + h) , (0,255,0) , 3)
  
  cv2.imshow("Image Capturing" , gray)

  key = cv2.waitKey(1)

  print(gray)

  if key == ord('q'):
    break
 
video.release()
cv2.destroyAllWindows()