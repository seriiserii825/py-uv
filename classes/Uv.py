from classes.Command import Command
from pathlib import Path


class Uv:
    @staticmethod
    def start():
        """
        Create .venv directory and install uv package.
        """
        if Path(".venv").exists():
            print("Virtual environment already exists.")
            return
        else:
            try:
                Command.run("uv venv .venv")
                print("Virtual environment created successfully.")
            except Exception as e:
                print(f"Error creating virtual environment: {e}")
                return
