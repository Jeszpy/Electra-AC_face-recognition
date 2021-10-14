import cv2
import os

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = "rtsp_transport;udp"
rtsp = "rtsp://admin:belprom1@192.168.1.64:554/onvif1"

cap = cv2.VideoCapture(rtsp, cv2.CAP_FFMPEG)

while True:
    ret, frame = cap.read()
    if ret == False:
        print('fail')
        break
    else:
        cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()