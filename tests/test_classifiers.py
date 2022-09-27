import pytest

from filext import classifiers


@pytest.mark.parametrize(
    "filepath, checker",
    [
        ("tests/files/document.docx", classifiers.is_docx),
        ("tests/files/document.pptx", classifiers.is_pptx),
        ("tests/files/document.xlsx", classifiers.is_xlsx),
        ("tests/files/document.pdf", classifiers.is_pdf),
        ("tests/files/document.doc", classifiers.is_doc),
        ("tests/files/document.ppt", classifiers.is_ppt),
        ("tests/files/document.xls", classifiers.is_xls),
    ],
)
def test_document_checkers_valid(filepath, checker):
    assert checker(filepath)


@pytest.mark.parametrize(
    "filepath, checker",
    [
        ("tests/files/document.docx", classifiers.is_pptx),
        ("tests/files/document.pptx", classifiers.is_xlsx),
        ("tests/files/document.xlsx", classifiers.is_pdf),
        ("tests/files/document.pdf", classifiers.is_docx),
    ],
)
def test_document_checkers_invalid(filepath, checker):
    assert not checker(filepath)


@pytest.mark.parametrize(
    "filepath, checker",
    [
        ("tests/files/image.bmp", classifiers.is_bmp),
        ("tests/files/image.gif", classifiers.is_gif),
        ("tests/files/image.heic", classifiers.is_heic),
        ("tests/files/image.jpg", classifiers.is_jpg),
        ("tests/files/image.png", classifiers.is_png),
        ("tests/files/image.tif", classifiers.is_tif),
    ],
)
def test_image_checkers_valid(filepath, checker):
    assert checker(filepath)


def test_microsoft_openxml(all_ms_openxml_files):
    assert classifiers.is_microsoft_openxml(all_ms_openxml_files)


def test_compound_file_binary_format(all_cfbf_files):
    assert classifiers.is_compound_file_binary_format(all_cfbf_files)
