import os
import shutil

from actions import Action


class Executor:
    def __init__(self, args, actions_list: list[Action], base_path: str):
        self._args = args
        self._base_path = base_path

        self.create_actions = [a for a in actions_list if a.action_type == "CREATE"]
        self.move_actions = [a for a in actions_list if a.action_type == "MOVE"]
        self.conflict_actions = [a for a in actions_list if a.action_type == "CONFLICT"]

        self.succeeded_actions = []
        self.failed_actions = []

        if not self._args.dry_run:
            self._execute()

    def _execute(self) -> None:
        self._create_directories()
        self._move_files()

    def _create_directories(self) -> None:
        for action in self.create_actions:
            try:
                os.makedirs(action.destination_path, exist_ok=True)
                self.succeeded_actions.append(action)
                if self._args.verbose:
                    print(f"✔ Directory created: {action.element_name}")
            except Exception as e:
                self.failed_actions.append(action)
                print(f"✖ Failed to create directory '{action.element_name}': {e}")

    def _move_files(self) -> None:
        for action in self.move_actions:
            try:
                shutil.move(action.source_path, action.destination_path)
                self.succeeded_actions.append(action)
                if self._args.verbose:
                    print(f"✔ File moved: {action.element_name}")
            except Exception as e:
                self.failed_actions.append(action)
                print(f"✖ Failed to move file '{action.element_name}': {e}")

    def print_summary(self) -> None:
        print("\n==================== SORT SUMMARY ====================")

        print(f"Path: {self._base_path}")
        print(f"Directories created: {len(self.create_actions)}")
        print(f"Files moved: {len(self.move_actions)}")
        print(f"Conflicts: {len(self.conflict_actions)}")
        print(f"Errors: {len(self.failed_actions)}")

        if self._args.verbose:
            if self.conflict_actions:
                print("\nConflicts:")
                for action in self.conflict_actions:
                    print(f"  ⚠ {action}")

            if self.failed_actions:
                print("\nErrors:")
                for action in self.failed_actions:
                    print(f"  ✖ {action}")

        print("=====================================================\n")
