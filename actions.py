class Action:
    def __init__(
        self,
        element_name: str,
        element_type: str,
        source_path: str,
        destination_path: str,
        target_directory: str,
        action_type: str
    ):
        self.element_name = element_name
        self.element_type = element_type
        self.source_path = source_path
        self.destination_path = destination_path
        self.target_directory = target_directory
        self.action_type = action_type

    def __repr__(self) -> str:
        return (
            f"--> ACTION: {self.action_type} {self.element_type} '{self.element_name}'\n"
            f"  | FROM: '{self.source_path}'\n"
            f"  | TO:   '{self.destination_path}'"
        )

    def __str__(self) -> str:
        return f"{self.action_type} {self.element_type} '{self.element_name}'"
