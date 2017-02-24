"""Consensus and Profile."""

from sys import argv


def format_data(fasta):
    """Format fasta file into list of DNA strings."""
    # return [val for idx, val in enumerate(fasta) if idx % 2 != 0]
    step1 = fasta.split()
    step2 = ''.join(step1)
    step3 = step2.split('>')[1:]
    return [i[13:] for i in step3]


def generate_profile(dna):
    """Generate profile matrix."""
    profile = {'A': [0] * len(dna[0]),
               'C': [0] * len(dna[0]),
               'G': [0] * len(dna[0]),
               'T': [0] * len(dna[0])}
    for strand in dna:
        for idx, base in enumerate(strand):
            profile[base][idx] += 1
    return profile


def generate_consensus(profile):
    """Generate consensus sequence from profile."""
    consen = [max(profile.items(), key=lambda p: p[1][idx])[0]
              for idx in range(len(profile['A']))]
    return ''.join(consen)


def visualize_profile(profile):  # pragma: no cover
    """Visualize profile in required format."""
    bases = ['A', 'C', 'G', 'T']

    for base in bases:
        print('{}: {}'.format(
            base,
            ' '.join([str(num) for num in profile[base]])
        ))


if __name__ == '__main__':  # pragma: no cover
    script, filename = argv

    def open_file(file):
        """Open test file and return as string."""
        with open(file) as fasta:
            output = fasta.read()
        return output

    data = format_data(open_file(filename))
    profile = generate_profile(data)
    print(generate_consensus(profile))
    visualize_profile(profile)
