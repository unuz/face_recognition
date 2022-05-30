# camera.py

import cv2

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0.
        # If you have trouble capturing from a webcam, 
        # comment the line below out and use a video file instead.
        self.video = cv2.VideoCapture(0)
        #print("self.video", self.video)

        # If you decide to use video.mp4, 
        # you must have this file in the folder as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        # Grab a single frame of video
        #print("self", self.video.read());
        ret, frame = self.video.read()
        return frame


if __name__ == '__main__':
    # print('__camera__ : ', __name__)
    # print('__cv2__라이브러리 파일 위치 : ', cv2.__file__)
    cam = VideoCamera()
    while True:
        frame = cam.get_frame()
        #print('frame : ', frame)
        # show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    #print('finish')
