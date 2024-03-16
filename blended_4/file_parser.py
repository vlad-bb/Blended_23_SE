from pathlib import Path


def scan_folders(dir_path: Path) -> list[Path]:
    print(f"Func start with: {dir_path.name}")
    file_list = []
    for el in dir_path.iterdir():
        if el.is_file():  # base case
            file_list.append(el)
        else:
            file_list.extend(scan_folders(el))  # recurse case
    print(f"Func finished with {file_list} in {dir_path.name}")
    return file_list


if __name__ == "__main__":
    source_dir = Path('.').absolute()
    result = scan_folders(source_dir)
    print(f"{result=}")
