from classes.Command import Command
from classes.InputValidator import InputValidator
from classes.Uv import Uv


class Package:
    @staticmethod
    def install():
        package_name = InputValidator.get_string("Enter the package name to install: ")
        try:
            Command.run(f"uv add {package_name}")
        except RuntimeError as e:
            raise RuntimeError(f"Failed to install package '{package_name}': {e}")
