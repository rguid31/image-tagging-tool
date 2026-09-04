from openai import OpenAI

from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_description(tags):
    """Generate a concise metadata description from CLIP-ranked tags."""
    prompt = (
        "Write a concise stock-photo metadata description using only the information "
        f"contained in these tags: {', '.join(tags)}. "
        "Do not invent specific people, objects, locations, actions, or scene details "
        "that are not supported by the tags."
    )

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You write accurate, concise image metadata from supplied tags. "
                    "Avoid unsupported visual details."
                ),
            },
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content.strip()
