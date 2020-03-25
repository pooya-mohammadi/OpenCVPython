import cv2

img_path = 'pooya.jpg'

img = cv2.imread(img_path)

cv2.rectangle(img, (200, 200), (500, 600), (0, 255, 0), 2)

cv2.imshow('pooya', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
