# face_recog.py

import face_recognition
import cv2
import camera
import os
import numpy as np

class FaceRecog():
    def __init__(self):
        # Using OpenCV to capture from device 0. 
        # If you have trouble capturing from a webcam, 
        # comment the line below out and use a video file instead.
        self.camera = camera.VideoCamera()

        self.known_face_encodings = []
        self.known_face_names = []

        dirname = 'knowns'
        files = os.listdir(dirname)
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext == '.jpg':
                self.known_face_names.append(name)
                pathname = os.path.join(dirname, filename)
                #이미지 불러오기
                img = face_recognition.load_image_file(pathname)
                #이미지 인코딩 (type : numpy)
                #이미지 인코딩 => 128차원 얼굴 인코딩
                face_encoding = face_recognition.face_encodings(img)[0]
                print(type(face_encoding))
                print(face_encoding)

                self.known_face_encodings.append(face_encoding)

        # Initialize some variables
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

        self.frame_count = 0

    def __del__(self):
        del self.camera

    def get_frame(self):


        self.frame_count += 1

        # Grab a single frame of video
        frame = self.camera.get_frame()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        #if self.process_this_frame:

        # 50프레임 당 한 번 실행
        if self.frame_count % 50 == 0:
            # Find all the faces and face encodings in the current frame of video

            # 사람 얼굴 경계 상자 배열 반환
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            # frame -> 128차원 얼굴 인코딩
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

            print("rgb_small_frame : ",rgb_small_frame)
            print("self.face_locations : ",self.face_locations)
            print("self.face_encodings : ",self.face_encodings)

            #print("rgb_small_frame : ",rgb_small_frame)

            self.face_names = []
            for face_encoding in self.face_encodings:
                # See if the face is a match for the known face(s)
                # 얼굴 비교에 대한 거리 값 반환
                distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                '''
                # endocings -> 특징점 128개
                print(" known face_distance  :",self.known_face_encodings)
                print(" face_distance  :",face_encoding)
                print(" face_distance size  :",face_encoding.size)
                '''
                min_value = min(distances)

                # tolerance: How much distance between faces to consider it a match. Lower is more strict.
                # 0.6 is typical best performance.
                name = "Unknown"
                if min_value < 0.5:
                    index = np.argmin(distances)
                    name = self.known_face_names[index]

                self.face_names.append(name)

        # 1프레임 당 한 번 실행
        #self.process_this_frame = not self.process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left, bottom), font, 1.0, (255, 255, 255), 1)


            #print("****************** frame : ", frame)
        return frame

    def get_jpg_bytes(self):
        frame = self.get_frame()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpg = cv2.imencode('.jpg', frame)

        #print("*********** get_jpg_bytes : ")

        return jpg.tobytes()


if __name__ == '__main__':
    # print('__face_recog__ : ', __name__)
    # print('__cv2__라이브러리 : ', cv2)
    # print('__face_recognition__라이브러리 : ', face_recognition)
    # print('__np__라이브러리 : ', np)
    
    face_recog = FaceRecog()
    while True:
        frame = face_recog.get_frame()

        # show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    print('finish')
