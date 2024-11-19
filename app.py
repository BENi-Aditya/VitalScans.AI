from flask import Flask, request, render_template, url_for, jsonify
from PIL import Image, ImageDraw, ImageFont
import os
from inference_sdk import InferenceHTTPClient
from datetime import datetime
from chatbot import chatbot


# Initialize Flask App
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Initialize RoboFlow Client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="hjCFUfsJBCSxi8KzP8yC"
)
MODEL_ID = "pneumonia-itjkr/2"  # Update this with your exact model version

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Make prediction with RoboFlow
        result = CLIENT.infer(filepath, model_id=MODEL_ID)
        predictions = result["predictions"]
        
        # Draw predictions on the image
        result_image_path = draw_predictions(filepath, predictions)

        return render_template(
            'result.html', 
            original_image=url_for('static', filename=f'uploads/{file.filename}'),
            result_image=url_for('static', filename=f'results/{os.path.basename(result_image_path)}'),
            predictions=predictions
        )

def draw_predictions(image_path, predictions):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    for pred in predictions:
        x, y, width, height = pred["x"], pred["y"], pred["width"], pred["height"]
        confidence = pred["confidence"]
        label = pred["class"]

        # Calculate bounding box
        left = x - width / 2
        top = y - height / 2
        right = x + width / 2
        bottom = y + height / 2

        # Draw bounding box
        draw.rectangle([left, top, right, bottom], outline="red", width=3)

        # Add label and confidence
        text = f"{label}: {confidence:.2%}"
        draw.text((left, top - 10), text, fill="red", font=font)

    # Save result
    result_image_path = os.path.join(RESULT_FOLDER, os.path.basename(image_path))
    image.save(result_image_path)
    return result_image_path

@app.route('/ask_chatgpt', methods=['POST'])
def ask_chatgpt():
    question = request.form['question']
    prediction = request.form['prediction']
    confidence = request.form['confidence']
    
    context = f"The user's chest X-ray scan has been analyzed, and the prediction is {prediction} with a confidence of {confidence}%. "
    
    response = chatbot.get_response(context + question)
    return jsonify({'answer': response})

if __name__ == '__main__':
    app.run(debug=True)
