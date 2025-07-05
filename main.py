from classes.Menu import Menu
from menu.exit_menu import exit_menu
from menu.format_and_check import format_and_check
from menu.install_package import install_package
from menu.list_installed_packages import list_installed_packages
from menu.uninstall_package import uninstall_package


def main():
    def menu():
        Menu.display()
        choice = Menu.choose_option()
        if choice == 1:
            format_and_check()
            menu()
        elif choice == 2:
            list_installed_packages()
            menu()
        elif choice == 3:
            install_package()
            menu()
        elif choice == 4:
            uninstall_package()
            menu()
        if choice == 5:
            exit_menu()
    menu()


if __name__ == "__main__":
    main()
