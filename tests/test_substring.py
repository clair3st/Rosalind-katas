"""Test substring to return indexs."""

import pytest

TEST_INPUT = [
    ['GATATATGCATATACTT', 'ATAT', '2 4 10'],
    ['AAAAAAAAA', 'AA', '1 2 3 4 5 6 7 8'],
    ['ATC', 'G', '']
]


@pytest.mark.parametrize('string, sub, idx', TEST_INPUT)
def test_substring(string, sub, idx):
    """Test correct idxs  is returned."""
    from src.substring import substring
    assert substring(string, sub) == idx
