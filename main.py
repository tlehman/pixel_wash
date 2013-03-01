import cv2

while (success,image = capture.read())[0]:
  cv2.imshow('video', image)

