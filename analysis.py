import os
import sys

from actions import Action
from processed_files import ProcessedFile


class Analysis:
    def __init__(self, args) -> None:
        self._args = args
        self.normalized_path = ""
        self._processed_files = []
        self._existing_directories = set()
        self._required_directories = set()
        self.actions_list = []
        self._conflict_actions = []

        self._validate_args_path()
        self._set_normalized_path()

        self._analyze_directory(self._read_directory())
        self._determine_required_directories()
        self._build_actions_list()

    def _validate_args_path(self) -> None:
        if not os.path.exists(self._args.path):
            print(f"[ERROR] Path does not exist: {self._args.path}")
            sys.exit(1)

        if not os.path.isdir(self._args.path):
            print(f"[ERROR] Directory path required, got a file: {self._args.path}")
            sys.exit(1)

    def _set_normalized_path(self) -> None:
        self.normalized_path = os.path.abspath(self._args.path)
        if self._args.verbose:
            print(f"--> Using directory: {self.normalized_path}")

    def _read_directory(self) -> list[str]:
        try:
            return os.listdir(self.normalized_path)
        except PermissionError:
            print(f"[ERROR] Access denied to directory: {self.normalized_path}")
            sys.exit(1)
        except OSError as e:
            print(f"[ERROR] OS error while accessing directory: {e}")
            sys.exit(1)

    def _analyze_directory(self, content: list[str]) -> None:
        if self._args.verbose:
            print("\n--------------- File analysis ---------------")

        for element_name in content:
            element_path = os.path.join(self.normalized_path, element_name)

            if os.path.isdir(element_path):
                self._existing_directories.add(element_name)
                if self._args.verbose:
                    print(f"--> DIRECTORY: '{element_name}'")
                continue

            if not os.path.isfile(element_path):
                continue

            processed_file = ProcessedFile(
                element_path,
                element_name,
                self._args.others_folder
            )

            self._processed_files.append(processed_file)

            if self._args.verbose:
                print(
                    f"--> FILE: '{processed_file.filename}' | "
                    f"EXTENSION: '{processed_file.extension}' | "
                    f"TARGET DIR: '{processed_file.target_directory}'"
                )

        if self._args.verbose:
            print("---------------------------------------------\n")

    def _determine_required_directories(self) -> None:
        for pf in self._processed_files:
            if pf.target_directory not in self._existing_directories:
                self._required_directories.add(pf.target_directory)

    def _build_actions_list(self) -> None:
        for directory in self._required_directories:
            self.actions_list.append(
                Action(
                    element_name=directory,
                    element_type="DIRECTORY",
                    source_path=self.normalized_path,
                    destination_path=os.path.join(self.normalized_path, directory),
                    target_directory=directory,
                    action_type="CREATE"
                )
            )

        for pf in self._processed_files:
            destination_directory = os.path.join(
                self.normalized_path,
                pf.target_directory
            )
            destination_path = os.path.join(
                destination_directory,
                pf.filename
            )

            action = Action(
                element_name=pf.filename,
                element_type="FILE",
                source_path=pf.source_path,
                destination_path=destination_path,
                target_directory=pf.target_directory,
                action_type="MOVE"
            )

            if os.path.exists(destination_path):
                action.action_type = "CONFLICT"
                self._conflict_actions.append(action)
                continue

            self.actions_list.append(action)

        if self._args.dry_run:
            self._print_dry_run()

    def _print_dry_run(self) -> None:
        print("\n------------------ Dry run ------------------")
        for action in self.actions_list + self._conflict_actions:
            print(action)

        movable_files = len(
            [a for a in self.actions_list if a.action_type == "MOVE"]
        )

        print(
            f"\n--> Needs to:\n"
            f"    - create {len(self._required_directories)} directories\n"
            f"    - move {movable_files} files\n"
            f"--> Found {len(self._conflict_actions)} conflicts"
        )
        print("---------------------------------------------")
