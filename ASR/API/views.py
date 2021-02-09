from drf_yasg.openapi import Parameter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.cache import never_cache
from Bert_NLP.bert_loader import Bert_loader
from Quartznet_ASR.quartznet_loader import Quartznet_loader
from TTS_ESPnet.tts_loader import TTS_loader
from scipy.io.wavfile import write
from rest_framework import status

from .serializers import TTSOutputSerializer, ASROutputSeralizer

from .models import TTSSound, ASRInputSound, ASRText
import time
import uuid
import os
import shutil

# Load NLP and ASR Nemo alongside with Tacotron Model
bert_punctuator = Bert_loader()
quartznet_asr =Quartznet_loader()
tacotron2_tts = TTS_loader()
ASR_SAMPLING_RATE = 22050


# Post method for ASR transcription
@api_view(['POST'])
def asr_conversion(request):
    data = request.FILES['audio']

    audio = ASRInputSound.objects.create(audio_file=data)

    file = [audio.audio_file.path]
    start_time = time.time()
    transcription = quartznet_asr.covert_to_text(file)
    well_formatted = bert_punctuator.punctuate(transcription)

    text = ASRText.objects.create(
        name='ASR_Text_%02d' % uuid.uuid1(),
        Output=well_formatted,
        inference_time=str((time.time() - start_time)),
        audio_join_Transformed=audio.audio_file.path
    )

    serializer = ASROutputSeralizer(text)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Post method for TTS audio generation
@api_view(['POST'])
def tts_transcription(request):
    text = request.data.get('text')
    tts_id = uuid.uuid1()
    path = "Audio/tts_output_%02d.wav" % tts_id

    start_time = time.time()
    output_audio = tacotron2_tts.tts_inference(text)

    write(path, int(ASR_SAMPLING_RATE), output_audio)
    audio = TTSSound.objects.create(
        audio_join=path,
        name='Sound_%02d' % tts_id,
        text_content=text,
        inference_time=str((time.time() - start_time))
    )

    audio.save()
    serializer = TTSOutputSerializer(audio)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Empty the local folder when they get full of messy audio files
def empty_folder(request):
    folder_input = 'Audio/'
    for filename in os.listdir(folder_input):
        file_path = os.path.join(folder_input, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    folder_output = 'ASR_Input/'
    for filename in os.listdir(folder_output):
        file_path = os.path.join(folder_output, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    return Response({'response': "Media folders were cleaned up!!"})