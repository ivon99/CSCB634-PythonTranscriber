from transcriber import *
from audiostreamer import *
from filewriter import *

import os
import pyaudio
import time
from transcriber.transcriber import Transcriber
from transcriber.transcriber_config import TranscriberConfig
from audiostreamer.audiostreamer import AudioStreamer
from filewriter.filewriter import FileWriter

# DeepSpeech parameters
DEEPSPEECH_MODEL_DIR = 'models'
MODEL_FILE_PATH = os.path.join(DEEPSPEECH_MODEL_DIR, 'output_graph.pbmm')
BEAM_WIDTH = 500
LM_FILE_PATH = os.path.join(DEEPSPEECH_MODEL_DIR, 'lm.binary')
TRIE_FILE_PATH = os.path.join(DEEPSPEECH_MODEL_DIR, 'trie')
LM_ALPHA = 0.75
LM_BETA = 1.85

# Make DeepSpeech Model
cfg = TranscriberConfig(MODEL_FILE_PATH, BEAM_WIDTH, LM_FILE_PATH, TRIE_FILE_PATH, LM_ALPHA, LM_BETA)
transcriber = Transcriber(cfg)

# Create a Streaming session
transcriber.create_stream()

# PyAudio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
INPUT = True
CHUNK_SIZE = 1024

# Record audio and feed to transcriber
audiostreamer= AudioStreamer(FORMAT, CHANNELS, RATE, INPUT, CHUNK_SIZE)
audiostreamer.record_till_keyboard_interrupt(transcriber)
text = transcriber.finish_stream()
print('Final text = {}'.format(text))

# Save text transcription to file 
PATH_TRANSCRIPTIONS = 'repository'
filewrite = FileWriter(text,PATH_TRANSCRIPTIONS)
in_filename= input("Enter filename of text note to write transcript to:")
if(in_filename):
	filewrite.save_text_inputted_filename(in_filename)
else:
	filewrite.save_text_automatic_filename()
