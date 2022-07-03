"""Module providing the functionality for recognizing speech and converting it to text.
"""

import deepspeech
import numpy as np

from transcriber.transcriber_config import TranscriberConfig

class Transcriber(object):
    """Class for converting audio data to text.

    The class uses the Mozilla's deepspeech library for recognizing stream of audio data and converting it to text.  
    """
    def __init__(self, config: TranscriberConfig) -> None:
        """ Initialize the transcriber with provider configuration.
        """
        self.model = deepspeech.Model(config.model_path, config.beam_width)
        self.model.enableDecoderWithLM(config.lm_file_path, config.trie_file_path, config.lm_alpha, config.lm_beta)

    def create_stream(self) -> None:
        """ Create new streaming session for transcribing data.
        """
        self.context = self.model.createStream()

    def finish_stream(self) -> str:
        """ Close streaming session and return the transcribed data as text.
        """
        return self.model.finishStream(self.context)

    def debug(self):
        """ Print the intermediate result of the speech recognition session
        """
        text = self.model.intermediateDecode(self.context)
        print('DEBUG: {}'.format(text))

    def transcribe(self, data) -> None:
        """ Feed audio content to the current streaming session for transcription.
        """
        data16 = np.frombuffer(data, dtype=np.int16)
        self.model.feedAudioContent(self.context, data16)
