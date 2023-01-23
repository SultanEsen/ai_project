import cv2
import numpy as np


img = cv2.imread('images/image1.jpeg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# img = cv2.GaussianBlur(img, (1, 1), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 250, 250)

kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)


cv2.imshow('Photo', img)

print(img.shape)

cv2.waitKey(0)


# cap = cv2.VideoCapture(0)
# cap.set(3, 500)
# cap.set(4, 500)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('Video', img)
#
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break

