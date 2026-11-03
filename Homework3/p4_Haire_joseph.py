from testif import testif

def ed_read(filename: str, start: int = 0, to: int = -1) -> str:
    """Return the content of the file in the halp-open range [start, to)
    
    Parameters    : filename the file to read, start first index to end index. -1 means end of file
    Preconditions : the file exists
    Postconditions: the file is not changed
    Raises        : IndexError if to exceeds file length; file I/O errors are passed to the caller"""

    with open(filename) as f:
        text = f.read()

    if to == -1:
        to = len(text)
    if to > len(text):
        raise IndexError("to (" + str(to) + ") exceeds file length")
    return text[start:to]

def ed_find(filename: str, search_str: str) -> list:
    """Return a list of positions where search_str occurs in file.
    
        Parameters    : filename the file to search, search_str the string to find
        Preconditions : the file exists
        Postconditions: the file is not changed
        Raised        : file I/O errors are passed to the caller"""

    with open(filename) as f:
        text = f.read()

    positions = []
    i = text.find(search_str)

    while i != -1:
        positions.append(i)
        i = text.find(search_str, i + 1)

    return positions

def ed_replace(filename: str, search_str: str, replace_with: str, occurrence: int = -1) -> int:
    """Replace search_str with replace_with in the file
    
        Parameters    : search for the string to replace, replace_with the new string
        Precondtitions: the file exists
        Postconditions: returns the number of replacements, the file is not changed if occurrence
                        is larger than previouse occurrence index
        Raised        : file I/O errors are passed to the caller"""

    with open(filename) as f:
        text = f.read()

    positions = ed_find(filename, search_str)

    if occurrence == -1:
        count = len(positions)
        text  = text.replace(search_str, replace_with)
    elif occurrence < len(positions):
        count = 1
        p     = positions[occurrence]
        text  = text[:p] + replace_with +text[p + len(search_str):]
    else:
        return 0

    with open(filename, "w") as f:
        f.write(text)

    return count

def ed_append(filename: str, string: str) -> int:
    """Append string to the end of the file; create file if needed
    
        Parameters    : filename file to append, string the text to append
        Postconditions: Returns the number of characters written
        Raised        : file I/O errors are passed to the caller"""

    with open(filename, "a") as f:
        return f.write(string)

def test_ed_find() -> None:
    """Test ed_find()"""

    fn = "test_find.txt"

    with open(fn, "w") as f:
        f.write("01234567890123456789")

    testif(ed_find(fn, "345") == [3, 13], "ed_find: two matches")
    testif(ed_find(fn, "356") == [], "ed_find: no matches")

def test_ed_replace() -> None:
    '''Unit test for ed_replace().'''
    fn = "test_replace.txt"
    with open(fn, "w") as f:
        f.write("01234567890123456789")
    n = ed_replace(fn, "345", "ABCDE", 1)
    testif(n == 1 and ed_read(fn) == "0123456789012ABCDE6789",
           "ed_replace: second occurrence")
    with open(fn, "w") as f:
        f.write("01234567890123456789")
    n = ed_replace(fn, "345", "ABCDE")
    testif(n == 2 and ed_read(fn) == "012ABCDE6789012ABCDE6789",
           "ed_replace: all occurrences")
    n = ed_replace(fn, "ABC", "X", 5)
    testif(n == 0 and ed_read(fn) == "012ABCDE6789012ABCDE6789",
           "ed_replace: occurrence too large")

    
def main() -> None:
    """Show how to use ed_ functions"""

    fn = "file1.txt"
    open(fn, "w").close()

    ed_append(fn, "0123456789")
    ed_append(fn, "0123456789")

    print(ed_read(fn, 3, 9))
    print(ed_read(fn, 3))
    print(ed_find(fn, "345"))
    print(ed_find(fn, "356"))
    print(ed_replace(fn, "345", "ABCDE", 1))
    print(ed_read(fn))

    test_ed_find()
    test_ed_replace()

main()
