from pprint import pprint

import pyttsx3 as pyttsx3

import cv2  # We're using OpenCV to read video, to install !pip install opencv-python
import vlc # We're using OpenCV to read video, to install !pip install python-vlc
import base64
import time
from openai import OpenAI


def generate_caption_video(_prompt, _input_video, max_tokens=200, base_frames=50):

    client = OpenAI()
    _video = cv2.VideoCapture(f"media/{_input_video}")

    base64Frames = []
    while _video.isOpened():
        success, frame = _video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

    _video.release()
    print(len(base64Frames), "frames read.")

    prompt_messages = [
        {
            "role": "user",
            "content": [
                _prompt,
                *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::base_frames]),
            ],
        },
    ]
    params = {
        "model": "gpt-4-vision-preview",
        "messages": prompt_messages,
        "max_tokens": max_tokens,
    }

    result = client.chat.completions.create(**params)
    return result


def generate_audio(_transcript):
    client = OpenAI()

    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=_transcript,
    )
    return response


if __name__ == '__main__':

    # 1. Writing a story based on a short film
    video = "star_wars_stop_motion.mp4"
    # prompt = "These are frames from a video that I want to upload. Generate a compelling description \
    # that I can upload along with the video."
    # video_description = generate_caption_video(prompt, video, max_tokens=200, base_frames=50)
    # pprint(video_description.choices[0].message.content)

    # 2. Use voice narration to describe what is happening on the video
    prompt_narration = "These are frames of a starwars video. Create a short voiceover script in the style of " \
                        "David Attenborough. Only include the narration."

    #Vision -- generate a text
    video_narration = generate_caption_video(prompt_narration, video, max_tokens=200, base_frames=60)
    video_narration_txt = video_narration.choices[0].message.content
    pprint(video_narration_txt)

    # Text-to-speech -- generate an audio file from the text + play it
    audio_file = "starwars_stop_motion.mp3"
    audio = generate_audio(video_narration_txt)
    audio.stream_to_file(f"media/{audio_file}")
    sound_file = vlc.MediaPlayer(f"media/{audio_file}")
    sound_file.play()
    time.sleep(200)







