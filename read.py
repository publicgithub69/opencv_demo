import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

# Reading image
img = cv.imread('images/dog_1.webp')
cv.imshow('dog',rescaleFrame(img))

#Reading Video
#capture=cv.VideoCapture('videos/dog_video.mp4')


    
'''
while True:
    isTrue, frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
'''


#capture.release()
cv.destroyAllWindows()
