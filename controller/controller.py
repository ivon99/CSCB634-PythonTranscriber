import os
import time

import pyaudio
from audiostreamer.audiostreamer import AudioStreamer
from controller.commands import RecordToFileCommand
from controller.result import Result, ResultCode
from filewriter.filewriter import FileWriter

from transcriber.transcriber import Transcriber
from transcriber.transcriber_config import TranscriberConfig


# DeepSpeech parameters
DEEPSPEECH_MODEL_DIR = 'models'
MODEL_FILE_PATH = os.path.join(DEEPSPEECH_MODEL_DIR, 'output_graph.pbmm')
BEAM_WIDTH = 500
LM_FILE_PATH = os.path.join(DEEPSPEECH_MODEL_DIR, 'lm.binary')
TRIE_FILE_PATH = os.path.join(DEEPSPEECH_MODEL_DIR, 'trie')
LM_ALPHA = 0.75
LM_BETA = 1.85

# PyAudio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
INPUT = True
CHUNK_SIZE = 1024

# Save text to file 
FILES_DIR = 'notes'

class Controller(object):
    def __init__(self):
        cfg = TranscriberConfig(MODEL_FILE_PATH, BEAM_WIDTH, LM_FILE_PATH, TRIE_FILE_PATH, LM_ALPHA, LM_BETA)
        self.transcriber = Transcriber(cfg)
        self.audio_streamer= AudioStreamer(FORMAT, CHANNELS, RATE, INPUT, CHUNK_SIZE)

    def record_to_file(self, command: RecordToFileCommand) -> Result:
        if command == None:
            return Result(ResultCode.BAD_COMMAND, 'Missing command')
        elif command != None and not command.generate and command.filename == None:
            return Result(ResultCode.BAD_COMMAND, 'Missing filename')

        try:
            self.transcriber.create_stream()
            self.audio_streamer.record(self.transcriber)
            try:
                while self.audio_streamer.is_active_stream():
                    time.sleep(0.1)
            except KeyboardInterrupt:
                self.audio_streamer.finish_recording()
            text = self.transcriber.finish_stream()

            file_writer = FileWriter(text, FILES_DIR)
            if command.generate:
                filename = file_writer.save_text_automatic_filename()
            else:
                filename = command.filename
                file_writer.save_text_inputted_filename(filename)
            
            return Result(ResultCode.OK, 'Successfully stored the text in file - {}'.format(filename))
        except Exception as e:
            text = 'Unknown exception - {}'.format(str(e))
            return Result(ResultCode.UNKNOWN_ERROR, text)

    
