import numpy as np
import cv2 as cv
import psutil as ps
import pyautogui as pag

def stoper():
    eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    previous_eyes = current_eyes = "0"
    state = False

    while True:
        try:
            processes = [psutil.Process(i).name() for i in psutil.pids()]
            if "vlc.exe" in str(processes):
                state = True
                
            if state:
                cap = cv.videocapture(0)
                
        except:
            pass
        
        while state:
            previous_eyes = current_eyes
            _, frame = cap.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces) < 1:
                current_eyes = "0"
            for (x,y,w,h) in faces:
                cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    if ey > 40 and ey < 100:
                        current_eyes = "1"
                        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            if previous_eyes + current_eyes == "01":
                pag.hotkey('Shift', '2') #resume
            if previous_eyes + current_eyes == "10":
                pag.hotkey('Shift', '1') #pause
            try:
                processes = [psutil.Process(i).name() for i in psutil.pids()]
                cv.namedWindow('Retina',cv.WINDOW_NORMAL)
                cv.imshow('Retina',frame)
                k = cv.waitKey(10)
                if "vlc.exe" not in str(processes):
                    pag.alert(text='Retina is haulted', title='Retina', button='OK')
                    runningState = False
                    cap.release()
                    cv.destroyAllWindows()
                    break
            except:
                pass