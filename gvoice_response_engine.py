from google.cloud import texttospeech
import error_reporter
from playsound import playsound
import os

def synthesize_text(text):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.types.cloud_tts_pb2.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.cloud_tts_pb2.VoiceSelectionParams(
        language_code='en-US',
        name='en-US-Wavenet-F',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.cloud_tts_pb2.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
    playsound('output.mp3')
    os.remove('output.mp3')