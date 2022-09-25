import glob

import pytest


@pytest.fixture(params=glob.glob("./tests/files/image*"))
def image_files(request):
    yield request.param


@pytest.fixture(params=glob.glob("./tests/files/document*"))
def document_files(request):
    yield request.param


@pytest.fixture(params=glob.glob("./tests/files/*"))
def all_files(request):
    yield request.param
