
from parallel_wavegan.utils import load_model
from espnet2.bin.tts_inference import Text2Speech
import os.path as path
import torch


TTS_WORK_DIR = "TTS_ESPnet/TTS_Checkpoints/"
VOCODER_WORK_DIR = "TTS_ESPnet/Parallel_Wavegan/"

TTS_MODEL_WEIGHTS = "Tacotron2-199epoch.pth"
TTS_CONFIG_FILE = "config.yaml"

VOCODER_MODEL_WEIGHTS = "checkpoint-1000000steps.pkl"

"""
Handler class that manages Tacotron2 loading files and checkpoints,
implementing all required methods to ease access for other external modules relying
on it.

- Loading yaml configuration files and checkpoints
- Instantiating Text2Speech Espnet core module with specific data parameters
- Define a tts_inference method that takes input text and generates corresponding human audible output.
the voice implemented in this code is the female one. 
"""

class TTS_loader():
    def __init__(self, torch_device=None):
        if torch_device is None:
            if torch.cuda.is_available():
                torch_device = 'cuda'
            else:
                torch_device = 'cpu'

        self.tacotron_file_config = path.join(TTS_WORK_DIR, TTS_CONFIG_FILE)
        self.tacotron_file_checkpoints = path.join(TTS_WORK_DIR, TTS_MODEL_WEIGHTS)

        self.vocoder_file_config = path.join(TTS_WORK_DIR, TTS_CONFIG_FILE)
        self.vocoder_file_checkpoints = path.join(VOCODER_WORK_DIR, VOCODER_MODEL_WEIGHTS)

        # Tacotron2 Loading
        self.tacotron_instance = Text2Speech(
            self.tacotron_file_config,
            self.tacotron_file_checkpoints,
            device=torch_device,
            threshold=0.5,
            minlenratio=0.0,
            maxlenratio=10.0,
            use_att_constraint=False,
            backward_window=1,
            forward_window=3
        )
        self.tacotron_instance.spc2wav = None

        # Vocoder Loading
        self.vocoder = load_model(self.vocoder_file_checkpoints)\
            .to(torch_device)\
            .eval()
        self.vocoder.remove_weight_norm()

    def tts_inference(self, input_text):
        with torch.no_grad():
            wav, c, *_ = self.tacotron_instance(input_text)
            wav = self.vocoder.inference(c)

        return wav.view(-1).cpu().numpy()

