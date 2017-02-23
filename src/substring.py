"""Find a Motif in DNA."""

from sys import argv


def substring(string, substring):
    """Return indexes where substring exists in string."""
    idxs = [str(idx + 1) for idx in range(len(string))
            if string.find(substring, idx) == idx]

    return ' '.join(idxs)


if __name__ == '__main__':  # pragma: no cover
    script, filename = argv

    def open_file(file):
        """Open test file and return as string."""
        with open(file) as f:
            output = f.readlines()
        return output

    a, b = open_file(filename)
    print(substring(a, b))
