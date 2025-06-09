"""Utility script to verify that all required packages are installed.

It reads a requirements file passed on the command line and checks whether
every listed dependency is present in the current Python environment.
"""

import pkg_resources
import sys


def main() -> None:
    """Check the requirements file specified on the command line.

    The script exits with a non-zero status if any packages are missing.
    """
    requirements_file = sys.argv[1]
    with open(requirements_file, "r") as f:
        required_packages = [
            line.strip().split("#")[0].strip() for line in f.readlines()
        ]

    installed_packages = [package.key for package in pkg_resources.working_set]

    missing_packages = []
    for package in required_packages:
        if not package:  # Skip empty lines
            continue
        package_name = package.strip().split("==")[0]
        if package_name.lower() not in installed_packages:
            missing_packages.append(package_name)

    if missing_packages:
        print("Missing packages:")
        print(", ".join(missing_packages))
        sys.exit(1)
    else:
        print("All packages are installed.")


if __name__ == "__main__":
    main()
