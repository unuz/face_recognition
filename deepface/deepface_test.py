from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import os

def deepface():
    imgDir = 'knowns'
    files = os.listdir(imgDir)
    for filename in files:
        name, ext = os.path.splitext(filename)
        if ext == '.jpg':
            img = cv2.imread(imgDir+"/"+filename)
            imgplot = plt.imshow(img)

            obj = DeepFace.analyze(img_path = imgDir+"/"+filename, actions = ['age', 'gender', 'race', 'emotion'])
            print("name : ", filename)
            print("age :",obj["age"], "gender :",obj["gender"], "dominant_race :",obj["dominant_race"], "dominant_emotion :",obj["dominant_emotion"])

    return obj

        # print("age : ",obj["age"])
        # print("gender : ",obj["gender"])
        # #인종 분석
        # #print("race : ",obj["race"])
        # print("dominant_race : ",obj["dominant_race"])
        # #감정 분석
        # #print("emotion : ",obj["emotion"])
        # print("dominant_emotion : ",obj["dominant_emotion"])
                

# def deepface():
#     imgFile = "knowns/test2.jpg"
#     img = cv2.imread(imgFile)
#     imgplot = plt.imshow(img)

#     print("imgFile : ",imgFile)
#     obj = DeepFace.analyze(img_path = imgFile, actions = ['age', 'gender', 'race', 'emotion'])

#     return obj, imgFile

# print("age : ",obj["age"])
# print("gender : ",obj["gender"])
# #인종 분석
# #print("race : ",obj["race"])
# print("dominant_race : ",obj["dominant_race"])
# #감정 분석
# #print("emotion : ",obj["emotion"])
# print("dominant_emotion : ",obj["dominant_emotion"])


#print(obj["age"]," years old ",obj["dominant_race"]," ",obj["dominant_emotion"]," ", obj["gender"])
