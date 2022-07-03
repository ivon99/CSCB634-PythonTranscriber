""" Keeps the configuration of the transcriber.
"""

class TranscriberConfig(object):
    """Provide the needed arguments for the transcriber object.

    Attributes:
        model_path: A string, path to the model file to load.
        beam_width: Integer, decoder beam width.
        lm_file_path: A string representing the path to the language model binary file.
        trie_file_path: A string representing the path to the trie file build from the same vocabulary as the language model binary
        lm_alpha: A float representing the alpha hyperparameter of the CTC decoder. Language Model weight.
        lm_beta: A float representing the beta hyperparameter of the CTC decoder. Word insertion weight.
    """
    def __init__(self, model_path, beam_width, lm_file_path, trie_file_path, lm_alpha, lm_beta) -> None:
        self.model_path = model_path
        self.beam_width = beam_width
        self.lm_file_path = lm_file_path
        self.trie_file_path = trie_file_path
        self.lm_alpha = lm_alpha
        self.lm_beta = lm_beta
