import cv2


class FaceDetector:

    def __init__(self, faceCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

    def detect(self, image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)):
        rects = self.faceCascade.detectMultiScale(
            image,
            # reduction factor at each image scale
            scaleFactor=scaleFactor,
            # number of neighbors each window should have to be considered a face
            minNeighbors=minNeighbors,
            # minimum size of the window
            minSize=minSize,
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        return rects
