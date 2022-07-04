""" Module for reading and writing to the console.
"""

from colorama import Fore
from controller.commands import RecordToFileCommand
from controller.result import Result


class Cli(object):
    """ Cli is a class for reading and writing predefined messages to the console.

    The class use colorama to show colored output.
    """
    def show_result(self, result: Result) -> None:
        """Print the result of the executed controller command"""
        print(Fore.GREEN + 'Result status code - {}'.format(result.result_code))
        print(Fore.GREEN + 'Result message - {}'.format(result.message))

    def ask_for_filename(self) -> RecordToFileCommand:
        """Ask for file name from the console and build RecordToFileCommand command"""
        filename = input(Fore.GREEN + 'If you want to store the audio in specific file, please type the name. The default name will be used otherwise: ')
        if not filename:
            return RecordToFileCommand()
        else:
            return RecordToFileCommand(generate=False, filename=filename)

    def show_start_recording(self) -> None:
        """Print a message for start recording"""
        print(Fore.GREEN + 'Starting Audio recording. When done press Ctrl-C ...')

    def ask_if_want_to_continue(self) -> bool:
        """Ask for input if the user want to do second recording"""
        result = input(Fore.GREEN + 'Do you want to do new recording? (y/n)')
        if result.lower() == 'y':
            return True
        elif result.lower() == 'n':
            return False
        else:
            print(Fore.GREEN + 'Unrecognized response. Assuming you don\'t want to continue')
            return False
