from typing import Union

from filext.utils import get_bytes, validate_header, validate_trailer


def is_microsoft_openxml(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    header = b"\x50\x4B\x03\x04\x14\x00\x06\x00"
    header_offset = 0
    trailer = b"\x50\x4B\x05\x06"
    trailer_offset = 18

    return validate_header(data, header, header_offset) and validate_trailer(
        data, trailer, trailer_offset
    )


def is_docx(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    return is_microsoft_openxml(data) and b"word/document.xml" in data


def is_xlsx(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    return is_microsoft_openxml(data) and b"xl/workbook.xml" in data


def is_pptx(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    return is_microsoft_openxml(data) and b"ppt/presentation.xml" in data


def is_pdf(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    header = b"\x25\x50\x44\x46"
    return validate_header(data, header)


def is_png(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    header = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
    trailer = b"\x49\x45\x4E\x44\xAE\x42\x60\x82"
    return validate_header(data, header) and validate_trailer(data, trailer)


def is_jpg(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    header = b"\xFF\xD8\xFF"
    trailer = b"\xFF\xD9"
    return validate_header(data, header) and validate_trailer(data, trailer)
