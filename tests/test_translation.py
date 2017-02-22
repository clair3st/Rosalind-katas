"""Translation RNA testing."""

RNA = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'


def test_translation():
    """Test translation function."""
    from src.translation import translation
    assert translation(RNA) == 'MAMAPRTEINSTRING'
