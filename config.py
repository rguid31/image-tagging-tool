import os

from dotenv import load_dotenv
from transformers import CLIPModel, CLIPProcessor

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is not set. Copy .env.example to .env and add your API key."
    )

CLIP_MODEL_NAME = "openai/clip-vit-base-patch32"

try:
    model = CLIPModel.from_pretrained(CLIP_MODEL_NAME)
    processor = CLIPProcessor.from_pretrained(CLIP_MODEL_NAME)
except Exception as exc:
    raise RuntimeError(f"Unable to load CLIP model '{CLIP_MODEL_NAME}': {exc}") from exc
