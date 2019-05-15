import numpy as np
import cv2 as cv
import psutil as ps
import pautogui as pag

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
previous_eyes = current_eyes = "0"
state = False