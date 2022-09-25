import pathlib

from filext import whatdoc, whatfile, whatimage


def test_whatfile(all_files):
    file_ext = pathlib.Path(all_files).suffix.strip(".")
    image_type = whatfile(all_files)
    assert file_ext == image_type


def test_documents(document_files):
    file_ext = pathlib.Path(document_files).suffix.strip(".")
    image_type = whatdoc(document_files)
    assert file_ext == image_type


def test_images(image_files):
    file_ext = pathlib.Path(image_files).suffix.strip(".")
    image_type = whatimage(image_files)
    assert file_ext == image_type
