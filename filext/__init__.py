from typing import Union

from filext.classifiers import *
from filext.utils import lookup_file_type


def whatfile(file: Union[str, bytes]) -> Union[str, None]:
    """
    Identifies the file type by calling each classifier

    Args:
        file (Union[str, bytes]): path to file or bytes of file

    Returns:
        str: found file type or None
    """
    classifiers = (
        whatdoc,
        whatimage,
    )
    for classifier in classifiers:
        result = classifier(file)
        if result:
            return result


def whatdoc(file: Union[str, bytes]) -> Union[str, None]:
    """
    Identifies the file type by calling each document classifier

    Args:
        file (Union[str, bytes]): path to file or bytes of file

    Returns:
        Union[str,None]: found file type or None
    """
    file_types = {
        "docx": is_docx,
        "pptx": is_pptx,
        "xlsx": is_xlsx,
        "pdf": is_pdf,
    }
    return lookup_file_type(file, file_types)


def whatimage(file: Union[str, bytes]) -> Union[str, None]:
    """
    Identifies the file type by calling each image classifier

    Args:
        file (Union[str, bytes]): path to file or bytes of file

    Returns:
        Union[str,None]: found file type or None
    """
    file_types = {
        "bmp": is_bmp,
        "gif": is_gif,
        "heic": is_heic,
        "jpg": is_jpg,
        "png": is_png,
        "tif": is_tif,
    }
    return lookup_file_type(file, file_types)
