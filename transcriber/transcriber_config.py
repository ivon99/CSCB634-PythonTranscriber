class TranscriberConfig(object):
    def __init__(self, model_path, beam_width, lm_file_path, trie_file_path, lm_alpha, lm_beta) -> None:
        self.model_path = model_path
        self.beam_width = beam_width
        self.lm_file_path = lm_file_path
        self.trie_file_path = trie_file_path
        self.lm_alpha = lm_alpha
        self.lm_beta = lm_beta
