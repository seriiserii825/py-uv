from classes.Print import Print
from classes.Ruff import Ruff


def format_and_check():
    Ruff.ensure_ruff_installed()
    try:
        Ruff.format_and_check()
    except RuntimeError as e:
        Print.error(f"Error during Ruff operation: {e}")
