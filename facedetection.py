import cv2
from deepface import DeepFace
import os
import sys
from speak import *

detected_face_name= None
# Function to perform face detection and recognition
def performFaceDetection():
    global detected_face_name 
    print("Face detection started")
    speak("Face detection started")
    speak("Please look at the camera")
    # Initialize the webcam
    video_capture = cv2.VideoCapture(0)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # Decrease frame width
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # Decrease frame height

    # Set the directory for known faces
    known_faces_dir = "known_faces"

    # Load known faces and their names
    known_face_paths = []
    known_face_names = []

    # Iterate through each user folder in the known_faces_dir
    for user_name in os.listdir(known_faces_dir):
        user_dir = os.path.join(known_faces_dir, user_name)
        if os.path.isdir(user_dir):
            for image_name in os.listdir(user_dir):
                image_path = os.path.join(user_dir, image_name)
                known_face_paths.append(image_path)
                known_face_names.append(user_name)

    last_detected_names = []  # Initialize last detected names
    face_detected = False  # Flag to indicate if a face is detected

    while not face_detected:
        # Capture a single frame of video
        ret, frame = video_capture.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Flip the frame horizontally (to correct mirroring)
        frame = cv2.flip(frame, 1)

        # Convert the image from BGR color to RGB color
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Initialize an array for names of detected faces
        face_names = []

        try:
            if not last_detected_names:
                # Perform face detection and verification
                for known_face_path, known_face_name in zip(known_face_paths, known_face_names):
                    result = DeepFace.verify(known_face_path, rgb_frame)

                    if result["verified"]:
                        face_names.append(known_face_name)
            else:
                # Check if new faces are detected
                new_face_detected = False
                for known_face_path, known_face_name in zip(known_face_paths, known_face_names):
                    if known_face_name not in last_detected_names:
                        result = DeepFace.verify(known_face_path, rgb_frame)

                        if result["verified"]:
                            face_names.append(known_face_name)
                            new_face_detected = True
                            break

                if not new_face_detected:
                    # No new faces detected, return empty list
                    face_names = []

        except Exception as e:
            # Handle errors during face detection
            # print("Error during face detection:", e)
            print("Please face yourself at the camera ")

        if face_names:
            speak("Face detected successfully")
            # Known face detected
            speak(f"Hello, {', '.join(face_names)}!")
            last_detected_names = face_names
            face_detected = True
            detected_face_name = last_detected_names[0]
            print(detected_face_name)
            break  # End face recognition

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

    if face_detected:
        return True
    else:
        speak("Sorry, I cannot recognize you.")
        return False

