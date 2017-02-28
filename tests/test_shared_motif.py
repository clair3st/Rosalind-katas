"""Test shared motif."""

import pytest

TEST_DATA = [
    (['GATTACA', 'TAGACCA', 'ATACA'], 'TA'),
    (['CAT', 'CAT', 'CAT'], 'CAT')
]


@pytest.mark.parametrize('data, substring', TEST_DATA)
def test_is_substring(data, substring):
    """Test the longest substring function."""
    from src.shared_motif import longest_substring
    assert longest_substring(data) == substring
