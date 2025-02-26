import os
from dotenv import load_dotenv

import openai
from transformers import CLIPProcessor, CLIPModel

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Validate API Key
if not openai.api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY in the .env file.")

# Load CLIP Model and Processor
try:
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
except Exception as e:
    raise RuntimeError(f"Error loading CLIP model: {e}")

print("✅ Configuration loaded successfully.")