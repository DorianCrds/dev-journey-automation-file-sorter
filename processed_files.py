class ProcessedFile:
    def __init__(self, element_path: str, element_name: str, others_folder_name: str) -> None:
        self.source_path = element_path
        self.filename = element_name
        self.extension: str | None = None
        self.target_directory = ""

        self._extract_extension()
        self._set_target_directory(others_folder_name)

    def _extract_extension(self) -> None:
        if self.filename.startswith(".") and self.filename.count(".") == 1:
            self.extension = None
            return

        if "." not in self.filename:
            self.extension = None
            return

        self.extension = self.filename.rsplit(".", 1)[-1].lower()

    def _set_target_directory(self, others_folder_name: str) -> None:
        self.target_directory = (
            others_folder_name if self.extension is None else self.extension
        )
