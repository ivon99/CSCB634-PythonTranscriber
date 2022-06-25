from transcriber import *

import os
import pyaudio
import time
from transcriber.transcriber import Transcriber

from transcriber.transcriber_config import TranscriberConfig

# DeepSpeech parameters
DEEPSPEECH_MODEL_DIR = 'models'
MODEL_FILE_PATH = os.path.join(DEEPSPEECH_MODEL_DIR, 'deepspeech-0.9.3-models.pbmm')
BEAM_WIDTH = 500
SCORER_PATH = os.path.join(DEEPSPEECH_MODEL_DIR, 'deepspeech-0.9.3-models.scorer')
LM_ALPHA = 0.75
LM_BETA = 1.85

# Make DeepSpeech Model
cfg = TranscriberConfig(MODEL_FILE_PATH, BEAM_WIDTH, SCORER_PATH, LM_ALPHA, LM_BETA)
transcriber = Transcriber(cfg)

# Create a Streaming session
transcriber.create_stream()

# Encapsulate DeepSpeech audio feeding into a callback for PyAudio
def process_audio(in_data, frame_count, time_info, status):
    transcriber.transcribe(in_data)
    transcriber.debug()
    return (in_data, pyaudio.paContinue)

# PyAudio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK_SIZE = 1024

# Feed audio to deepspeech in a callback to PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK_SIZE,
    stream_callback=process_audio
)

print('Please start speaking, when done press Ctrl-C ...')
stream.start_stream()

try: 
    while stream.is_active():
        time.sleep(0.1)
except KeyboardInterrupt:
    # PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()
    print('Finished recording.')
    # DeepSpeech
    text = transcriber.finish_stream()
    print('Final text = {}'.format(text))