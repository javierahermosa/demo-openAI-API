import base64
import os
from pprint import pprint

import requests


def generate_caption(_prompt, _image):

    # OpenAI API Key
    api_key = os.getenv('OPENAI_API_KEY')

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Path to your image
    image_path = f"images/{_image}"

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": _prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 500
    }

    _response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return _response.json()


if __name__ == '__main__':

    # Image of kids at the lake
    # prompt = "What’s in this image?"
    # image = "image.png"

    # Hand written note:
    #prompt = "What is written in this note? What could it be about? Transcribe, translate, and explain the note."

    # image = "note_wit.jpg"
    #image = "summary Nikolas.jpg"
    #
    image = 'fridge.jpg'
    prompt = "what do you see in my fridge? List everything you see. Hint: we are vegetarians and have diabetes." \
              "Suggest a meal that I can cook with these ingredients."

    #
    # image = 'doctors_writing.jpg'
    # prompt = "What is written in this note? Transcript and translate if not in english. \
    #           Explain what it could be about. What's your opinion about this font?"
    #
    # image = 'paper_p1.jpg'
    # prompt = "What is in the image? Can you transcribe the text and summarize it?"

    response = generate_caption(prompt, image)
    pprint(response['choices'][0]['message']['content'])



# Response to harry potter note
# ("The note is written in German, and it appears to be a child's writing "
#  'exercise or a creative story. Here is the transcription and translation to '
#  'English:\n'
#  '\n'
#  'Transcription (with corrections to spelling mistakes where context allows):\n'
#  'Kapitel drei\n'
#  'Harry ging zum Einkaufen.\n'
#  '\n'
#  'Danach gingen sie zum See.\n'
#  "In einem Tag hat Harry Potter's Geburtstag.\n"
#  'Harry hatte sich um Auto keine Geduld ge-\n'
#  'macht Harry fand es nicht\n'
#  'toll dass es so nach\n'
#  'Seetang roch. Es regnete. Es war\n'
#  'kalt. Und es war zu unruhig\n'
#  'glaubte er. Es war gefährlich. Und\n'
#  'Buuuum. Ein Riese.\n'
#  '\n'
#  'Translation:\n'
#  'Chapter three\n'
#  'Harry went shopping.\n'
#  '\n'
#  'Afterwards, they went to the lake.\n'
#  "In one day is Harry Potter's birthday.\n"
#  'Harry had no patience for the car.\n'
#  "Harry didn't think it was\n"
#  'great that it smelled so much like\n'
#  'seaweed. It was raining. It was\n'
#  'cold. And it was too restless\n'
#  'he believed. It was dangerous. And\n'
#  'Boom. A giant.\n'
#  '\n'
#  "The content suggests that this might be a child's own interpretation or a "
#  'small fan fiction of the "Harry Potter" series.')