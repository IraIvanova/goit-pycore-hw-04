import sys
from pathlib import Path
from colorama import Fore

def build_files_tree(directory: Path, prefix = ''):
    sorted_list = sorted(directory.iterdir(), key=sort_by_name)

    for index, path in enumerate(sorted_list):
        connector = "└── " if index == len(sorted_list) - 1 else "├── "

        if path.is_dir():
            print(prefix + connector + Fore.BLUE + path.name + Fore.RESET)
            indent = "    " if index == len(sorted_list) - 1 else "│   "
            build_files_tree(path, prefix + indent )
        else:
            print(prefix + connector + Fore.GREEN + path.name + Fore.RESET)


def sort_by_name(item: Path):
    return item.name.lower()

def main():

    if len(sys.argv) < 2:
        print("Directory path is required.")
        sys.exit(1)

    root_path = Path(sys.argv[1])

    if not root_path.exists():
        print("Directory does not exist.")
        sys.exit(1)

    if not root_path.is_dir():
        print("Only directories are allowed.")
        sys.exit(1)

    print(f"Structure of directory {root_path}:\n")
    print(root_path.name)
    build_files_tree(root_path)


if __name__ == "__main__":
    main()