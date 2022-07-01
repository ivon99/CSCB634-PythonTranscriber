from enum import Enum


class ResultCode(Enum):
    OK = 0
    UNKNOWN_ERROR = 1

class Result(object):
    def __init__(self, result_code: ResultCode, message: str) -> None:
        self.result_code = result_code
        self.message = message