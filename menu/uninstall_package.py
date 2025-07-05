from classes.Package import Package
from classes.Print import Print


def uninstall_package():
    try:
        Package.uninstall()
    except RuntimeError as e:
        Print.error(e)
