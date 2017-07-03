import cv2
import time
import pandas
from datetime import datetime

initial_frame = None                                                                        #initialising the initial frame to a null value
status_record = [None, None]                                                                #to keep track of when objects enter and leave the scenario
times = []                                                                                  #to record the times an object enters or leaves the scenario
dataframe = pandas.DataFrame(columns = ["Entry", "Exit"])
video = cv2.VideoCapture(0)

while True:
    check, image = video.read()
    status = 0                                                                              #status var tells if there is an object in the frame or not
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)                                              #to remove noise and make the image more smooth


    if initial_frame is None:
        initial_frame = gray
        continue

    delta_image = cv2.absdiff(initial_frame, gray)                                          #bg subtraction

    thresh_image = cv2.threshold(delta_image, 30, 255, cv2.THRESH_BINARY)[1]                #to make only the significant values more prominent after subtraction
    thresh_image = cv2.dilate(thresh_image, None, iterations = 10)                          #to smoothen out the subtracted image

    (_,contours,_) = cv2.findContours(thresh_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 3000:                                                 #eliminates the smaller white areas that are obtained
            continue

        status = 1
        (xcord, ycord, width, height) = cv2.boundingRect(contour)                           #gets the dimensions of the rectangle that contains the particular contour
        cv2.rectangle(image, (xcord, ycord), (xcord+width, ycord+height), (0, 255, 0), 2)   ##that is large enough and draws a green rectangle around it in the main video frame

    status_record.append(status)

    if status_record[-1] == 1 and status_record[-2] == 0:
        times.append(datetime.now())
    if status_record[-1] == 0 and status_record[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("Main Detection", image)
    #cv2.imshow("Delta", delta_image)
    #cv2.imshow("Detect", thresh_image)

    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break
    print(status)

print(times)

for i in range(0, len(times), 2):
    dataframe = dataframe.append({"Entry":times[i],"Exit":times[i+1]}, ignore_index = True)

dataframe.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows
