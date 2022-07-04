"""Commands is submodule responsibel for keeping all command of the program
"""

class RecordToFileCommand(object):
    """ RecordToFileCommand is class representing the command for recording to file

    Attributes:
        generate: Boolean attribute, indicating if a new file name should be generated or not
        filename: String attribute, representing the name of the file if the user request specific file name.
    """
    def __init__(self, generate=True, filename=None):
        """Initialize the RecordToFileCommand object with generated and filename values"""
        self.generate = generate
        self.filename = filename
