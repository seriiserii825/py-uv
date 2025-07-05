from classes.Menu import Menu
from classes.Print import Print
from classes.Ruff import Ruff


def main():
    Menu.display()
    choice = Menu.choose_option()
    Print.print(f"choice: {choice}")
    if choice == 1:
        Ruff.ensure_ruff_installed()
        try:
            Ruff.format_and_check()
        except RuntimeError as e:
            Print.print(f"Error during Ruff operation: {e}", error=True)
    if choice == 4:
        Print.print("Exiting the program.", error=True)
        return


if __name__ == "__main__":
    main()
