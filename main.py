import cv2
import numpy as np
from os import system
import multiprocessing

cap = cv2.VideoCapture("D:\Documents\Code\Python\movieImage\movie.mp4")
width_center = int((cap.get(cv2.CAP_PROP_FRAME_WIDTH)/2))
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
img = np.zeros((int(height),1,3),np.uint8)
frame_count = 0

try:
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
except:
    total_frames = 1
    print("Frames percentage is broken, unable to get total frame count")

while(1):
    ret, frame = cap.read()

    frame_show = frame[:, width_center:width_center+1] #width and then height limitation

    if frame_count % int(total_frames/2500) == 0:
        img = cv2.hconcat([img, frame_show])
        print(str(float(frame_count/total_frames*100))+" % Done!")

    cv2.imshow('frame',frame_show)

    if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
        cap.release()
        cv2.destroyAllWindows()
        break

    frame_count += 1

cv2.imwrite("D:\Documents\Code\Python\movieImage\pic.png", img)
print("Image created!")
