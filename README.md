# OpenCV-Mini-Projects
**Computer vision** is a field of artificial intelligence that trains computers to interpret and understand the visual world. Using digital images from cameras and videos and deep learning models, machines can accurately identify and classify objects — and then react to what they “see.”

**OpenCV (Open Source Computer Vision Library)** is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez. The library is cross-platform and free for use under the open-source BSD license.

Here are some projects & their applications which can be build using openCV:-

## 1. Face Blur

Use GaussianBlur with a kernel of (91,91) to blur faces. It can be used for Privacy & Identity Protection in public/private areas. Can increase or decrease blur strength by changing the kernel.

## 2. Color Transfer

Used one image color (source) to change the color of different image (target) using both Color Transfer Algorithm as well as color_transfer modules. It can be used to apply different types of color filters.

## 3. Live Sketch

convert an image or a video into a sketch.

## 4. Extract Faces From An Image

Simple python program to extract faces from an image. It can be used in a face recognition app to improve accuracy.

## 5. Color Detection

Color detection is the process of detecting the name of any color. Color detection is necessary to recognize objects, it is also used as a tool in various image editing and drawing apps. Some Real-world Applications:-

- In self-driving car, to detect the traffic signals.
- Multiple color detection is used in some industrial robots, to performing pick-and-place task in separating different colored objects.

## 6. Virtual Paint

This code helps you track an object-of-interest to draw colored lines on the screen (just like the Paint application but using the webcam).

## 7. Number Plate Detection

Detecting Number plate from image (or webcam) of cars.

## 8. Facial Landmark Detection

Detect all landmarks of face like Eyes, Nose, Lips, Eyebrows.
I have used pre-trained HOG + Linear SVM object detector specifically for the task of face detection.
Download shape_predictor_68_face_landmarks.dat from here:-
https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat

Detecting facial landmarks in an image is a two step process:
First i have localize a face(s) in an image. This can be accomplished using a number of different techniques, but normally involve either Haar cascades or HOG + Linear SVM detectors. Apply the shape predictor, specifically a facial landmark detector, to obtain the (x, y)-coordinates of the face regions in the face ROI. 

It can used in Face part extraction (i.e., nose, eyes, mouth, jawline, etc.), Facial alignment, Head pose estimation, Face swapping, Blink detection …and much more applications!

## 9. Eye Blink Detection

Detect if an eye blink or not. We first detect the eyes & then, we detect two lines: an horizontal line and a vertical line crossing the eye. The size of the horizontal line is almost identical in the closed eye and in the open eye while the vertical line is much longer in the open eye in coparison with the closed eye. In the closed eye, the vertical line almost disappears.

I have used pre-trained HOG + Linear SVM object detector specifically for the task of face detection.
Download shape_predictor_68_face_landmarks.dat from here:-
https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat

## 10. Face Recognition

Face recognition is a method of identifying or verifying the identity of an individual using their face. Face recognition systems can be used to identify people in photos, video, or in real-time. Law enforcement may also use mobile devices to identify people during police stops. 

## 11. Document Scanner

Building a document scanner with OpenCV can be accomplished in just three simple steps:

- Step 1: Detect edges.
- Step 2: Use the edges in the image to find the contour (outline) representing the piece of paper being scanned.
- Step 3: Apply a perspective transform to obtain the top-down view of the document.

## 12. Drowsiness Detection

Driver drowsiness detection is a car safety technology which helps prevent accidents caused by the driver getting drowsy. Various studies have suggested that around 20% of all road accidents are fatigue-related, up to 50% on certain roads.

Some of the current systems learn driver patterns and can detect when a driver is becoming drowsy. 
I have used pre-trained HOG + Linear SVM object detector specifically for the task of face detection.
Download shape_predictor_68_face_landmarks.dat from here:-
https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat

## 13. Chrome Dino Game

Play offline chrome dinosaur game using opencv & eye blink. Just open chrome browser with no internet connection.
Drawback of this application is it can be used only for jumping purpose.

I have used pre-trained HOG + Linear SVM object detector specifically for the task of face detection.
Download shape_predictor_68_face_landmarks.dat from here:-
https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat

## 14. Object Detection

Object detection is a computer vision technique that allows us to identify and locate objects in an image or video. With this kind of identification and localization, object detection can be used to count objects in a scene and determine and track their precise locations, all while accurately labeling them.

## 15. Angle Finder

Created an Angle Finder. In that, I first define two lines using mouse clicks and then find the angle between theses lines using simple mathematics. 

## 16. Face Alignment

Face alignment is the task of identifying the geometric structure of faces in digital images, and attempting to obtain a canonical alignment of the face based on translation, scale, and rotation. Using Face Alignment we can get higher accuracy from our face recognition. As Face Alignment is like data normalization.

I have used pre-trained HOG + Linear SVM object detector specifically for the task of face detection.
Download shape_predictor_68_face_landmarks.dat from here:-
https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat

## 17. Contour Detection

Contour detection is a major issue in image processing. For instance, in classification and segmentation, the goal is to split the image into several parts. This problem is strongly related to the detection of the connected contours separating these parts. It is quite easy to detect edges using local image analysis techniques, but the detection of continuous contours is more complicated and needs a global analysis of the image.
