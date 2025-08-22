def read_totes(filepath):
    """Reads and returns the totes listed in the file."""
    with open(filepath, "r") as file:
        totes = file.readlines()
    return totes
