from datetime import datetime
import cv2
import time
import pandas
import imutils


initial_frame = None                                                                        #initialising the initial frame to a null value
status_record = [None, None]                                                                #to keep track of when objects enter and leave the scenario
times = []                                                                                 #to record the times an object enters or leaves the scenario
dataframe_motion = pandas.DataFrame(columns = ["Entry", "Exit"])
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)

while True:
    check, image = video.read()
    status_motion = 0                                                                             #status var tells if there is an object in the frame or not
    image = imutils.resize(image, width = 600)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 8)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)                                              #to remove noise and make the image more smooth

    #for x, y, w, h in faces:
    #    image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 3)


    if initial_frame is None:
        initial_frame = gray.copy().astype("float")
        continue

    cv2.accumulateWeighted(gray, initial_frame, 0.25)
    delta_image = cv2.absdiff(cv2.convertScaleAbs(initial_frame), gray)                                          #bg subtraction

    thresh_image = cv2.threshold(delta_image, 50, 255, cv2.THRESH_BINARY)[1]                #to make only the significant values more prominent after subtraction
    thresh_image = cv2.dilate(thresh_image, None, iterations = 50)                          #to smoothen out the subtracted image

    (_,contours,_) = cv2.findContours(thresh_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 3000:                                                 #eliminates the smaller white areas that are obtained
            continue

        status_motion = 1
        (xcord, ycord, width, height) = cv2.boundingRect(contour)                           #gets the dimensions of the rectangle that contains the particular contour
        cv2.rectangle(image, (xcord, ycord), (xcord+width, ycord+height), (0, 255, 0), 2)   ##that is large enough and draws a green rectangle around it in the main video frame

    if status_motion == 1:
        cv2.putText(image, "Something is moving!", (10, 20),
    		cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 255), 2)
    else:
        cv2.putText(image, "Nothing has moved for some time", (10, 20),
    		cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 255), 2)

    status_record.append(status_motion)

    if status_record[-1] == 1 and status_record[-2] == 0:
        times.append(datetime.now())
    if status_record[-1] == 0 and status_record[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("Main Detection", image)
    cv2.imshow("Delta", delta_image)
    cv2.imshow("Detect", thresh_image)

    key = cv2.waitKey(1)
    if key == ord('q'):
        if status_motion == 1:
            times.append(datetime.now())
        break

print(times)


for i in range(0, len(times), 2):
    dataframe_motion = dataframe_motion.append({"Entry":times[i],"Exit":times[i+1]}, ignore_index = True)

dataframe_motion.to_csv("Motion_Times.csv")
video.release()
cv2.destroyAllWindows
