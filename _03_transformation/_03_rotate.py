import cv2

img = cv2.imread('pooya.jpg')
h, w, _ = img.shape

m = cv2.getRotationMatrix2D((w // 2, h // 2), 180, 1)

m[0, 2] += 100
m[1, 2] += 100
print(m)

img_rotate = cv2.warpAffine(img, m, (w, h))

cv2.imshow('', img_rotate)
cv2.waitKey(0)
