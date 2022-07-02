from pytest import fixture

from behavioral.command import CopyCommand, CMD, PasteCommand


@fixture
def example_text():
    return "Text to work on"


class TestCommand:

    def test_cmd_executes_copy_command(self, example_text: str):
        cmd = CMD()
        copy_cmd = CopyCommand(example_text)

        assert cmd.execute_commands(copy_cmd) == example_text

    def test_cmd_executes_paste_command(self, example_text: str):
        cmd = CMD()
        copy_cmd = CopyCommand(example_text)

        paste_cmd = PasteCommand(copy_cmd)

        assert cmd.execute_commands(paste_cmd) == example_text
