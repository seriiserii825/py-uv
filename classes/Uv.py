from classes.Command import Command


class Uv:
    @staticmethod
    def start():
        """
        Create .venv directory and install uv package.
        """
        Command.run("uv venv .venv")
