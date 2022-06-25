import deepspeech
import numpy as np

from transcriber.transcriber_config import TranscriberConfig


class Transcriber(object):
    def __init__(self, config: TranscriberConfig) -> None:
        self.model = deepspeech.Model(config.model_path)
        self.model.setBeamWidth(config.beam_width)
        self.model.enableExternalScorer(config.scorer_path)
        self.model.setScorerAlphaBeta(config.lm_alpha, config.lm_beta)
    
    def create_stream(self) -> None:
        self.context = self.model.createStream()

    def finish_stream(self) -> str:
        return self.context.finishStream()

    def debug(self):
        text = self.context.intermediateDecode()
        print('DEBUG: {}'.format(text))

    def transcribe(self, data) -> None:
        data16 = np.frombuffer(data, dtype=np.int16)
        self.context.feedAudioContent(data16)
