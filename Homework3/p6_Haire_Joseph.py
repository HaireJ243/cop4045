"""Model files and folders and report their storage usage."""


class Entry:
    """Base class for a file-system entry."""

    def __init__(self, name: str) -> None:
        """Create an entry with a name and no parent folder."""
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.name: str = name
        self._parent: Folder | None = None

    def parent(self) -> "Folder | None":
        """Return the folder containing this entry, or None for a root."""
        return self._parent

    def size(self) -> int:
        """Return this entry's size in bytes."""
        raise NotImplementedError("Entry subclasses must implement size()")

    def absolute_path(self) -> list["Entry"]:
        """Return this entry, its parent, and ancestors up to the root."""
        parent = self.parent()
        if parent is None:
            return [self]
        return [self] + parent.absolute_path()


class File(Entry):
    """A file with a fixed storage size."""

    def __init__(self, name: str, bytes_used: int) -> None:
        """Create a file and reject negative storage sizes."""
        super().__init__(name)
        if not isinstance(bytes_used, int):
            raise TypeError("bytes_used must be an integer")
        if bytes_used < 0:
            raise ValueError("bytes_used cannot be negative")
        self.bytes_used: int = bytes_used

    def size(self) -> int:
        """Return the number of bytes used by this file."""
        return self.bytes_used


class Folder(Entry):
    """A folder containing files and other folders."""

    def __init__(self, name: str) -> None:
        """Create an empty folder."""
        super().__init__(name)
        self._children: list[Entry] = []

    def add(self, entry: Entry) -> None:
        """Add an entry as a child of this folder."""
        if not isinstance(entry, Entry):
            raise TypeError("entry must be an Entry")
        self._children.append(entry)
        entry._parent = self

    def size(self) -> int:
        """Return the total size of all files in this folder tree."""
        return sum(entry.size() for entry in self._children)

    def children(self) -> tuple[Entry, ...]:
        """Return the folder's children as a tuple."""
        return tuple(self._children)


def find_large_files(entry: Entry, minimum_size: int) -> list[File]:
    """Return files at least minimum_size bytes, searching recursively.

    If entry is a File, return a one-item list when it meets the threshold,
    otherwise return an empty list. If entry is a Folder, search its contents.
    """
    if isinstance(entry, File):
        if entry.size() >= minimum_size:
            return [entry]
        return []

    if isinstance(entry, Folder):
        large_files: list[File] = []
        for child in entry.children():
            large_files.extend(find_large_files(child, minimum_size))
        return large_files

    raise TypeError("entry must be a File or Folder")


def make_example_tree() -> Folder:
    """Build and return a three-level folder tree with several files."""
    root = Folder("university")
    department = Folder("computer-science")
    lab = Folder("research-lab")

    root.add(department)
    department.add(lab)
    lab.add(File("dataset.bin", 1200))
    lab.add(File("notes.txt", 800))
    department.add(File("schedule.csv", 250))
    return root


def main() -> None:
    """Demonstrate folder sizing, large-file search, and absolute paths."""
    root = make_example_tree()
    print(f"Total storage: {root.size()} bytes")

    for threshold in (500, 1000):
        files = find_large_files(root, threshold)
        print(f"Files at least {threshold} bytes: "
              f"{[(file.name, file.size()) for file in files]}")

    dataset = find_large_files(root, 1000)[0]
    print("Absolute path (entry to root):",
          [entry.name for entry in dataset.absolute_path()])


if __name__ == "__main__":
    main()