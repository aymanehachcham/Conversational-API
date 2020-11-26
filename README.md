# PEER DJANGO-API
![peer logo](images/peer_logo.png)

A django based REST API for serving ASR & TTS systems relating to Peer app
* This is the first version relased. 
* A later version implementing TorchServe will be soon pushed.

## Installation
* Clone this repository:
```
git clone git@github.com:Spotbills-AI-Department/Peer-API-V1.0.0.git
```
* Set up the virtual environment and all required dependencies either by:
1. Using [Anaconda](https://docs.anaconda.com/anaconda/install/):
```
conda env create -f peer_environment.yaml
```
2. Manually using pip:
* Set up a `python=3.6` virtual environment
* run: `pip install -r requirements.txt`

### Download required Checkpoints and config files from Google Drive:
* Google Drive link: [API Peer V1.0.0](https://drive.google.com/drive/u/0/folders/1tDeCoN1putp6o141Jq-iU_iywXrbDEk7):
* Folder tree:
    * Bert_Checkpoints -> inside *ASR/Bert_NLP*
    * Parallel_Wavegan -> inside *ASR/TTS_ESPnet*
    * Quartznet_Checkpoints -> inside *ASR/Quartznet_ASR*
    * TTS_Checkpoints -> inside *ASR/TTS_ESPnet*
    
## Run the django API
`python manage.py runserver`
* The api will be automatically serving at localhost, port 8000 if you are in linux
 
