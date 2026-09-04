import json
import os

from description import generate_description
from tagging import generate_tags

SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png")


def batch_process_images(image_folder, output_file="image_metadata.json"):
    """Process supported images in a folder and write metadata to JSON."""
    if not os.path.isdir(image_folder):
        raise FileNotFoundError(f"Image folder not found: {image_folder}")

    output_data = []

    for image_file in sorted(os.listdir(image_folder)):
        if image_file.lower().endswith(SUPPORTED_EXTENSIONS):
            image_path = os.path.join(image_folder, image_file)
            tags = generate_tags(image_path)
            description = generate_description(tags)
            output_data.append(
                {
                    "filename": image_file,
                    "tags": tags,
                    "description": description,
                }
            )

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(output_data, json_file, indent=2, ensure_ascii=False)

    print(f"Processed {len(output_data)} image(s). Metadata saved to {output_file}.")
    return output_data
