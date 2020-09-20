import cv2
import dlib
import numba as np
from skimage.io import imshow
import face_recognition 

class FL:
    # def __init__(self):
    #     img=cv2.imread('/home/bigpenguin/Downloads/circle-cropped.png')
    #     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #     detector=dlib.get_frontal_face_detector()
    #     faces=detector(gray)
        
    #     for face in faces:
    #         x1=face.left()
    #         y1=face.top()
    #         x2=face.right()
    #         y2=face.bottom()

    #         cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)
        
    #     p = "/home/bigpenguin/Downloads/shape_predictor_68_face_landmarks.dat"
    #     # Initialize dlib's shape predictor
    #     predictor = dlib.shape_predictor(p)
    #     # Get the shape using the predictor
    #     landmarks=predictor(gray, face)

    #     for i in range(0,68):
    #         print(landmarks.part(i))
    def face_recognitions(self):

        known_image = face_recognition.load_image_file("/home/bigpenguin/Downloads/circle-cropped.png")
        unknown_image = face_recognition.load_image_file("/home/bigpenguin/Downloads/fr_test.jpeg")

        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
        print(results)

if __name__=='__main__':
    fl=FL()
    fl.face_recognitions()
