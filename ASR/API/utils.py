
import uuid
import os

def get_tts_media(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'tts_audio/{}{}'.format(uuid.uuid4(), ext)

def get_asr_media(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'asr_audio/{}{}'.format(uuid.uuid4(), ext)