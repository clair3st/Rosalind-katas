"""Test point mutations."""

DATA = ['GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT']


def test_hamming_distance():
    """Test hamming distance."""
    from src.point_mutations import hamming_dist
    assert hamming_dist(DATA[0], DATA[1]) == 7
