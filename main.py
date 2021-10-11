import face_recognition
from PIL import Image, ImageDraw
import cv2
import numpy as np
# from  simple_facerec import SimpleFacerec

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    print(ret, frame)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
# def recognition():
#    pass

#
# if __name__ == "__main__":
#     recognition()
