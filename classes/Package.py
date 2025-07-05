import json
import subprocess

from pyfzf.pyfzf import FzfPrompt

from classes.Command import Command
from classes.InputValidator import InputValidator

fzf = FzfPrompt()


class Package:
    @staticmethod
    def list_installed():
        Command.run("uv pip list")

    @staticmethod
    def install():
        package_name = InputValidator.get_string("Enter the package name to install: ")
        try:
            Command.run(f"uv add {package_name}")
        except RuntimeError as e:
            raise RuntimeError(f"Failed to install package '{package_name}': {e}")

    @staticmethod
    def uninstall():
        installed_packages = Package.get_uv_installed_packages()
        choosed_package = Package.choose_package_with_fzf(installed_packages)
        try:
            Command.run(f"uv remove {choosed_package}")
        except RuntimeError as e:
            raise RuntimeError(f"Failed to uninstall package '{choosed_package}': {e}")

    @staticmethod
    def get_uv_installed_packages() -> list[str]:
        result = subprocess.run(
            ["uv", "pip", "list", "--format=json"],
            capture_output=True,
            text=True,
            check=True,
        )
        packages = json.loads(result.stdout)  # List of dicts
        packages = [package["name"] for package in packages]
        return packages

    @staticmethod
    def choose_package_with_fzf(packages: list[str]) -> str:
        selected_package = fzf.prompt(packages)
        if not selected_package:
            raise RuntimeError("No package selected.")

        return selected_package[0]
