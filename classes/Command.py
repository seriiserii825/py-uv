import subprocess
from rich import print


class Command:
    @staticmethod
    def run(command: str) -> str:
        try:
            result = subprocess.run(
                command, shell=True, check=True, text=True, capture_output=True
            )
            print(f"[green]Command '{command}' executed successfully.")
            print(f"[blue]Output: {result.stdout.strip()}")
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                f"[red]Command '{command}' failed with error: {e.stderr.strip()}"
            ) from e
