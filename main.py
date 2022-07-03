"""The entry point of the program
"""

from cli.cli import Cli
from controller.commands import RecordToFileCommand
from controller.controller import Controller


def main():
    """The main function, executing the main loop of the program.
    """
    cli = Cli()
    should_continue = True
    while should_continue:
        controller = Controller()
        command = cli.ask_for_filename()
        cli.show_start_recording()
        result = controller.record_to_file(command)
        cli.show_result(result)
        should_continue = cli.ask_if_want_to_continue()

if __name__ == '__main__':
    main()
