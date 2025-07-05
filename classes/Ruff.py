from rich import print

from classes.Command import Command


class Ruff:
    @staticmethod
    def ensure_ruff_installed():
        try:
            Command.run("ruff --version")
        except RuntimeError as e:
            command = "sudo pacman -S ruff"
            print(f"[red]{e}")
            print(
                f"[blue]Ruff is not installed. "
                f"{command}"
                f" Press [bold]Enter[/bold] to install Ruff."
            )
            try:
                Command.run(command)
                print("[green]Ruff has been successfully installed.")
            except RuntimeError as install_error:
                print(f"Failed to install Ruff: {install_error}")
                raise RuntimeError("Please install Ruff manually.") from install_error

    @staticmethod
    def format_and_check():
        try:
            Command.run("ruff format .")
            Command.run("ruff check .")
            print("[green]Ruff check and format completed successfully.[/green]")
        except RuntimeError as e:
            print(f"[red]Ruff encountered an error: {e}[/red]")
            raise
