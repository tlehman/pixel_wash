import cv2

class VideoIterable(object):
  """ Take a filename of a video and yield the current frame on each call to next() """
  def __init__(self, filename):
    self.filename = filename
    self.capture = cv2.VideoCapture(filename)
    self.read_next_from_capture()

  def __iter__(self):
    return self

  def read_next_from_capture(self):
    self.success, self.image = self.capture.read()
    return self.success

  def next(self):
    if self.read_next_from_capture() == False:
      raise StopIteration 
    return self.image

def main():
  videofilm = VideoIterable('original.mov')
  print("read in video")
  for image in videofilm:
    cv2.imshow('video', image)
    if cv2.waitKey(10) == 27:
      print("hit key 27")
      break

main()

