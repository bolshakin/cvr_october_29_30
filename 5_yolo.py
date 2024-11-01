from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated
#from pprint import pprint
model = YOLO('yolov8n.pt') # x надо поменять на n, x много весит

cap = cv2.VideoCapture(0)

#pprint(model.names)
#exit()

cap.set(4, 640) #cap.set(3, 640)
cap.set(3, 480) #cap.set(4, 480)

while True:
    _, img = cap.read()
    _, img = cap.read()

    # BGR to RGB conversion is performed under the hood
    # see: https://github.com/ultralytics/ultralytics/issues/2575
    results = model.predict(img)

    for r in results:

        annotator = Annotator(img)

        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            c = box.cls
            if model.names[int(c)] == 'person':
                x1, y1, x2, y2 = map(int, b)
                overlay = img.copy()
                cv2.rectangle(overlay, (x1, y1), (x2, y2), (0, 255, 0), -1)
                cv2.addWeighted(overlay, 0.4, img, 0.6, 0, img)
            else:
                annotator.box_label(b, model.names[int(c)])

    #img = annotator.result()
    cv2.imshow('YOhttps://habr.com/ru/articles/593547/LO V8 Detection', img)
    #print(img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()