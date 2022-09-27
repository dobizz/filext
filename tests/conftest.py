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


@pytest.fixture(params=glob.glob("./tests/files/*.*x"))
def all_ms_openxml_files(request):
    yield request.param


@pytest.fixture(
    params=glob.glob("./tests/files/*.doc")
    + glob.glob("./tests/files/*.ppt")
    + glob.glob("./tests/files/*.xls")
)
def all_cfbf_files(request):
    yield request.param
