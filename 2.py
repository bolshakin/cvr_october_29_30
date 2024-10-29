import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #print(frame.shape)
    height, width, _ = frame.shape
    length = round(0.52*height)
    x = width // 2
    y = height // 2
    l = length // 2
    frame[(y-l):(y+l), (x-l):(x+l), 1] = 255
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    #print(key)
    if key == ord(' '):
        break
    #print(ret)
    #print(frame)
cv2.destroyAllWindows()
cap.release()
