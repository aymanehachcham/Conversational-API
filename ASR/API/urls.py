
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings


app_name = 'API'

urlpatterns = [
    path(r'test', views.test_api, name='test_api_communication'),
    path(r'asr/', views.asr_conversion),
    path(r'tts/', views.tts_transcription)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)