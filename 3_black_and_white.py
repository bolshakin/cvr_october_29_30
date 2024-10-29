import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(frame)
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    #print(key)
    if key == ord(' '):
        break
    break
    #print(ret)
    #print(frame)
cv2.destroyAllWindows()
cap.release()
