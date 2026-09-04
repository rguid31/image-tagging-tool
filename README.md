# AI Image Tagging and Description Tool

A small Python portfolio project that generates structured image metadata by combining CLIP-based tag ranking with OpenAI-generated descriptions.

The tool processes images from a local folder, ranks a fixed vocabulary of candidate tags using the `openai/clip-vit-base-patch32` model, then uses the selected tags as context for an OpenAI API request. Results are written to JSON for reuse in metadata, organization, and publishing workflows.

## What it does

1. Loads `.jpg`, `.jpeg`, and `.png` files from the `images/` directory.
2. Uses CLIP embeddings to rank candidate tags for each image.
3. Sends the highest-ranked tags to the OpenAI API to generate a concise stock-photo-style metadata description.
4. Saves the filename, tags, and description to `image_metadata.json`.

## Tech stack

- Python
- PyTorch
- Hugging Face Transformers
- CLIP (`openai/clip-vit-base-patch32`)
- Pillow
- OpenAI API
- python-dotenv

## Local setup

1. Clone the repository:

```bash
git clone https://github.com/rguid31/image-tagging-tool.git
cd image-tagging-tool
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows, activate it with:

```powershell
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a local environment file:

```bash
cp .env.example .env
```

Add your OpenAI API key to `.env`:

```text
OPENAI_API_KEY=your_api_key_here
```

5. Add images to the `images/` directory and run:

```bash
python main.py
```

The generated metadata is written to `image_metadata.json`.

## Important limitation

This is a portfolio prototype rather than a production image-captioning system. CLIP ranks images against a predefined candidate-tag list, and the OpenAI model receives those selected tags rather than the original image pixels. The generated description is therefore tag-derived and may not capture every image-specific detail.

Unsplash upload automation is not currently implemented.

## Project status

Portfolio prototype. The repository is maintained as an example of applied AI, Python, structured-data generation, and API integration.

## Author

Ryan Guidry

- Portfolio: https://ryanguidry.com
- LinkedIn: https://www.linkedin.com/in/rmguidry
- GitHub: https://github.com/rguid31
