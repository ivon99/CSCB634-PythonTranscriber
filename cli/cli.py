from controller.commands import RecordToFileCommand
from controller.result import Result


class Cli(object):
    def show_result(self, result: Result) -> None:
        print('Result status code - {}'.format(result.result_code))
        print('Result message - {}'.format(result.message))
    
    def ask_for_filename(self) -> RecordToFileCommand:
        filename = input('If you want to store the audio in specific file, please type the name. The default name will be used otherwise: ')
        if not filename:
            return RecordToFileCommand()
        else:
            return RecordToFileCommand(generate=False, filename=filename)
    
    def show_start_recording(self) -> None:
        print('Starting Audio recording. When done press Ctrl-C ...')
    
    def ask_if_want_to_continue(self) -> bool:
        result = input('Do you want to do new recording? (y/n)')
        if result.lower() == 'y':
            return True
        elif result.lower() == 'n':
            return False
        else:
            print('Unrecognized response. Assuming you don\'t want to continue')
            return False
