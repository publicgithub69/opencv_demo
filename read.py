import cv2 as cv


# Reading image
#img = cv.imread('images/dog_1.webp')
#cv.imshow('dog',img)

#Reading Video
capture=cv.VideoCapture('videos/dog_video.mp4')


while True:
    isTrue, frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
