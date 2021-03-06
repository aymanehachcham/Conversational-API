
import json
import torch
import os.path as path
from omegaconf import OmegaConf, DictConfig
from nemo.collections.asr.models import EncDecCTCModel

WORK_DIR = "Quartznet_ASR/Quartznet_Checkpoints/"
_MODEL_CONFIG = "model_config.yaml"
_MODEL_WEIGHTS = "model_weights.ckpt"
_MODEL_IS_RESTORED = False

"""
Handler class that manages QuartzNet loading files and checkpoints,
implementing all required methods to ease access for other external modules relying
on it.

- Loading yaml configuration files and checkpoints
- Instantiating EncDecCTCModel NeMo core module
- Define a convert_to_text method that runs inference on saved audio files and returns transcribed text
"""
class Quartznet_loader():
    def __init__(self, torch_device=None):
        if torch_device is None:
            if torch.cuda.is_available():
                torch_device = torch.device('cuda')
            else:
                torch_device = torch.device('cpu')

        self.file_config = path.join(WORK_DIR, _MODEL_CONFIG)
        self.file_checkpoints = path.join(WORK_DIR, _MODEL_WEIGHTS)

        model_config = OmegaConf.load(self.file_config)
        OmegaConf.set_struct(model_config, True)

        if isinstance(model_config, DictConfig):
            self.config = OmegaConf.to_container(model_config, resolve=True)
            self.config = OmegaConf.create(self.config)
            OmegaConf.set_struct(self.config, True)

        # EncDecCTCModel.set_model_restore_state(is_being_restored=True)
        instance = EncDecCTCModel(cfg=self.config)

        self.model_instance = instance
        self.model_instance.to(torch_device)
        self.model_instance.load_state_dict(torch.load(self.file_checkpoints, torch_device), False)

    def covert_to_text(self, audio_files):
        return self.model_instance.transcribe(paths2audio_files=audio_files)

    def create_output_manifest(self, file_path):
        # create manifest
        manifest = dict()
        manifest['audio_filepath'] = file_path
        manifest['duration'] = 18000
        manifest['text'] = 'todo'

        with open(file_path + ".json", 'w') as fout:
            fout.write(json.dumps(manifest))

        return file_path + ".json"