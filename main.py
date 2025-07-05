from classes.Menu import Menu
from classes.Print import Print


def main():
    Menu.display()
    choice = Menu.choose_option()
    print(f"choice: {choice}")
    Print.print("Thank you for using the program!", error=True)


if __name__ == "__main__":
    main()
