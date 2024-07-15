#import torch
#print(torch.cuda.is_available())
import cv2
import os
from ultralytics import YOLO
import time
import playsound
from sound_c import Sound
#this function is used to detect the currency in the image
def detect(file):
    model = YOLO("best.pt")
    results = model.predict(file, conf=0.7)
    result = results[0]
    try:
        len(result.boxes)
        box = result.boxes[0]
        class_id = result.names[box.cls[0].item()]
        #print("Probability:", box.conf)
        #print(result.names)
        #print("Object type:", class_id)
        currency = class_id
    except:
        print("No object detected")
        currency = 0
    return currency

#this is used to capture the image from the camera
while True:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite("temp.jpg", frame)
    cap.release()
    currency = detect("temp.jpg")
    print("Currency:", currency)
    Sound.soundplay(currency)
    os.remove("temp.jpg")
    time.sleep(10)
