import pytest

from filext import checkers


@pytest.mark.parametrize(
    "filepath, checker",
    [
        ("tests/files/document.docx", checkers.is_docx),
        ("tests/files/document.pptx", checkers.is_pptx),
        ("tests/files/document.xlsx", checkers.is_xlsx),
        ("tests/files/document.pdf", checkers.is_pdf),
    ],
)
def test_checkers_valid(filepath, checker):
    assert checker(filepath)


@pytest.mark.parametrize(
    "filepath, checker",
    [
        ("tests/files/document.docx", checkers.is_pptx),
        ("tests/files/document.pptx", checkers.is_xlsx),
        ("tests/files/document.xlsx", checkers.is_pdf),
        ("tests/files/document.pdf", checkers.is_docx),
    ],
)
def test_checkers_invalid(filepath, checker):
    assert not checker(filepath)
