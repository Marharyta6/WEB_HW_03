import argparse
from concurrent.futures import ThreadPoolExecutor
import logging
from pathlib import Path
from shutil import copyfile


def grabs_folder(path: Path):
    folders = []
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            folders.extend(grabs_folder(el))
    return folders


def copy_file(source: Path, dest: Path, file: Path):
    ext = file.suffix
    new_path = dest / ext
    try:
        new_path.mkdir(exist_ok=True, parents=True)
        copyfile(file, new_path / file.name)
    except OSError as e:
        logging.error(e)


def main(source: Path, output: Path):
    if not source.exists():
        logging.error(f"Source folder {source} does not exist.")
        return

    output.mkdir(parents=True, exist_ok=True)
    folders = [source] + grabs_folder(source)

    with ThreadPoolExecutor(max_workers=4) as executor:
        for folder in folders:
            for file in folder.iterdir():
                if file.is_file():
                    executor.submit(copy_file, source, output, file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sorting folder')
    parser.add_argument("--source", "-s", help="Source folder", required=True)
    parser.add_argument("--output", "-o", help="Output folder", default="dist")
    args = parser.parse_args()

    source = Path(args.source)
    output = Path(args.output)

    logging.basicConfig(level=logging.ERROR,
                        format="%(threadName)s %(message)s")

    main(source, output)
    print('Готово')
