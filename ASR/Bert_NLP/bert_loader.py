
import os.path as path
from omegaconf import OmegaConf, DictConfig
from nemo.collections.nlp.models import PunctuationCapitalizationModel
from nemo.core.classes.modelPT import ModelPT
import torch

WORK_DIR = "Bert_NLP/Bert_Checkpoints/"
_MODEL_CONFIG = "model_config.yaml"
_MODEL_WEIGHTS = "model_weights.ckpt"
_MODEL_IS_RESTORED = True

"""
Handler class that manages Bert loading files and checkpoints,
implementing all required methods to ease access for other external modules relying
on it.
- Loading yaml configuration files and checkpoints
- Instantiating PunctuationCapitalization NeMo core module
- Define a punctuation method that takes raw text and yields readable text
"""
class Bert_loader():
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

        # PunctuationCapitalizationModel.super().__set_model_restore_state(_MODEL_IS_RESTORED)
        instance = PunctuationCapitalizationModel(cfg=self.config)

        self.model_instance = instance
        self.model_instance.to(torch_device)
        self.model_instance.load_state_dict(torch.load(self.file_checkpoints, torch_device), False)

    def punctuate(self, query):
        return self.model_instance.add_punctuation_capitalization(query)[0]
