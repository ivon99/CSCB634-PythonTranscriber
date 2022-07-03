""" Result is module for keeping the result objects from the controller.
"""

from enum import Enum

class ResultCode(Enum):
    """ Enumerator, indicating the result status of the executed command.
    """
    OK = 0
    BAD_COMMAND=1
    UNKNOWN_ERROR = 2

class Result(object):
    """Result is a class, representing the result of the executed command in the controller.

    Arguments:
        result_code: ResultCode value, representing the result status of the executed command.
        message: Represent the message that should be displayed to the user.
    """
    def __init__(self, result_code: ResultCode, message: str) -> None:
        self.result_code = result_code
        self.message = message
