import re


def parse_folder_structure(file_name: str):
    dir_path: list[str] = []
    complete_dir_names: list[str] = []
    directory_sizes: dict[str, int] = {}
    prog = re.compile("^[0-9]*")

    with open(file_name) as f:
        for line in f.readlines():
            if line.startswith("$ cd"):
                dir_name = line[5:].strip()
                if dir_name == "..":
                    dir_path.pop()
                    complete_dir_names.pop()
                else:
                    dir_path.append(dir_name)
                    complete_dir_name = "-".join(dir_path)
                    complete_dir_names.append(complete_dir_name)
                    directory_sizes[complete_dir_name] = 0
                continue

            match = prog.search(line)
            if file_size := match.group():
                for dir in complete_dir_names:
                    directory_sizes[dir] += int(file_size)
                continue

    return directory_sizes


def get_folders_with_maximum_size(file_name: str, max_folder_size: int) -> int:
    directory_sizes = parse_folder_structure(file_name)

    folder_values = directory_sizes.values()

    return sum([fv for fv in folder_values if fv <= max_folder_size])


def get_closest_folder_to_target(
    file_name: str, target: int, total_system_size: int
) -> int:
    directory_sizes = parse_folder_structure(file_name)

    total_size = directory_sizes["/"]

    free = total_system_size - total_size
    to_delete = target - free

    if to_delete <= 0:
        return 0

    folder_sizes = list(directory_sizes.values())

    return min([f for f in folder_sizes if f >= to_delete])


if __name__ == "__main__":
    FILE_NAME = "dec_7/input.txt"

    dir_count = get_folders_with_maximum_size(FILE_NAME, 100_000)

    print(f"Directory sizes: {dir_count}")

    folder_to_delete = get_closest_folder_to_target(FILE_NAME, 30_000_000, 70_000_000)

    print(f"Size of folder to delete {folder_to_delete}")
