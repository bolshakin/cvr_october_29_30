import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    #print(key)
    if key == ord(' '):
        break
    #print(ret)
    #print(frame)
cv2.destroyAllWindows()
cap.release()
