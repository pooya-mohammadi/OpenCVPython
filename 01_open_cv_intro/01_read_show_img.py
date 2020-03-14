import cv2

print('version: ', cv2.__version__)

img_path = 'pooya.jpg'

img = cv2.imread(img_path)
print('shape: ', img.shape)
print('type: ', type(img))
print('dtype: ', img.dtype)

cv2.imshow('pooya', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
