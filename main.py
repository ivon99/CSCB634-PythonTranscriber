from controller.commands import RecordToFileCommand
from controller.controller import Controller


def main():
    controller = Controller()
    result = controller.record_to_file(RecordToFileCommand(generate=False, filename='asdadasd'))
    print(result.result_code)
    print(result.message)

if __name__ == '__main__':
    main()
