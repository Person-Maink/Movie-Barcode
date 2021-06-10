import cv2
import numpy as np
from os import system
import concurrent.futures as c

def fps_cont(frame_count, width):
    if width == 1:
        return 1
    else:
        return int(frame_count/width)

def make_barcode(path):

    width_pass = 130

    cap = cv2.VideoCapture(path[0])
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
            print(str((total_frames/(frame_count+1))*100) + " % Done!")

        frame_count += 1
        cv2.imshow(path[0],cv2.resize(img, (1500, int(height/3))))
        #cv2.imshow('frame',frame)

    cv2.imwrite(path[1], img)
    print("Image created!")

if __name__ == '__main__':

    path_arr = []

    moviePath = '/home/mayankthakur/Downloads/Over.the.Moon.2020.1080p.WEBRip.x265-RARBG/Over.the.Moon.2020.1080p.WEBRip.x265-RARBG.mp4'
    picPath = 'bruhhhh.png'
    make_barcode([moviePath, picPath])
    img_rand = np.ones((100,100,3),np.uint8)
    cv2.imwrite(picPath, img_rand)


    #for i in range(1,35):
    #    #movie_path = "D:\Documents\Code\Python\movieImage\\" + "({})".format(i) + ".mp4"
    #    #pic_path = "D:\Documents\Code\Python\movieImage\movie" + "pic" + str(i) + ".png"

    #    movie_path = "({})".format(i) + ".mp4"
    #    pic_path = "pic" + str(i) + ".png"

    #    #img_rand = np.ones((100,100,3),np.uint8)
    #    #cv2.imwrite(pic_path, img_rand)

    #    path_arr.append([movie_path, pic_path])
    #    #print([movie_path, pic_path])
    #    #make_barcode([movie_path, pic_path])

    #with c.ProcessPoolExecutor() as e:
    #    e.map(make_barcode, path_arr)


    print("Done!")
