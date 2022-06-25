class TranscriberConfig(object):
    def __init__(self, model_path, beam_width, scorer_path, lm_alpha, lm_beta) -> None:
        self.model_path = model_path
        self.beam_width = beam_width
        self.scorer_path = scorer_path
        self.lm_alpha = lm_alpha
        self.lm_beta = lm_beta