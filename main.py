import cv2

class VideoIterable(object):
  """ Take a filename of a video and yield the current frame on each call to next() """
  def __init__(self, filename):
    self.filename = filename
    capture = cv2.VideoCapture(filename)
    read_from(capture)

  def read_from(capture):
    self.success, self.image = capture.read()

  def next(self):
    read_from(capture)
    if (self.success == False):
      raise StopIteration 
    return self.image

capture = cv2.VideoCapture('original.mov')
success,image = capture.read()

while success:
  success,image = capture.read()
  cv2.imshow('video', image)
  if cv2.waitKey(10) == 27:
    break

