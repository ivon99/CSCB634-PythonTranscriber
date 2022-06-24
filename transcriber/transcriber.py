import deepspeech
import numpy as np

from transcriber.transcriber_config import TranscriberConfig


class Transcriber(object):
    def __init__(self, config: TranscriberConfig) -> None:
        self.model = deepspeech.Model(config.model_path, config.beam_width)
        self.model.enableDecoderWithLM(config.lm_file_path, config.trie_file_path, config.lm_alpha, config.lm_beta)
    
    def create_stream(self) -> None:
        self.context = self.model.createStream()

    def finish_stream(self) -> str:
        return self.model.finishStream(self.context)

    def transcribe(self, data) -> None:
        data16 = np.frombuffer(data, dtype=np.int16)
        self.model.feedAudioContent(self.context, data16)
        # Debug only
        # text = self.model.intermediateDecode(context)
        # print('Interim text = {}'.format(text))