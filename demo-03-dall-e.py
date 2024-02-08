"""
This program uses the OPENAI API to classify news articles and obtain the answer in JSON format
"""
from openai import OpenAI
import pprint


def api_call_generate_image(_prompt, _size, _quality):
    client = OpenAI()

    _response = client.images.generate(
        model="dall-e-3",
        prompt=_prompt,
        size=_size,
        quality=_quality,
        n=1,
    )

    image_url = _response.data[0].url
    return image_url


def api_call_edit_image(_prompt, _image, _mask, _size):
    client = OpenAI()

    _response = client.images.edit(
        model="dall-e-2",
        image=open(f"media/{_image}", "rb"),
        mask=open(f"media/{_mask}", "rb"),
        prompt=_prompt,
        n=1,
        size=_size
    )
    image_url = _response.data[0].url
    return image_url


if __name__ == '__main__':

    size = "1024x1024"
    quality = "hd"
    # Image generation with Dall-e-3, use ::w to emphasize words
    prompt = 'Illustration of a spaceship::2 travelling to another galaxy, ' \
             'rendered in the bold and vivid style of a vintage travel poster. No text.'
    response = api_call_generate_image(prompt, size, quality)

    # Editing an image using a mask - Kids at the lake
    prompt_edit_image = 'A beautiful picture of a lake. There are no people.'
    #prompt_edit_image = 'A beautiful picture of a lake. There are no people. Only a flamingo on the shore.'
    image = "lake.png"
    mask = "lake_mask.png"
    response = api_call_edit_image(prompt_edit_image, image, mask, size)


    #Editing an image using a mask - Bride & brother-in-law
    # prompt_edit_image = "A picture of a beautiful bride holding a glass of wine."
    # image = "bride.png"
    # mask = "bride_mask.png"
    # response = api_call_edit_image(prompt_edit_image, image, mask, size)

    pprint.pprint(response, compact=True)






