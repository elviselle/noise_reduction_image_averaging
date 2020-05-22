import itertools
import glob
import os
import numpy as np
import cv2

# 圖片檔副檔名
SUPPORTED_EXTENSIONS = ["bmp", "png", "jpg", "jpeg", "JPG"]

def dataset_files(root):
    return list(itertools.chain.from_iterable(
        glob.glob(os.path.join(root, "*.{}".format(ext))) for ext in SUPPORTED_EXTENSIONS))

imgs = dataset_files("2")
pic1 = cv2.imread(imgs[0])
avg_img = np.zeros(pic1.shape)

for i in range(len(imgs)):
    pic = cv2.imread(imgs[i])
    # print(imgs[i])
    avg_img += pic / len(imgs)
            
avg_img = avg_img.astype(np.uint8)
cv2.imwrite("average.jpg",avg_img)

cv2.imshow("res",avg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
