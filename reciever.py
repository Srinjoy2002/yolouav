import cv2
from imageprocessing import process_frame  

cap = cv2.VideoCapture('http://192.168.63.8:5000/')  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    processed_frame = process_frame(frame)  

    cv2.imshow('Processed Frame', processed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
