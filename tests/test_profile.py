"""Test profile and consensus string functions."""

TEST_INPUT = '''>Rosalind_1
                ATCCAGCT
                >Rosalind_2
                GGGCAACT
                >Rosalind_3
                ATGGATCT
                >Rosalind_4
                AAGCAACC
                >Rosalind_5
                TTGGAACT
                >Rosalind_6
                ATGCCATT
                >Rosalind_7
                ATGGCACT'''

FORMAT = ['ATCCAGCT',
          'GGGCAACT',
          'ATGGATCT',
          'AAGCAACC',
          'TTGGAACT',
          'ATGCCATT',
          'ATGGCACT']

PROFILE = {'A': [5, 1, 0, 0, 5, 5, 0, 0],
           'C': [0, 0, 1, 4, 2, 0, 6, 1],
           'G': [1, 1, 6, 3, 0, 1, 0, 0],
           'T': [1, 5, 0, 0, 0, 1, 1, 6]}


def test_correct_format():
    """Test input data is correctly formatted."""
    from src.profile import format_data
    assert format_data(TEST_INPUT) == FORMAT


def test_profile():
    """Test the profile is generate."""
    from src.profile import generate_profile
    assert generate_profile(FORMAT) == PROFILE


def test_generate_consensus():
    """Test consesnus sequence is generated based on profile."""
    from src.profile import generate_consensus
    assert generate_consensus(PROFILE) == 'ATGCAACT'
