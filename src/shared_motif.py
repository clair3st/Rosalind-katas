"""Find shared motif."""

from sys import argv
from profile import format_data


def long_substr(data):
    """Loop through each character to be start of substring.

    keep track of a substrings that appear in all items in list.

    Update for the longest substring.
    """
    substr = ''
    for i in range(len(data[0])):
        for j in range(len(data[0]) - i + 1):
            if j > len(substr) and is_substr(data[0][i:i + j], data):
                substr = data[0][i:i + j]
    return substr


def is_substr(find, data):
    """Return true if substring is in all items of data."""
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


if __name__ == '__main__':  # pragma: no cover
    script, filename = argv

    def open_file(file):
        """Open test file and return as string."""
        with open(file) as f:
            output = f.read()
        return output

    data = format_data(open_file(filename))

    print(long_substr(data))
