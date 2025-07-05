from classes.Menu import Menu


def main():
    Menu.display()
    choice = Menu.choose_option()
    print(f"choice: {choice}")


if __name__ == "__main__":
    main()
