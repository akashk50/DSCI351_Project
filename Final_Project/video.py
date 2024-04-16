import cv2
import time
from deepface import DeepFace

def process_frame(frame):
    try:
        # Convert the color space from BGR to RGB because DeepFace expects RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Analyze the image for emotions and get the first result since DeepFace.analyze returns a list
        analysis = DeepFace.analyze(frame_rgb, actions=['emotion'], enforce_detection=False)
        
        # Extracting the dominant emotion
        dominant_emotion = analysis[0]['dominant_emotion']
        print(f"Dominant Emotion: {dominant_emotion}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return frame


def capture_video(fps=1):
    max_length = 3
    curr_length = 0
    cap = cv2.VideoCapture(1)
    
    if not cap.isOpened():
        print("Error: Could not open video capture device.")
        return
    
    prev_frame_time = time.time()

    try:
        while curr_length < max_length:
            ret, frame = cap.read()
            if not ret:
                print("Error: Can't receive frame (stream end?). Exiting ...")
                break

            curr_frame_time = time.time()

            if (curr_frame_time - prev_frame_time) > 1/fps:
                processed_frame = process_frame(frame)
                prev_frame_time = curr_frame_time
                curr_length += 1
            else:
                processed_frame = frame

            cv2.imshow('Live Video', processed_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

capture_video(fps=1)