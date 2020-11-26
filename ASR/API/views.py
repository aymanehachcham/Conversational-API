from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.cache import never_cache
from Bert_NLP.bert_loader import Bert_loader
from Quartznet_ASR.quartznet_loader import Quartznet_loader
from TTS_ESPnet.tts_loader import TTS_loader
from scipy.io.wavfile import write
from .models import Sound
from .serializers import SoundSerializerOut

from .models import ASRSound
import time
import uuid

# Load NLP and ASR Nemo alongside with Tacotron Model
# bert_punctuator = Bert_loader()
# quartznet_asr =Quartznet_loader()
# tacotron2_tts = TTS_loader()


#Create your views here.
@api_view(['GET'])
@never_cache
def test_api(request):
    # ----- YAML below for Swagger -----
    """
    description: Test for the Peer API.
    parameters:
      - name: None
    """
    ...
    return Response({'response':"You are successfully connected to Peer API"})

# @api_view(['POST'])
# def asr_conversion(request):
#     # ----- YAML below for Swagger -----
#     """
#     description: ASR Conversion from Quartznet model
#     parameters:
#       - name: audio FILE
#         type: FILE
#         required: true
#         location: form
#     :returns
#         - text processed from an ASR model
#     """
#     data = request.FILES['audio']
#     audio = ASRSound.objects.create(audio_file=data)
#     input = audio.audio_file.path
#     file = [input]
#     #json_manifest = quartznet_asr.create_output_manifest(audio.audio_file.path)
#     # transcription = quartznet_asr.covert_to_text(file)
#     # well_formated = bert_punctuator.punctuate(transcription)
#
#     return Response({'Output': well_formated})

# @api_view(['POST'])
# def tts_transcription(request):
#     # ----- YAML below for Swagger -----
#     """
#     description: TTS Transcription from Tacotron2 and Parallel Wavegan models
#     parameters:
#       - name: text input
#         type: string
#         required: true
#         location: form
#     :returns
#         - wav audio file interpreting the text with a female voice
#     """
#     start_time = time.time()
#     text = request.data.get('text')
#     num_generated = uuid.uuid1()
#     print(' id num_generated for audio &&&&&&&&&&&&&&&&&&&&&&&&&&&')
#     path = "Audio/sound_output_%02d.wav" % num_generated
#     rate = 22050
#
#     output_audio = tacotron2_tts.tts_inference(text)
#     write(path, int(rate), output_audio)
#     audio = Sound.objects.create(audio_join=path, name='Sound_%02d' % num_generated, text_content=text)
#     audio.converted = True
#     audio.inference_time = str((time.time() - start_time))
#     audio.save()
#     ok = True
#     print("--- %s seconds ---" % (time.time() - start_time))
#     serializer = SoundSerializerOut(audio)
#     if ok == True:
#         return Response(serializer.data)
#     return Response({'response': "Sorry, we can't succeed to convert your text to sound!"})