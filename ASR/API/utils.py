
import uuid
import os

def get_path_media(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'audio/{}{}'.format(uuid.uuid4(), ext)

def get_path_media_audio_transformation(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'audio_transformation/{}{}'.format(uuid.uuid4(), ext)