import numpy as np
import cv2

img = cv2.imread('pooya.jpg')
h, w, _ = img.shape
# M =[ 1 0 tx]
#    [0 1 ty]

tx = 100
ty = 100
m = np.array([[1, 0, tx], [0, 1, ty]]).astype(np.float32)

img_translate = cv2.warpAffine(img, m, (w, h))

cv2.imshow('', img_translate)
cv2.waitKey(0)
