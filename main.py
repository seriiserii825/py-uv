from classes.Menu import Menu
from menu.exit_menu import exit_menu
from menu.format_and_check import format_and_check
from menu.init import init
from menu.install_from_toml import install_from_toml
from menu.install_package import install_package
from menu.list_installed_packages import list_installed_packages
from menu.migrate_from_requirements import migrate_from_requirements
from menu.reinstall_packages import reinstall_packages
from menu.remove_git_hook import remove_git_hook
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
        elif choice == 2.1:
            list_installed_packages()
            install_from_toml()
            list_installed_packages()
            menu()
        elif choice == 3:
            list_installed_packages()
            install_package()
            list_installed_packages()
            menu()
        elif choice == 4:
            list_installed_packages()
            uninstall_package()
            list_installed_packages()
            menu()
        elif choice == 5:
            list_installed_packages()
            reinstall_packages()
            list_installed_packages()
            menu()
        elif choice == 6:
            init()
            menu()
        elif choice == 7:
            migrate_from_requirements()
            menu()
        elif choice == 8:
            remove_git_hook()
            menu()
        if choice == 9:
            exit_menu()

    menu()


if __name__ == "__main__":
    main()
