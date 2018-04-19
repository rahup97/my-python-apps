import cv2, time

video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    check, image = video.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors = 5)

    for x, y, w, h in faces:
        image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)


    cv2.imshow("Frontal Face Detection", image)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows
