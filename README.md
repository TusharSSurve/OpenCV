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

## 18. Remove Duplicate Images From An Given Dataset

Having duplicate images in your dataset creates a problem for two reasons:
- It introduces bias into your dataset, giving your deep neural network additional opportunities to learn patterns specific to the duplicates
- It hurts the ability of your model to generalize to new images outside of what it was trained on

And identifying duplicates in a large dataset manually is very time consuming and error-prone. That's why we want to remove duplicate images from our dataset.

## 19. Eye Blink Count Detection

We can use eye blink count detector to check if eyes are blinking regularly or not to avoid the symptoms of Dry Eye. As eye blink is considered to be a suitable indicator for fatigue diagnostics. Drowsy state may be caused by lack of sleep, medication, drugs or driving continuously for long time period.

I have used pre-trained HOG + Linear SVM object detector specifically for the task of face detection.
Download shape_predictor_68_face_landmarks.dat from here:-
https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat

## 20. Object Tracking

Simple and realtime object tracking in a video sequence. 

## 21. Add Watermark

Add watermark to images using opencv. Please make sure that watermark has black background.

## 22. Multiple Object Tracking

Simple, multiple and realtime object tracking in a video sequence. 

## 23. QRCode & Barcode Scanner

Scanning QRCode & Barcode through camera using opencv and pyzbar.

## 24. Semantic Segmentation

Semantic segmentation, or image segmentation, is the task of clustering parts of an image together which belong to the same object class. It is a form of pixel-level prediction because each pixel in an image is classified according to a category. It can be used for autonomous driving, robotic navigation, localization, and scene understanding.

## 25. Human Activity Recognition

Human activity recognition model can recognize over 400 activities with 78.4-94.5% accuracy.

## 26. Image Smoothing

Smoothing is often used to reduce noise within an image or to produce a less pixelated image. Smoothing is also usually based on a single value representing the image, such as the average value of the image or the middle (median) value.

## 27. Yawn Detector

Yawn Detection is all about detecting yawn( open one’s mouth wide and inhale deeply due to tiredness or boredom) using OpenCV and Dlib. It can be used in various major applications like Self Driving Cars, Driver’s Fatigue detection, Driver’s Drowsiness detection, Driver’s consciousness detection etc.

I have used pre-trained HOG + Linear SVM object detector specifically for the task of face detection.
Download shape_predictor_68_face_landmarks.dat from here:-
https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat

## 28. Hand Landmark Detection 

Detect 21 landmarks of a hand using opencv and mediapipe. First, we have to use palm detection then we use hand landmark detector. Hand landmarks can be used in gesture control.

<a id="custom-anchor-name"></a>
## 29. Volume Control Using Hand Detection

Building a Volume Controller with OpenCV can be accomplished in just 3 simple steps:
- Step 1. Detect Hand landmarks 
- Step 2. Calculate the distance between thumb tip and index finger tip.
- Step 3. Map the distance of thumb tip and index finger tip with volume range. For my case, distance between thumb tip and index finger tip was within the range of 15 - 220 and the volume range was from -63.5 - 0.0. 

<a id="custom-anchor-name1"></a>
## 30. Brightness Control Using Hand Detection

Building a Brightness Controller with OpenCV can be accomplished in just 3 simple steps:
- Step 1. Detect Hand landmarks 
- Step 2. Calculate the distance between thumb tip and index finger tip.
- Step 3. Map the distance of thumb tip and index finger tip with volume range. For my case, distance between thumb tip and index finger tip was within the range of 15 - 220 and the volume range was from 0 - 100. 

## 31. Left or Right Hand Detection

Check whether the given hand in an image is left or right hand. It can be used to advance hand gestures control.

## 32. Brightness & Volume Control

It's same as [Volume Control Using Hand Detection](#custom-anchor-name) & [Brightness Control Using Hand Detection](#custom-anchor-name1). Only difference is now we can manage brightness with left hand & volume with right hand simultaneous.

## 33. Face Mesh

Face Mesh is a face geometry solution that estimates 468 3D face landmarks in real-time. It can be used as facial landmarks for detecting eyes, mouth, jawline, nose & eyebrows. Face mesh is mainly useful for real-time augmented reality (AR) applications.

## 34. Face Detector - Advance

So far I have used haar cascade & dlib for face detection. The main disadvantage of using this model was poor accuracy in terms of lightning, detecting background as face sometimes & much more. In order to overcome this, I have use the resnet caffe pretrained model.

## 35. Human Pose Estimation

Detect 33 3D landmarks on the whole body (or 25 upper-body landmarks) using opencv and mediapipe. It can be used in various applications such as quantifying physical exercises, sign language recognition, and full-body gesture control. For example, it can form the basis for yoga, dance, and fitness applications. It can also enable the overlay of digital content and information on top of the physical world in augmented reality.

## 36. Holistic Estimation 

Live perception of simultaneous human pose, face landmarks, and hand tracking in real-time can enable various modern life applications: fitness and sport analysis, gesture control and sign language recognition, augmented reality try-on and effects. It generate a total of 543 landmarks (33 pose landmarks, 468 face landmarks, and 21 hand landmarks per hand).

## 37. Save a video

Often, we have to capture live stream with camera. OpenCV provides a very simple interface to this. 

## 38. Create a GIF

Create an animated GIF in real-time.

## 39. Objectron

Objectron is a real-time 3D object detection solution for everyday objects. It detects objects in 2D images, and estimates their poses through a machine learning (ML) model. Currently supports Shoe, Chair, Cup & Camera.

## 40. Timer
Show Timer on webcam.
