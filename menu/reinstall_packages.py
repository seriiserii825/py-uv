from classes.Package import Package
from classes.Print import Print


def reinstall_packages():
    try:
        Package.reinstall_all()
    except RuntimeError as e:
        Print.error(f"Error during reinstallation: {e}")
