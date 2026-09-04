import torch
from PIL import Image

from config import model, processor

KEYWORDS = [
    "minimalism",
    "moody",
    "soft light",
    "introspective",
    "nature",
    "pastel colors",
    "monochrome",
    "cozy",
    "adventure",
    "mental health",
    "travel",
    "serene",
    "nighttime",
    "vintage",
    "hazy",
    "bright",
]

TOP_K = 5


def process_image(image_path):
    """Load and preprocess an image for CLIP feature extraction."""
    with Image.open(image_path) as source_image:
        image = source_image.convert("RGB")
        return processor(images=image, return_tensors="pt")


def generate_tags(image_path):
    """Rank candidate tags for an image using cosine similarity in CLIP space."""
    image_inputs = process_image(image_path)
    text_inputs = processor(text=KEYWORDS, return_tensors="pt", padding=True)

    with torch.no_grad():
        image_features = model.get_image_features(**image_inputs)
        text_features = model.get_text_features(**text_inputs)

    image_features = image_features / image_features.norm(dim=-1, keepdim=True)
    text_features = text_features / text_features.norm(dim=-1, keepdim=True)

    similarities = (image_features @ text_features.T).squeeze(0)
    top_matches = torch.argsort(similarities, descending=True)[: min(TOP_K, len(KEYWORDS))]

    return [KEYWORDS[index] for index in top_matches.tolist()]
