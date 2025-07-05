from classes.Package import Package
from classes.Print import Print


def install_package():
    try:
        Package.install()
    except RuntimeError as e:
        Print.error(e)
