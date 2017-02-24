"""Consensus and Profile."""


def format_data(fasta):
    """Format fasta file into list of DNA strings."""
    return [val for idx, val in enumerate(fasta) if idx % 2 != 0]


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
    consen = [max(profile.items(), key=lambda p: p[1][i])[0]
              for i in range(len(profile['A']))]
    return ''.join(consen)
