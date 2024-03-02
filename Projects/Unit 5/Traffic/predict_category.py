import cv2
import numpy as np
import sys
import tensorflow as tf

IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43

def load_image(image_path):
    # Load and preprocess the input image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
    img = img / 255.0  # Normalize pixel values
    return np.expand_dims(img, axis=0)  # Add batch dimension

def predict_category(image_path, model):
    # Load the model
    loaded_model = tf.keras.models.load_model(model)

    # Load and preprocess the image
    input_image = load_image(image_path)

    # Make a prediction
    predictions = loaded_model.predict(input_image)

    # Get the predicted category (index with the highest probability)
    predicted_category = np.argmax(predictions)

    return predicted_category

def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python predict_category.py image_path model_path")

    image_path = sys.argv[1]
    model_path = sys.argv[2]

    # Predict the category
    predicted_category = predict_category(image_path, model_path)

    print(f"The predicted category for the given image is: {predicted_category}")

if __name__ == "__main__":
    main()
