# USAGE
# python detect_face_parts.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/example_01.jpg 
# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import time

video_capture = cv2.VideoCapture(0)
while True:
	ret, frame = video_capture.read()
	if ret == True:
		# construct the argument parser and parse the arguments
		ap = argparse.ArgumentParser()
		ap.add_argument("-p", "--shape-predictor", required=True,help="path to facial landmark predictor")
		#ap.add_argument("-i", "--image", required=True,help="path to input image")
		args = vars(ap.parse_args())

		# initialize dlib's face detector (HOG-based) and then create
		# the facial landmark predictor
		detector = dlib.get_frontal_face_detector()
		predictor = dlib.shape_predictor(args["shape_predictor"])

		# load the input image, resize it, and convert it to grayscale
		#image = cv2.imread(frame)
		frame = imutils.resize(frame, width=500)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# # detect faces in the grayscale image
		rects = detector(gray, 1)

		# # # loop over the face detections
		for (i, rect) in enumerate(rects):
	 	# determine the facial landmarks for the face region, then
	 	# convert the landmark (x, y)-coordinates to a NumPy array
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)

			# loop over the face parts individually
			for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
				# clone the original image so we can draw on it, then
				# display the name of the face part on the image
				clone = frame.copy()
				cv2.putText(clone, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
					0.7, (0, 0, 255), 2)

				# loop over the subset of facial landmarks, drawing the
				# specific face part
				for (x, y) in shape[i:j]:
					cv2.circle(clone, (x, y), 1, (0, 255, 0), -1)

				#extract the ROI of the face region as a separate image
				(x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
				roi = frame[y:y + h, x:x + w]
				roi = imutils.resize(roi, width=250, inter=cv2.INTER_CUBIC)

				# show the particular face part
				cv2.imshow("ROI", roi)
				cv2.imshow("Image", clone)
				cv2.waitKey(3000)

			# visualize all facial landmarks with a transparent overlay
			output = face_utils.visualize_facial_landmarks(frame, shape)
			cv2.imshow('video', output)
		if cv2.waitKey(0) & 0xFF == ord('q'):
    			break
			
video_capture.release()
cv2.destroyAllWindows()
