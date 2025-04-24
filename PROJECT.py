from cvzone.HandTrackingModule import HandDetector
import cv2
import time
import serial

# Setup serial port (update 'COM3' to your port)
ser = serial.Serial('COM5', 9600, timeout=1)

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.5)
prev_time = 0
last_command = None

while True:
    ret, frame = cap.read()
    if not ret: break

    hands, frame = detector.findHands(frame)
    if hands:
        hand = hands[0]
        lmList = hand['lmList']
        if lmList:
            fingers = detector.fingersUp(hand)

            # Finger logic
            if fingers == [0, 1, 0, 0, 0] and last_command != "1":
                ser.write(b'1')
                print("Sent: 1 (ON)")
                last_command = "1"

            elif fingers == [0, 1, 1, 0, 0] and last_command != "2":
                ser.write(b'2')
                print("Sent: 2 (OFF)")
                last_command = "2"

    # FPS calculation
    new_time = time.time()
    fps = int(1 / (new_time - prev_time))
    frame = cv2.putText(frame, f'FPS: {fps}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    prev_time = new_time

cap.release()
cv2.destroyAllWindows()
