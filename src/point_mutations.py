"""Calculate the Hamming distace."""

from sys import argv


def hamming_dist(a, b):
    """Given two DNA strands return the hamming distance."""
    return sum(a[i] != b[i] for i in range(len(a)))


if __name__ == '__main__':  # pragma: no cover
    script, filename = argv

    def open_file(file):
        """Open test file and return as string."""
        with open(file) as f:
            output = f.readlines()
        return output

    a, b = open_file(filename)
    print(hamming_dist(a, b))
