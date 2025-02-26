import os
import json
from tagging import generate_tags

from description import generate_description

def batch_process_images(image_folder):
    output_data = []

    for image_file in os.listdir(image_folder):
        if image_file.endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(image_folder, image_file)
            tags = generate_tags(image_path)
            description = generate_description(tags)
            output_data.append({"filename": image_file, "tags": tags, "description": description})

    with open("image_metadata.json", "w") as json_file:
        json.dump(output_data, json_file, indent=4)

    print("Batch processing complete. Data saved to image_metadata.json")