# classes/Ruff.py
from classes.Command import Command
from classes.Print import Print


class Ruff:
    @staticmethod
    def ensure_ruff_installed() -> None:
        try:
            Command.run("ruff --version")
        except RuntimeError as err:
            install_cmd = "sudo pacman -S ruff"
            Print.error(f"{err}")
            try:
                Command.run(install_cmd)
                Print.success("Ruff has been successfully installed.")
            except RuntimeError as install_err:
                Print.error(f"[red]{install_err}")
                raise RuntimeError("Please install Ruff manually.") from install_err

    @staticmethod
    def format_and_check() -> None:
        try:
            Print.info("🔍 Running Ruff (check + format)…")
            Command.run("ruff format .")
            Command.run("ruff check .")
            Print.success("✅. Ruff check and format completed successfully.")
        except RuntimeError as err:
            # add colour *here*, after we know we’re printing to the console
            print(f"Ruff encountered an error:\n{err}")
            raise
