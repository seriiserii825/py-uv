from classes.MyTable import MyTable


class Menu:
    @staticmethod
    def display():
        """
        Display the main menu options.
        """
        columns = [
            {"title": "Index", "style": "cyan"},
            {"title": "Option", "style": "white"},
        ]
        rows = [
            ["1", "Ruff format and check"],
            ["2", "Show contact form fields with required fields"],
            ["3", "Show contact form fields with submitted fields"],
            ["4", "Exit"],
        ]
        tb = MyTable()
        tb.show("Main Menu", columns, rows, row_styles={0: "magenta"})
