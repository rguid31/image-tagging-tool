import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
from config import model, processor

# Keywords for tagging
KEYWORDS = ["minimalism", "moody", "soft light", "introspective", "nature", 
            "pastel colors", "monochrome", "cozy", "adventure", "mental health", 
            "travel", "serene", "nighttime", "vintage", "hazy", "bright"]

def process_image(image_path):
    """Loads and preprocesses an image for tagging."""
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    return inputs

def generate_tags(image_path):
    """Generates AI-powered tags for an image."""
    image = process_image(image_path)
    text_inputs = processor(text=KEYWORDS, return_tensors="pt", padding=True)

    with torch.no_grad():
        image_features = model.get_image_features(**image)
        text_features = model.get_text_features(**text_inputs)

    similarities = (image_features @ text_features.T).squeeze()
    top_matches = torch.argsort(similarities, descending=True)[:15]

    return [KEYWORDS[i] for i in top_matches]