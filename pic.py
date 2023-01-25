import cv2
import numpy as np


photo = np.zeros((500, 700, 3), dtype='uint8')

# RGB
# BGR
# photo[100:150, 200:250] = 3, 252, 82

cv2.rectangle(photo, (50, 100), (200, 200), (3, 252, 82), thickness=1)

cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (3, 252, 82), thickness=3)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 100, (3, 252, 82), thickness=2)

cv2.putText(photo, 'test text', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), thickness=1)

# print(type(photo))

cv2.imshow('Photo', photo)
cv2.waitKey(0)
