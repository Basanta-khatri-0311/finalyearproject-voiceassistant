# # # import cv2
# # # from deepface import DeepFace
# # # import os

# # # def detect_faces(frame, known_face_paths, known_face_names):
# # #     # Convert the image from BGR color to RGB color
# # #     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# # #     # Initialize an array for names of detected faces
# # #     face_names = []

# # #     # Perform face detection and verification
# # #     for known_face_path, known_face_name in zip(known_face_paths, known_face_names):
# # #         result = DeepFace.verify(known_face_path, rgb_frame)

# # #         if result["verified"]:
# # #             face_names.append(known_face_name)

# # #     return face_names

# # # def main():
# # #     # Initialize the webcam
# # #     video_capture = cv2.VideoCapture(0)
# # #     video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # Decrease frame width
# # #     video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # Decrease frame height

# # #     # Set the directory for known faces
# # #     known_faces_dir = "known_faces"

# # #     # Load known faces and their names
# # #     known_face_paths = []
# # #     known_face_names = []

# # #     # Iterate through each user folder in the known_faces_dir
# # #     for user_name in os.listdir(known_faces_dir):
# # #         user_dir = os.path.join(known_faces_dir, user_name)
# # #         if os.path.isdir(user_dir):
# # #             for image_name in os.listdir(user_dir):
# # #                 image_path = os.path.join(user_dir, image_name)
# # #                 known_face_paths.append(image_path)
# # #                 known_face_names.append(user_name)

# # #     last_detected_name = None  # Initialize last detected name
# # #     while True:
# # #         # Capture a single frame of video
# # #         ret, frame = video_capture.read()

# # #         # Flip the frame horizontally (to correct mirroring)
# # #         frame = cv2.flip(frame, 1)

# # #         # Detect faces in the frame
# # #         face_names = detect_faces(frame, known_face_paths, known_face_names)

# # #         # Display the resulting image with bounding boxes and labels
# # #         if face_names:
# # #             # Print message only once per detection
# # #             if face_names[0] != last_detected_name:
# # #                 print(f"Hello, {face_names[0]}!")  # Print the greeting message
# # #                 last_detected_name = face_names[0]  # Update last detected name

# # #         cv2.imshow('Video', frame)

# # #         # Hit 'q' on the keyboard to quit
# # #         if cv2.waitKey(1) & 0xFF == ord('q'):
# # #             break

# # #     # Release handle to the webcam
# # #     video_capture.release()
# # #     cv2.destroyAllWindows()

# # # if __name__ == "__main__":
# # #     main()


# # # import cv2
# # # from deepface import DeepFace
# # # import os

# # # def detect_faces(frame, known_face_paths, known_face_names):
# # #     # Convert the image from BGR color to RGB color
# # #     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# # #     # Initialize an array for names of detected faces
# # #     face_names = []

# # #     # Perform face detection and verification
# # #     for known_face_path, known_face_name in zip(known_face_paths, known_face_names):
# # #         result = DeepFace.verify(known_face_path, rgb_frame)

# # #         if result["verified"]:
# # #             face_names.append(known_face_name)

# # #     return face_names

# # # def main():
# # #     # Initialize the webcam
# # #     video_capture = cv2.VideoCapture(0)
# # #     video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # Decrease frame width
# # #     video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # Decrease frame height

# # #     # Set the directory for known faces
# # #     known_faces_dir = "known_faces"

# # #     # Load known faces and their names
# # #     known_face_paths = []
# # #     known_face_names = []

# # #     # Iterate through each user folder in the known_faces_dir
# # #     for user_name in os.listdir(known_faces_dir):
# # #         user_dir = os.path.join(known_faces_dir, user_name)
# # #         if os.path.isdir(user_dir):
# # #             for image_name in os.listdir(user_dir):
# # #                 image_path = os.path.join(user_dir, image_name)
# # #                 known_face_paths.append(image_path)
# # #                 known_face_names.append(user_name)

# # #     last_detected_name = None  # Initialize last detected name
# # #     is_detecting_face = False  # Flag to track face detection status

# # #     while True:
# # #         # Capture a single frame of video
# # #         ret, frame = video_capture.read()

# # #         # Flip the frame horizontally (to correct mirroring)
# # #         frame = cv2.flip(frame, 1)

# # #         # Detect faces in the frame only if not currently detecting face
# # #         if not is_detecting_face:
# # #             face_names = detect_faces(frame, known_face_paths, known_face_names)
# # #             if face_names:
# # #                 # Print message only once per detection
# # #                 if face_names[0] != last_detected_name:
# # #                     print(f"Hello, {face_names[0]}!")  # Print the greeting message
# # #                     last_detected_name = face_names[0]  # Update last detected name
# # #                 is_detecting_face = True  # Set flag to indicate face detection is in progress

# # #         cv2.imshow('Video', frame)

# # #         # Reset face detection flag if no face is detected
# # #         if not face_names:
# # #             is_detecting_face = False

# # #         # Hit 'q' on the keyboard to quit
# # #         if cv2.waitKey(1) & 0xFF == ord('q'):
# # #             break

# # #     # Release handle to the webcam
# # #     video_capture.release()
# # #     cv2.destroyAllWindows()

# # # if __name__ == "__main__":
# # #     main()


# import cv2
# import eel
# import base64
# from deepface import DeepFace
# from speak import *

# # Set the directory for known faces
# KNOWN_FACES_DIR = "known_faces"

# eel.init('gui')  # Initialize Eel with the assets directory

# @eel.expose
# def detect_faces(frame):
#     # Convert the image from BGR color to RGB color
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Initialize an array for names of detected faces
#     face_names = []

#     try:
#         # Perform face detection and verification
#         for known_face_path, known_face_name in zip(known_face_paths, known_face_names):
#             result = DeepFace.verify(known_face_path, rgb_frame)

#             if result["verified"]:
#                 face_names.append(known_face_name)
#                 speak(f"Face detected successfully. Welcome {known_face_name}")
                

#     except Exception as e:
#         print("Error during face detection:", e)

#     return face_names

# @eel.expose
# def capture_frames():
#     video_capture = cv2.VideoCapture(0)
#     while True:
#         ret, frame = video_capture.read()
#         if not ret:
#             break
#         else:
#             # Perform face detection on the frame
#             detected_faces = detect_faces(frame)
#             # Draw bounding boxes around detected faces
#             for face_name in detected_faces:
#                 cv2.putText(frame, face_name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#             # Convert the frame to base64 string
#             _, buffer = cv2.imencode('.jpg', frame)
#             frame_base64 = base64.b64encode(buffer).decode()
#             # Send the frame to the frontend
#             eel.updateFrame(frame_base64)()

# # Load known faces and their names
# known_face_paths = []
# known_face_names = []

# # Iterate through each user folder in the known_faces_dir
# for user_name in os.listdir(KNOWN_FACES_DIR):
#     user_dir = os.path.join(KNOWN_FACES_DIR, user_name)
#     if os.path.isdir(user_dir):
#         for image_name in os.listdir(user_dir):
#             image_path = os.path.join(user_dir, image_name)
#             known_face_paths.append(image_path)
#             known_face_names.append(user_name)

# # Run the Eel app
# eel.start('facedetection.html', size=(800, 600), block=False)

# capture_frames()

# import os
# import cv2
# import base64
# import time
# import eel
# from deepface import DeepFace
# import numpy as np
# from speak import *

# # Set the directory for known faces
# KNOWN_FACES_DIR = "known_faces"

# eel.init('assets')  # Initialize Eel with the assets directory

# def load_known_faces(known_faces_dir):
#     known_face_paths = []
#     known_face_names = []
#     for user_name in os.listdir(known_faces_dir):
#         user_dir = os.path.join(known_faces_dir, user_name)
#         if os.path.isdir(user_dir):
#             for image_name in os.listdir(user_dir):
#                 image_path = os.path.join(user_dir, image_name)
#                 known_face_paths.append(image_path)
#                 known_face_names.append(user_name)
#     return known_face_paths, known_face_names

# @eel.expose
# def detect_faces(frame_base64):
#     # Decode the base64 frame
#     frame_data = base64.b64decode(frame_base64)
#     frame = cv2.imdecode(np.frombuffer(frame_data, np.uint8), cv2.IMREAD_COLOR)
    
#     # Convert the image from BGR color to RGB color
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Initialize an array for names of detected faces
#     face_names = []

#     try:
#         known_face_paths, known_face_names = load_known_faces(KNOWN_FACES_DIR)
#         # Perform face detection and verification
#         for known_face_path, known_face_name in zip(known_face_paths, known_face_names):
#             result = DeepFace.verify(known_face_path, rgb_frame)
#             if result["verified"]:
#                 face_names.append(known_face_name)

#     except Exception as e:
#         print("Error during face detection:", e)
#         return []

#     # Draw bounding boxes and labels around detected faces
#     for face_name in face_names:
#         cv2.putText(frame, face_name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

#     # Encode the frame back to base64
#     _, buffer = cv2.imencode('.jpg', frame)
#     frame_base64 = base64.b64encode(buffer).decode()
    
#     # Update the frame in the frontend
#     eel.updateFrame(frame_base64)

#     # Return detected face names
#     return face_names

# def capture_frames():
#     video_capture = cv2.VideoCapture(0)
#     detected_faces = []
#     while True:
#         ret, frame = video_capture.read()
#         if not ret:
#             break
#         else:
#             # Perform face detection on the frame
#             detected_faces = detect_faces(cv2.imencode('.jpg', frame)[1].tobytes())
#             if detected_faces:
#                 # Display the frame for 2-3 seconds if faces are detected
#                 speak(f"Face detection successful. Welcome {detected_faces}")
#                 time.sleep(2)
#                 break

#     video_capture.release()
#     cv2.destroyAllWindows()
#     print(f"Detected faces: {detected_faces}")

# # Run the Eel app
# def main():
#     eel.start('facedetection.html', size=(800, 600), block=False)
#     capture_frames()
#     time.sleep(3)  # Wait for 3 seconds before closing the app
#     eel.close_window()

# if __name__ == "__main__":
#     main()

# import os
# import cv2
# import base64
# import time
# import eel
# from deepface import DeepFace
# import numpy as np

# # Set the directory for known faces
# KNOWN_FACES_DIR = "known_faces"

# eel.init('gui')  # Initialize Eel with the assets directory

# def load_known_faces(known_faces_dir):
#     known_face_paths = []
#     known_face_names = []
#     for user_name in os.listdir(known_faces_dir):
#         user_dir = os.path.join(known_faces_dir, user_name)
#         if os.path.isdir(user_dir):
#             for image_name in os.listdir(user_dir):
#                 image_path = os.path.join(user_dir, image_name)
#                 known_face_paths.append(image_path)
#                 known_face_names.append(user_name)
#     return known_face_paths, known_face_names

# @eel.expose
# def detect_faces(frame_base64):
#     # Decode the base64 frame
#     frame_data = base64.b64decode(frame_base64)
#     frame = cv2.imdecode(np.frombuffer(frame_data, np.uint8), cv2.IMREAD_COLOR)

#     if frame is None or frame.size == 0:
#         print("Error: Empty frame received.")
#         return []

#     # Convert the image from BGR color to RGB color
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Initialize an array for names of detected faces
#     face_names = []

#     try:
#         known_face_paths, known_face_names = load_known_faces(KNOWN_FACES_DIR)
#         # Perform face detection and verification
#         for known_face_path, known_face_name in zip(known_face_paths, known_face_names):
#             result = DeepFace.verify(known_face_path, rgb_frame)
#             if result["verified"]:
#                 face_names.append(known_face_name)

#     except Exception as e:
#         print("Error during face detection:", e)
#         return []

#     # Draw bounding boxes and labels around detected faces
#     for face_name in face_names:
#         cv2.putText(frame, face_name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

#     # Encode the frame back to base64
#     _, buffer = cv2.imencode('.jpg', frame)
#     frame_base64 = base64.b64encode(buffer).decode()
    
#     # Update the frame in the frontend
#     eel.updateFrame(frame_base64)

#     # Return detected face names
#     return face_names

# def capture_frames():
#     video_capture = cv2.VideoCapture(0)
#     detected_faces = []
#     while True:
#         ret, frame = video_capture.read()
#         if not ret:
#             print("Error: Failed to capture frame.")
#             break

#         # Encode frame to base64
#         _, buffer = cv2.imencode('.jpg', frame)
#         frame_base64 = base64.b64encode(buffer).decode()

#         # Perform face detection on the frame
#         detected_faces = detect_faces(frame_base64)
#         if detected_faces:
#             # Display the frame for 2-3 seconds if faces are detected
#             time.sleep(2)
#             break

#     video_capture.release()
#     cv2.destroyAllWindows()
#     print(f"Detected faces: {detected_faces}")

# # Run the Eel app
# def main():
#     eel.start('facedetection.html', size=(800, 600))
#     capture_frames()
#     time.sleep(3)  # Wait for 3 seconds before closing the app
#     eel.close_window()

# if __name__ == "__main__":
#     main()







# # #From hereeee-----------------

# import cv2
# from deepface import DeepFace
# import os
# from speak import speak

# def detect_faces(frame, known_face_paths, known_face_names, last_detected_names):
#     # Convert the image from BGR color to RGB color
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Initialize an array for names of detected faces
#     face_names = []

#     try:
#         if not last_detected_names:
#             # Perform face detection and verification
#             for known_face_path, known_face_name in zip(known_face_paths, known_face_names):
#                 result = DeepFace.verify(known_face_path, rgb_frame)

#                 if result["verified"]:
#                     face_names.append(known_face_name)
#         else:
#             # Check if new faces are detected
#             new_face_detected = False
#             for known_face_path, known_face_name in zip(known_face_paths, known_face_names):
#                 if known_face_name not in last_detected_names:
#                     result = DeepFace.verify(known_face_path, rgb_frame)

#                     if result["verified"]:
#                         face_names.append(known_face_name)
#                         new_face_detected = True
#                         break
            
#             if not new_face_detected:
#                 # No new faces detected, return empty list
#                 return []

#     except Exception as e:
#         # print("Error during face detection:", e)
#         return

#     return face_names

# def main():
#     # Initialize the webcam
#     video_capture = cv2.VideoCapture(0)
#     video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # Decrease frame width
#     video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # Decrease frame height

#     # Set the directory for known faces
#     known_faces_dir = "known_faces"

#     # Load known faces and their names
#     known_face_paths = []
#     known_face_names = []

#     # Iterate through each user folder in the known_faces_dir
#     for user_name in os.listdir(known_faces_dir):
#         user_dir = os.path.join(known_faces_dir, user_name)
#         if os.path.isdir(user_dir):
#             for image_name in os.listdir(user_dir):
#                 image_path = os.path.join(user_dir, image_name)
#                 known_face_paths.append(image_path)
#                 known_face_names.append(user_name)

#     last_detected_names = []  # Initialize last detected names

#     while True:
#         # Capture a single frame of video
#         ret, frame = video_capture.read()

#         if not ret:
#             print("Error: Failed to capture frame.")
#             break

#         # Flip the frame horizontally (to correct mirroring)
#         frame = cv2.flip(frame, 1)

#         # Detect faces in the frame
#         face_names = detect_faces(frame, known_face_paths, known_face_names, last_detected_names)

#         if face_names:
#             speak(f"Hello, {', '.join(face_names)}!")
#             last_detected_names = face_names

#         cv2.imshow('Video', frame)

#         # Hit 'q' on the keyboard to quit
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release handle to the webcam
#     video_capture.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()






import eel
import cv2
import face_recognition
import os
import numpy as np

# Initialize Eel with the web folder
eel.init('gui')

# Load known faces
known_face_encodings = []
known_face_names = []

known_faces_dir = 'known_faces'
for user_folder in os.listdir(known_faces_dir):
    user_folder_path = os.path.join(known_faces_dir, user_folder)
    if os.path.isdir(user_folder_path):
        for filename in os.listdir(user_folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image = face_recognition.load_image_file(os.path.join(user_folder_path, filename))
                encoding = face_recognition.face_encodings(image)[0]
                known_face_encodings.append(encoding)
                known_face_names.append(user_folder)

# Start the video capture
video_capture = cv2.VideoCapture(0)

@eel.expose
def start_face_recognition():
    while True:
        ret, frame = video_capture.read()
        print("Frame captured:", ret)
        if not ret:
            continue
             # Flip the frame horizontally
        frame = cv2.flip(frame, 1)
        
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

eel.start('facedetection.html')
eel.startFaceRecognition()
