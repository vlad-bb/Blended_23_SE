import datetime
import glob
from pathlib import Path
from file_parser import scan_folders

SAVE_PERIOD = 300  # seconds


def run_cleaner(dir_path_str: str) -> None:
    dir_path = Path(dir_path_str)
    file_list = scan_folders(dir_path)
    current_time = datetime.datetime.now()
    for file in file_list:
        create_timestamp = file.stat().st_ctime
        print(create_timestamp, type(create_timestamp))
        create_time = datetime.datetime.fromtimestamp(create_timestamp)
        print(create_time, type(create_time))
        delta_second = (current_time - create_time).seconds
        print(f"{delta_second=}")
        if delta_second > SAVE_PERIOD:
            print(f"File {file.name} has been deleted.")
            file.unlink(missing_ok=True)


def run_cleaner_short(dir_path_str: str):
    return [Path(file).unlink(missing_ok=True) for file in glob.glob(f"{dir_path_str}/**/*", recursive=True)
            if (datetime.datetime.now() - datetime.datetime.fromtimestamp(
            Path(file).stat().st_ctime)).seconds > SAVE_PERIOD and Path(file).is_file()]


if __name__ == '__main__':
    dir_path_ = 'folder_2'
    run_cleaner_short(dir_path_str=dir_path_)
