from deepface import DeepFace

def analyze_image_emotion(image_path):
    try:
        # Analyze the image for emotions. The analyze function will return several details, including emotion.
        analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'])
        dominant_emotion = analysis[0]["dominant_emotion"]
        
        print(f"Dominant Emotion: {dominant_emotion}")
        
        return dominant_emotion
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
image_path = 'path/to/your/image.jpg'  # Update this path to your image's path
dominant_emotion = analyze_image_emotion("/Users/akashkhanna/Desktop/testImage.jpeg")
