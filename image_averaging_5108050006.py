import itertools
import glob
import os
import numpy as np
import cv2

# postfix file name
SUPPORTED_EXTENSIONS = ["bmp", "png", "jpg", "jpeg", "JPG"]

# list images in folder
def dataset_files(folder):
    return list(itertools.chain.from_iterable(
        glob.glob(os.path.join(folder, "*.{}".format(ext))) for ext in SUPPORTED_EXTENSIONS))

imgs = dataset_files("2")   # load images from folder
pic1 = cv2.imread(imgs[0])
avg_img = np.zeros(pic1.shape)   

for i in range(len(imgs)):
    pic = cv2.imread(imgs[i])
    # print(imgs[i])
    avg_img += pic / len(imgs)
            
avg_img = avg_img.astype(np.uint8)
cv2.imwrite("average.jpg",avg_img)  # output averaging result to file

cv2.imshow("res",avg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
