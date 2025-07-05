from classes.Package import Package
from classes.Print import Print


def list_installed_packages():
    try:
        Package.list_installed()
    except RuntimeError as e:
        Print.error(e)
