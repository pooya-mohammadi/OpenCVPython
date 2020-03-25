import matplotlib.pyplot as plt
import cv2

img = cv2.imread('pooya.jpg')

height, width, _ = img.shape

img_resize = cv2.resize(img, (width * 2, height * 2))
img_resize_2 = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
img_resize_flag = cv2.resize(img, dsize=None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

plt.subplot(1, 4, 1)
plt.imshow(img[..., ::-1])
plt.title('org')

plt.subplot(1, 4, 2)
plt.imshow(img_resize[..., ::-1])
plt.title('resize')

plt.subplot(1, 4, 3)
plt.imshow(img_resize_2[..., ::-1])
plt.title('resize_2')


plt.subplot(1, 4, 4)
plt.imshow(img_resize_flag[..., ::-1])
plt.title('img_resize_flag')

plt.show()
# check out https://chadrick-kwag.net/cv2-resize-interpolation-methods/
