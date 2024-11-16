import torch
import monai
from monai.networks.nets import DenseNet121
from monai.transforms import (
    Compose,
    LoadImage,
    ScaleIntensity,
    Resize,
    EnsureChannelFirst
)
from PIL import Image
import numpy as np

class ScanAnalyzer:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self._setup_model()
        self.transforms = self._setup_transforms()

    def _setup_model(self):
        # Initialize the model
        model = DenseNet121(
            spatial_dims=2,
            in_channels=1,
            out_channels=2,  # Binary classification (normal/abnormal)
        ).to(self.device)
        
        # Set model to evaluation mode
        model.eval()
        return model

    def _setup_transforms(self):
        return Compose([
            LoadImage(image_only=True),
            EnsureChannelFirst(),
            ScaleIntensity(),
            Resize((224, 224)),
        ])

    def analyze_scan(self, image_path):
        try:
            # Load and transform the image
            image = self.transforms(image_path)
            
            # Add batch dimension
            image = image.unsqueeze(0).to(self.device)
            
            with torch.no_grad():
                output = self.model(image)
                probabilities = torch.softmax(output, dim=1)
                
            # Get prediction
            prediction = torch.argmax(probabilities, dim=1).item()
            confidence = probabilities[0][prediction].item()

            return {
                'prediction': 'Abnormal' if prediction == 1 else 'Normal',
                'confidence': round(confidence * 100, 2),
                'success': True
            }

        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            } 