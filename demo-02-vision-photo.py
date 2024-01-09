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
    _image_path = f"media/{_image}"

    # Getting the base64 string
    base64_image = encode_image(_image_path)

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

    # Image Description: useful for captioning
    image = "lake.png"
    prompt = "What’s in this image?"

    # Reding the text from an image containing a handwritten note
    # image = "handwritten_note_et.jpeg"
    # image = "handwritten_note_et_90d.jpeg"
    # prompt = "What’s in this image?"

    # Reading the text from an image containing a note written by a child
    # image = "handwritten_child.jpg"
    # prompt = "What is written in this note? What could it be about? Transcribe, translate, and explain the note."

    # Reading a doctor's handwriting
    # image = 'handwritten_doctor.jpg'
    # prompt = "What is written in this note? Transcript and translate if not in english. \
    #           Explain what it could be about. What's your opinion about this handwriting?"

    # Retrieving elements from an image and creating something new
    #image = 'fridge.jpeg'
    #prompt = "what do you see in my fridge?"
    # prompt = "what do you see in my fridge? List everything you see. Hint: we are vegetarians and have diabetes." \
    #            "Suggest a meal that I can cook with these ingredients."

    # Reading and translating a scientific paper from a magazine
    # image = 'medical_article_p1.jpeg'
    # prompt = "What is in the image? Can you transcribe the text and summarize it?"

    response = generate_caption(prompt, image)
    pprint(response['choices'][0]['message']['content'])