from classes.Menu import Menu
from classes.Package import Package
from classes.Print import Print
from classes.Ruff import Ruff


def main():
    Menu.display()
    choice = Menu.choose_option()
    Print.success(f"choice: {choice}")
    if choice == 1:
        Ruff.ensure_ruff_installed()
        try:
            Ruff.format_and_check()
        except RuntimeError as e:
            Print.error(f"Error during Ruff operation: {e}")
    elif choice == 2:
        try:
            Package.install()
        except RuntimeError as e:
            Print.error(e)
    elif choice == 3:
        try:
            Package.uninstall()
        except RuntimeError as e:
            Print.error(e)
    if choice == 4:
        Print.error("Exiting the program.")
        return


if __name__ == "__main__":
    main()
