from rich import print

from classes.MyTable import MyTable


class Menu:
    rows_count = 0

    @staticmethod
    def display():
        """
        Display the main menu options.
        """
        columns = [
            {"title": "Index", "style": "cyan"},
            {"title": "Option", "style": "white"},
        ]
        row_styles = {
            0: "blue",
            1: "blue",
            2: "green",
            3: "magenta",
            4: "green",
            5: "yellow",
            6: "yellow",
            7: "red",
            8: "red",
        }
        rows = [
            ["1", "Ruff format and check"],
            ["2", "List installed packages"],
            ["3", "Install package"],
            ["4", "Uninstall package"],
            ["5", "Reinstall packages"],
            ["6", "Init"],
            ["7", "Migrate from requirements.txt to pyproject.toml"],
            ["8", "Remove git-hook file"],
            ["9", "Exit"],
        ]

        Menu.rows_count = 0
        Menu.rows_count += len(rows)

        tb = MyTable()
        tb.show("Main Menu", columns, rows, row_styles=row_styles)

    @staticmethod
    def choose_option():
        """
        Prompt the user to choose an option from the menu.
        """
        while True:
            try:
                count_range = f"Please enter a number between 1 and {Menu.rows_count}: "
                choice = int(input(count_range))
                if choice in range(1, Menu.rows_count + 1):
                    return choice
                else:
                    print(
                        f"[red]Invalid input."
                        f"Please enter a number between 1 and {Menu.rows_count}."
                    )
            except ValueError:
                print("[red] Input must be a number. Please try again.[/red]")
