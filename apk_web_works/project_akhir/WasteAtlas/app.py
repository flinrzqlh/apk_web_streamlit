from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import os
import torch
import torchvision.transforms as transforms
from PIL import Image
import torch.nn.functional as F
import torch.nn as nn
import torchvision.models as models
import base64
from io import BytesIO

class WasteAtlasCNN(nn.Module):
    def __init__(self, num_classes=10):
        super(WasteAtlasCNN, self).__init__()
        self.model = models.resnet50(pretrained=True)
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, num_classes)

    def forward(self, x):
        return self.model(x)

app = Flask(__name__)
# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Class labels
WASTE_CLASSES = ['battery', 'biological', 'cardboard', 'clothes', 'glass', 'metal', 'paper', 'plastic', 'shoes', 'trash']

# Load the model (assuming you have your trained model saved)
def load_model():
    model = WasteAtlasCNN(num_classes=10)  # Initialize your model architecture
    model.load_state_dict(torch.load('best_cnn_model.pth', map_location=torch.device('cpu')))
    model.eval()
    return model

model = load_model()

# Image preprocessing
def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image_tensor = transform(image)
    return image_tensor.unsqueeze(0)  # Add batch dimension

# Predict function
def predict_waste(image):
    input_tensor = preprocess_image(image)
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = F.softmax(output, dim=1)
        pred_class = torch.argmax(output, dim=1).item()
        confidence = probabilities[0][pred_class].item() * 100
    return WASTE_CLASSES[pred_class], confidence

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/types')
def types():
    return render_template('types.html')

@app.route('/battery')
def battery():
    return render_template('battery.html')

@app.route('/biological')
def biological():
    return render_template('biological.html')

@app.route('/cardboard')
def cardboard():
    return render_template('cardboard.html')

@app.route('/clothes')
def clothes():
    return render_template('clothes.html')

@app.route('/glass')
def glass():
    return render_template('glass.html')

@app.route('/metal')
def metal():
    return render_template('metal.html')

@app.route('/paper')
def paper():
    return render_template('paper.html')

@app.route('/plastic')
def plastic():
    return render_template('plastic.html')

@app.route('/shoes')
def shoes():
    return render_template('shoes.html')

@app.route('/trash')
def trash():
    return render_template('trash.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/photo')
def photo():
    return render_template('photo.html')

@app.route('/capture', methods=['POST'])
def capture():
    try:
        data = request.get_json()
        image_data = data['image'].split(',')[1]
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes)).convert('RGB')
        
        # Save the captured image
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'captured_image.png')
        image.save(image_path)
        
        # Make prediction
        waste_type, confidence = predict_waste(image)
        
        return jsonify({
            'success': True,
            'waste_type': waste_type,
            'confidence': confidence,
            'filename': 'captured_image.png'
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/image', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Process the image and make a prediction
            try:
                waste_type, confidence = predict_waste(Image.open(file_path).convert('RGB'))
                return render_template('image.html', filename=filename, waste_type=waste_type, confidence=confidence)
            except Exception as e:
                return render_template('image.html', message=f'Error during prediction: {str(e)}')

    return render_template('image.html')

@app.route('/delete', methods=['POST'])
def delete_file():
    filename = request.form['filename']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return render_template('image.html')
    else:
        return render_template('image.html')

if __name__ == '__main__':
    app.run(debug=True)