from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class CopyCommand(Command):

    def __init__(self, text: str):
        self.text = text

    def execute(self):
        return self.text


class PasteCommand(Command):

    def __init__(self, copied_elementy: CopyCommand):
        self.copied_elementy = copied_elementy

    def execute(self):
        data = self.copied_elementy.text
        return data


class CMD:

    def execute_commands(self, command: Command):
        return command.execute()


if __name__ == "__main__":
    example_text = "Text to work on"
    copy_cmd = CopyCommand(example_text)

    paste_cmd = PasteCommand(copy_cmd)

    command_interface = CMD()

    print(command_interface.execute_commands(paste_cmd))

    print(command_interface.execute_commands(copy_cmd))



