#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import lcddriver
import time
import atexit
from Raspi_PWM_Servo_Driver import PWM
import RPi.GPIO as gpio
#import driveFunctions
from driveFunctions import Drive
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

#threshold straight -0.01 to 0 to 0.01
#threshold straigh left slight -0.01 to -0.11
#threshold straight left hard -0.11 and over
#threshold straight right slight 0.01 to 0.11
#threshold straight right hard 0.11 and over
drive = Drive()
def make_points(image, line):
    slope, intercept = line
    y1 = int(image.shape[0])# bottom of the image
    y2 = int(y1*3/5)         # slightly lower than the middle
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return [[x1, y1, x2, y2]]

def average_slope_intercept(image, lines):
    left_fit    = []
    right_fit   = []
    if lines is None:
        return None
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit = np.polyfit((x1,x2), (y1,y2), 1)
            slope = fit[0]
            intercept = fit[1]
            if slope < 0: # y is reversed in image
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
    # add more weight to longer lines
    left_fit_average  = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line  = make_points(image, left_fit_average)
    right_line = make_points(image, right_fit_average)
    averaged_lines = [left_line, right_line]
    return averaged_lines

def canny(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    kernel = 5
    blur = cv2.GaussianBlur(gray,(kernel, kernel),0)
    canny = cv2.Canny(gray, 50, 150)
    return canny

def display_lines(img,lines):
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    return line_image

def region_of_interest(canny):
    height = canny.shape[0]
    width = canny.shape[1]
    mask = np.zeros_like(canny)

    triangle = np.array([[
    (200, height),
    (550, 250),
    (1100, height),]], np.int32)

    cv2.fillPoly(mask, triangle, 255)
    masked_image = cv2.bitwise_and(canny, mask)
    return masked_image

def findlanes(image):
    canny_image = canny(frame)
    cropped_canny = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_canny, 2, np.pi/180, 100, np.array([]), minLineLength=40,maxLineGap=5)
    averaged_lines = average_slope_intercept(frame, lines)
    line_image = display_lines(frame, averaged_lines)
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    cv2.imshow("result", combo_image)

def img_preprocess(img):
    img = img[60:135,:,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3,3), 0 )# arg = img , kernal size and deviation
    img = cv2.resize(img , (200,66))
    img = img/255 # normalisation , explained in lane detection
    return img

def main(frame):
    image = np.asarray(frame)
    image = img_preprocess(image)
    image = np.array([image])
    steering_angle = float(model.predict(image))
    if steering_angle >= -0.01 && steering_angle <= 0.01:
        drive.Forward()
    else if steering_angle >= -0.11 && steering_angle < -0.01:
        drive.MoveLightLeft()
    else if steering_angle >= -1.00 && steering_angle < -0.11:
        drive.MoveHardLeft()
    else if steering_angle < -1.0:
        drive.SpinLeft()
    else if steering_angle <= 0.11 && steering_angle > 0.01:
        drive.MoveLightRight()
    else if steering_angle <= 1.00 && steering_angle > -0.11:
        drive.MoveHardRight()
    else if steering_angle > 1.0:
        drive.SpinRight()

if __name__ == '__main__':
    model = load_model('models/model.h5')
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        #__main__
        main()
        findlanes()
        #cv2.imshow('frame',frame)    
        if cv2.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
