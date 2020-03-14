import cv2
import matplotlib.pyplot as plt

img_path = 'pooya.jpg'

img = cv2.imread(img_path)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_rgb_2 = img[..., ::-1]

plt.subplot(1, 3, 1)
plt.imshow(img)

plt.subplot(1, 3, 2)
plt.imshow(img_rgb)

plt.subplot(1, 3, 3)
plt.imshow(img_rgb_2)


plt.show()
