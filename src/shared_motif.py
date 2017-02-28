"""Find shared motif."""

from sys import argv
from profile import format_data


def long_substr(data):
    """Loop through each character to be start of substring.

    keep track of a substrings that appear in all items in list.

    Update for the longest substring.
    """
    longest_substr = ''
    for start_idx in range(len(data[0])):
            for len_substr in range(len(data[0]) - start_idx + 1):
                substr = data[0][start_idx:start_idx + len_substr]
                if len_substr > len(longest_substr) and all(
                    substr in dna for dna in data
                ):
                    longest_substr = substr
    return longest_substr


if __name__ == '__main__':  # pragma: no cover
    script, filename = argv

    def open_file(file):
        """Open test file and return as string."""
        with open(file) as f:
            output = f.read()
        return output

    data = format_data(open_file(filename))

    print(long_substr(data))
