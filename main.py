import cv2
import numpy as np
from os import system

def fps_cont(frame_count, width):
    if width == 1:
        return 1
    else:
        return int(frame_count/width)

def make_barcode(movie_path, image_path, width_pass):

    cap = cv2.VideoCapture(movie_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    img = np.zeros((int(height),1,3),np.uint8)
    frame_count = 0

    try:
        total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    except:
        total_frames = 1
        print("Frames percentage is broken, unable to get total frame count")

    while(1):
        ret, frame = cap.read()

        if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
            cap.release()
            cv2.destroyAllWindows()
            break

        if frame_count % fps_cont(total_frames, width_pass) == 0:
            img = cv2.hconcat([img, cv2.resize(frame, (1,height))])
            if int(frame_count/total_frames*100) != int((frame_count-1)/total_frames*100):
                print(str(int(frame_count/total_frames*100))+" % Done!")

        frame_count += 1
        cv2.imshow('frame',cv2.resize(img, (width, height)))

    cv2.imwrite(image_path, img)
    print("Image created!")

for i in range(2,8):
    movie_path = "D:\Documents\Code\Python\movieImage\movie" + str(i) + ".mp4"
    pic_path = "D:\Documents\Code\Python\movieImage\pic" + str(i) + ".png"

    img_rand = np.ones((100,100,3),np.uint8)
    cv2.imwrite(pic_path, img_rand)

    cont = make_barcode(movie_path, pic_path, 4500)

    if cont == False:
        break

print("Done!")
