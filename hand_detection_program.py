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
led1 = LED(18)
led2 = LED(2)
led3 = LED(22)
led4 = LED(23)
led5 = LED(24)

temp1=1
values = range(1)
M1 = LED(17)
M2 = LED(27)



cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=1)
#mySerial = cvzone.SerialObject("COM8",9600,1)
values = range(5)




def play_audio(audio_path_file):
    #os.system('mpg123 ' + audio_path_file)
    print(audio_path_file)


def led_code_0():
    print("0")
    led1.off()
    led2.off()
    led3.off()
   
def led_code_1():
    print("1 ON ")
    audio_file_path = "/home/pi/Desktop/final_with_mp3_and_mp4/opencv_project/final_voices/led_1_on.mp3"
    play_audio(audio_file_path)
    led1.on()
    
    
def led_code_1_off():
    print("1 off ")
    audio_file_path = "/home/pi/Desktop/final_with_mp3_and_mp4/opencv_project/final_voices/led_1_on.mp3"
    play_audio(audio_file_path)
    led1.off()
       


def led_code_2():
    print("2 ON")
    
    
    led2.on()
    

    
    audio_file_path = "/home/pi/Desktop/final_with_mp3_and_mp4/opencv_project/final_voices/led_2_on.mp3"
    play_audio(audio_file_path)
    


def led_code_2_off():
    print("2 Off")
    
    led2.off()


def led_code_3():
    print("3 ON")
    
    led3.on()
    
    

    audio_file_path ="/home/pi/Desktop/final_with_mp3_and_mp4/opencv_project/final_voices/led_3_on.mp3"
    play_audio(audio_file_path)

def led_code_3_off():
    print("3 off")
    led3.off()

def code_run():
    led5.on()
    if fingerUp == [1,0,0,0,1]:
        

        audio_file_path = "/home/pi/Desktop/final_with_mp3_and_mp4/opencv_project/final_voices/led_control_started.mp3"
        play_audio(audio_file_path)
    elif fingerUp == [0, 1, 0, 0, 0]:
        cv2.putText(frame, 'Finger count:1', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)
        # print("one")
        for _ in values:
            led_code_1()
    elif fingerUp == [0, 1, 1, 0, 0]:
        cv2.putText(frame, 'Finger count:2', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)

        for _ in values:
            led_code_2()
    elif fingerUp == [0, 1, 1, 1, 0]:
        cv2.putText(frame, 'Finger count:3', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)
        led_code_3()

    elif fingerUp == [0, 0, 0, 0, 1]:
        cv2.putText(frame, 'Finger count:1', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)
        # print("one")
        for _ in values:
            led_code_1_off()
    elif fingerUp == [0, 0, 0, 1, 1]:
        cv2.putText(frame, 'Finger count:2', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)

        for _ in values:
            led_code_2_off()
    elif fingerUp == [0, 0, 1, 1, 1]:
        cv2.putText(frame, 'Finger count:3', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)
        led_code_3_off()
#    elif fingerUp == [0, 1, 1, 0, 0]:
#        cv2.putText(frame, 'low speed', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1,
#                    (255, 255, 255), 1)
#        medium_speed()
#   elif fingerUp == [0, 1, 0, 0, 0]:
#       cv2.putText(frame, 'fan medium speed', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1,
#                   (255, 255, 255), 1)
#       low_speed()

#   elif fingerUp == [0, 1, 1, 1, 0]:
#       cv2.putText(frame, 'fan high speed', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1,
#                   (255, 255, 255), 1)
#       high_speed()
    elif fingerUp == [0, 0, 1, 0, 0]:
        vilakamaru()












def fan_on():
    print("Fan on")
    
def fan_off():
    print("no action")
    M1.off()
    M2.off()
    

def exit_from_led_control():
    
    led5.off()

    print("Thank you")
    

  

    audio_file_path = "/home/pi/Desktop/final_with_mp3_and_mp4/opencv_project/final_voices/exit_from_led_control.mp3"
    play_audio( audio_file_path)



def low_speed():
    print("fan in low speed")
    M1.on()
    M2.off()
    
    audio_path = "/home/pi/Desktop/final_with_mp3_and_mp4/opencv_project/final_voices/fan_in_low_speed.mp3"
    play_audio(audio_path)
def high_speed():
    print("Fan in high speed")
    M1.off()
    M2.off()
 
    audio_path = "/home/pi/Desktop/final_with_mp3_and_mp4/opencv_project/final_voices/fan_in_high_speed.mp3"
    play_audio( audio_path)
def medium_speed():
    print("Fan in medium")
    
    M1.off()
    M2.on()
    audio_path = "/home/pi/Desktop/final_with_mp3_and_mp4/opencv_project/final_voices/fan_in_medium_speed.mp3"
    play_audio(audio_path)











def fan_run_controls():

    if fingerUp == [1, 1, 0, 0, 0]:
        
        cv2.putText(frame, 'fan control started', (20, 320), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (255, 255, 255), 1)
        
        led4.on()
        


        audio_path = "/home/pi/Desktop/final_with_mp3_and_mp4/opencv_project/final_voices/fan_control_stated.mp3"
        play_audio(audio_path)
        

    elif fingerUp == [0, 0, 0, 0, 1]:
        low_speed()
    elif fingerUp == [0, 1, 0, 0, 0]:
        low_speed()

    elif fingerUp == [0, 0, 0, 1, 1]:
        cv2.putText(frame, 'low speed', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (255, 255, 255), 1)
        medium_speed()
    elif fingerUp == [0, 1, 1, 0, 0]:
        cv2.putText(frame, 'low speed', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (255, 255, 255), 1)
        medium_speed()


    elif fingerUp == [0, 0, 1, 1, 1]:
        cv2.putText(frame, 'fan high speed', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (255, 255, 255), 1)
        high_speed()
    elif fingerUp == [0, 1, 1, 1, 0]:
        cv2.putText(frame, 'fan high speed', (20, 480), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (255, 255, 255), 1)
        high_speed()
    elif fingerUp == [0, 0, 0, 0, 0]:
        fan_off()

def exit_from_fan_control():
    led4.off()
    audio_path = "/home/pi/Desktop/final_with_mp3_and_mp4/opencv_project/final_voices/exit_fom_fan_control.mp3"
    play_audio(audio_path)

while True:

    ret, frame = cap.read()
    hands, frame = detector.findHands(frame)
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        #print(fingerUp)
        #mySerial.sendData(fingerUp)








        if fingerUp == [1, 1, 0, 0, 0]:
            score1 = score1 + 1

            cv2.putText(frame, "start", (20, 440), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [1, 1, 1, 0, 0]:
            # audio_file_path = "VOICES\\thank you 1.wav"
            # play_audio(audio_file_path)
            score1 = score1 - 1
            cv2.putText(frame, "end", (20, 440), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
        if score1 < 0:

            score1 = 0
            print("bye")
            exit_from_fan_control()

        cv2.putText(frame, 'fan time:  ' + str(score1), (200, 420), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)

        if score1 > 3:
            score1 = 4
            
            # cv2.imwrite(os.path.join(path, 'image.jpg'), frame)
            try:
                fan_run_controls()
            except:
                pass
                if thicc < 6:
                    thicc = thicc + 2
                else:
                    thicc = thicc - 2
                    if thicc < 2:
                        thicc = 2
                cv2.rectangle(frame, (0, 0), (1366, 768), (0, 0, 255), thicc)


        if fingerUp == [1,0,0,0,1]:
            score = score + 1

            cv2.putText(frame,"start",(20, 460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp == [1,1,0,0,1]:
            #audio_file_path = "VOICES\\thank you 1.wav"
            #play_audio(audio_file_path)
            score = score - 1
            cv2.putText(frame,"end",(20, 460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)

        if score < 0:
            score = 0
            
            print("bye")
            exit_from_led_control()
            
        cv2.putText(frame,'led time:  '+str(score),(200, 460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)

        if score > 3:
            score = 4
            
            
            
            #cv2.imwrite(os.path.join(path, 'image.jpg'), frame)
            try:
                
                code_run()
                
                
                    
            except:
                pass
                if thicc1 < 6:
                    thicc1 = thicc1 + 2
                else:
                    thicc1 = thicc1 - 2
                    if thicc1 < 2:
                        thicc1 = 2
                cv2.rectangle(frame, (0, 0), (1366, 768), (0, 0, 255), thicc1)


    frame = cv2.imshow("frame", frame)
    key = cv2.waitKey(1)

