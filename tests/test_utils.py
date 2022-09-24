import pytest

from filext.utils import get_bytes


@pytest.mark.parametrize("file", ["tests/files/image.png"])
def test_get_bytes_valid(file):
    assert isinstance(get_bytes(file), bytes)


@pytest.mark.parametrize(
    "file",
    [
        0,
        None,
        [],
        {},
        int,
        len,
    ],
)
def test_get_bytes_invalid(file):
    with pytest.raises(TypeError):
        get_bytes(file)
