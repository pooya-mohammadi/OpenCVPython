import cv2

img_path = 'pooya.jpg'

img = cv2.imread(img_path)

cv2.rectangle(img, (200, 200), (500, 600), (0, 255, 0), 2)
cv2.putText(img, 'pooya mohammadi', (200, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
cv2.imwrite('pooya_mohammadi.png', img)
