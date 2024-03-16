from pathlib import Path


def scan_folders(dir_path: Path, spaces=1) -> None:
    for el in dir_path.iterdir():
        print(f"{'-' * spaces}{el.name}")
        if el.is_file():  # base case
            continue
        else:
            scan_folders(el, spaces=spaces+1)  # recurse case


if __name__ == "__main__":
    source_dir = Path('.').absolute()
    scan_folders(source_dir)
