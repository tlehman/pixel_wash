import cv2

capture = cv2.VideoCapture('original.mov')

success,image = capture.read()

while success:
  success,image = capture.read()
  cv2.imshow('video', image)
  if cv2.waitKey(10) == 27:
    break

