from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

# img1_path = "knowns/img1.jpg"
# img2_path = "knowns/img2.jpg"

def verify(img1_path,img2_path):
    img1= cv2.imread(img1_path)
    img2= cv2.imread(img2_path)

    print(type(img1_path))
    print(img1_path)
    print(type(img2_path))
    print(img2_path)
    
    """
    plt.imshow(img1[:,:,::-1])
    plt.show()
    plt.imshow(img2[:,:,::-1])
    plt.show()
    """
    
    output = DeepFace.verify(img1_path,img2_path)
    print(output)
    verification = output['verified']
    if verification:
       print('They are same')
    else:
       print('The are not same')

verify('knowns/test123.jpg', 'knowns/test456.jpg')