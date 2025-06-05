import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=2)


cap = cv2.VideoCapture(0)  
cap.set(3, 640)  
cap.set(4, 480)  
while True:  
    success, img = cap.read() 
    img = cv2.flip(img, 1) 
    hands, img = detector.findHands(img) 
    if hands and hands[0]['type'] == 'Left': 
        fingers = detector.fingersUp(hands[0]) 
        totalFingers = fingers.count(1) 
        cv2.putText(img, f'Fingers: {totalFingers}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        if totalFingers == 5:
            pyautogui.keyDown('right')
            pyautogui.keyUp('left')
        if totalFingers == 0:
            pyautogui.keyDown('left')
            pyautogui.keyUp('right')

    cv2.imshow("Image", img)
    cv2.waitKey(1) 