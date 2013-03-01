from video_iterable import *

def main():
  videofilm = VideoIterable('original.mov')  # Home Movies Reference
  print("read in video")
  for image in videofilm:
    cv2.imshow('video', image)
    if cv2.waitKey(10) == 27:
      break

main()

