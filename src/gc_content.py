"""Calculate the GC content."""

from sys import argv


def format_data(fasta):
    """Format Fasta file into dict."""
    step1 = fasta.split()
    step2 = ''.join(step1)
    step3 = step2.split('>')[1:]
    return {i[:13]: i[13:] for i in step3}


def gc_content(dna):
    """Given text file of Dna string find highest GC content."""
    gc = (dna.count('C') + dna.count('G')) / float(len(dna))
    return gc * 100


def highest_gc(data):
    """Given a dict of dna return with highest gc."""
    highest_gc = max((gc_content(v), k) for k, v in data.items())
    return highest_gc[1] + '\n' + str(highest_gc[0])


if __name__ == '__main__':  # pragma: no cover
    script, filename = argv

    def open_fasta(file):
        """Open test file and return as string."""
        with open(file) as fasta:
            output = fasta.read()
        return output

    opened = open_fasta(filename)
    print(highest_gc(format_data(opened)))
