import argparse

from analysis import Analysis
from executor import Executor


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="sorter",
        description="Automated file sorter tool"
    )

    parser.add_argument(
        "path",
        help="Directory path to process"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Display detailed output"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview actions without moving files"
    )

    parser.add_argument(
        "--others-folder",
        default="others",
        help="Folder name for files without extensions"
    )

    args = parser.parse_args()

    analysis = Analysis(args)

    executor = Executor(args, analysis.actions_list, analysis.normalized_path)

    executor.print_summary()


if __name__ == "__main__":
    main()
