import cv2
import os
from gpiozero import LED, Servo

from cvzone.HandTrackingModule import HandDetector
import RPi.GPIO as GPIO
import pygame
from time import sleep
import cvzone

score = 0
count = 0
path = os.getcwd()
score1 = 0
thicc = 0
thicc1 = 0
light1 = LED(18)
light2 = LED(2)
light3 = LED(22)
led4 = LED(23)
led5 = LED(24)

temp1=1
values = range(1)
M1 = LED(17)
M2 = LED(27)


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Initialize scores and thickness


score2 = 0
thicc2 = 2

start_valve = 25
def light_3_off():
    print("light_3_off")
    light3.off()
def light_3_on():
    print("light_3_on")
    light3.on()
def light_2_off():
    print("light_2_off")
    light2.off()
def light_2_on():
    print("light_2_on")
    light2.on()
def light_1_off():
    print("light_1_off")
    light1.off()
def light_1_on():
    print("light_1_on")
    light1.on()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    # Detect hands
    hands, frame = detector.findHands(frame)
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        # Check finger positions and update scores
        if fingerUp == [0, 1, 1, 0, 0]:
            score1 += 1
            cv2.putText(frame, "start", (20, 440), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 0, 0, 1, 1]:
            score1 -= 1
            cv2.putText(frame, "end", (20, 440), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

        if score1 < 0:
            score1 = 0
           
            light_2_off()

        cv2.putText(frame, 'Light 2 time: ' + str(score1), (200, 420), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)

        if score1 > start_valve:
            score1 = start_valve+1
            try:
                light_2_on()
                
            except:
                pass
            if thicc < 6:
                thicc += 2
            else:
                thicc -= 2
                if thicc < 2:
                    thicc = 2
            cv2.rectangle(frame, (0, 0), (1366, 768), (0, 0, 255), thicc)

        if fingerUp == [0, 1, 0, 0, 0]:
            score += 1
            cv2.putText(frame, "start", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 0, 0, 0, 1]:
            score -= 1
            cv2.putText(frame, "end", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

        if score < 0:
            score = 0
            print("bye")
            light_1_off()

        cv2.putText(frame, 'light 1 time: ' + str(score), (200, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)

        if score > start_valve:
            score = start_valve+1
            try:
                light_1_on()
                
            except:
                pass
            if thicc1 < 6:
                thicc1 += 2
            else:
                thicc1 -= 2
                if thicc1 < 2:
                    thicc1 = 2
            cv2.rectangle(frame, (0, 0), (1366, 768), (0, 0, 255), thicc1)

        if fingerUp == [0, 1, 1, 1, 0]:
            score2 += 1
            cv2.putText(frame, "start", (20, 440), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 0, 1, 1, 1]:
            score2 -= 1
            cv2.putText(frame, "end", (20, 440), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

        if score2 < 0:
            score2 = 0
           
            light_3_off()

        cv2.putText(frame, 'Light 3 time: ' + str(score2), (200,390), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)

        if score2 > start_valve:
            score2 = start_valve+1
            try:
                light_3_on()
                
            except:
                pass
            if thicc2 < 6:
                thicc2 += 2
            else:
                thicc2 -= 2
                if thicc2 < 2:
                    thicc2 = 2
            cv2.rectangle(frame, (0, 0), (1366, 768), (0, 0, 255), thicc)


    # Display the resulting frame
    cv2.imshow("frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
