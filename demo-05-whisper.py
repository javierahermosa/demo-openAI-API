"""
This program uses the OPENAI API to classify news articles and obtain the answer in JSON format
"""

from openai import OpenAI
import pprint
import cv2  # We're using OpenCV to read video, to install !pip install opencv-python
import vlc # We're using OpenCV to read video, to install !pip install python-vlc
import base64
import time
from openai import OpenAI


def api_call_transcribe(_audio_input):
    from openai import OpenAI
    client = OpenAI()

    _audio_file = open(f"media/{_audio_input}", "rb")

    _transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=_audio_file,
        response_format="text"
    )
    print("transcribing your audio...")
    return _transcript


def api_call_translate(_audio_input):
    from openai import OpenAI
    client = OpenAI()

    _audio_file = open(f"media/{_audio_input}", "rb")

    _transcript_translated = client.audio.translations.create(
        model="whisper-1",
        file=_audio_file,
        response_format="text"
    )
    return _transcript_translated


def generate_audio(_transcript):
    client = OpenAI()

    response = client.audio.speech.create(
        model="tts-1",
        voice="echo",
        input=_transcript,
    )
    return response


if __name__ == '__main__':

    # 1.  We have recorded an audio file in German, let's listen
    audio_file = "no_more_starwars_german.mp3"
    sound_file = vlc.MediaPlayer(f"media/{audio_file}")
    #sound_file.play()

    # 2. Create a transcript of the audio file
    transcript_txt = api_call_transcribe(audio_file)
    pprint.pprint(transcript_txt, compact=True)

    # 3. Create a translation of the audio file & audio
    translation_txt = api_call_translate(audio_file)
    pprint.pprint(translation_txt, compact=True)

    output_audio_file = "audio_output_translation.mp3"
    audio = generate_audio(translation_txt)
    audio.stream_to_file(f"media/{output_audio_file}")
    sound_file = vlc.MediaPlayer(f"media/{output_audio_file}")
    sound_file.play()
    time.sleep(200)
