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


def is_compound_file_binary_format(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    header = b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1"
    header_offset = 0

    return validate_header(data, header, header_offset)


def is_doc(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    header = b"\xEC\xA5\xC1\x00"
    header_offset = 512
    return is_compound_file_binary_format(data) and validate_header(
        data, header, header_offset
    )


def is_docx(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    return is_microsoft_openxml(data) and b"word/document.xml" in data


def is_xls(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    header1 = b"\xFD\xFF\xFF\xFFnn\x00"
    header2 = b"\xFD\xFF\xFF\xFFnn\x02"
    header3 = b"\x09\x08\x10\x00\x00\x06\x05\x00"
    header_offset = 512
    return is_compound_file_binary_format(data) and any(
        (
            validate_header(data, header1, header_offset),
            validate_header(data, header2, header_offset),
            validate_header(data, header3, header_offset),
        )
    )


def is_xlsx(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    return is_microsoft_openxml(data) and b"xl/workbook.xml" in data


def is_ppt(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    header1 = b"\xA0\x46\x1D\xF0"
    header2 = b"\x00\x6E\x1E\xF0"
    header3 = b"\x0F\x00\xE8\x03"
    header4 = b"\xFD\xFF\xFF\xFFnnnn\x00\x00"
    file_signature1 = b"\x50\x00\x6F\x00\x77\x00\x65\x00\x72\x00\x50\x00\x6F\x00\x69\x00\x6E\x00\x74\x00\x20\x00\x44\x00\x6F\x00\x63\x00\x75\x00\x6D\x00\x65\x00\x6E\x00\x74\x00"
    file_signature2 = b"\x5F\xC0\x91\xE3"
    header_offset = 512
    return is_compound_file_binary_format(data) and any(
        (
            validate_header(data, header1, header_offset),
            validate_header(data, header2, header_offset),
            validate_header(data, header3, header_offset),
            validate_header(data, header4, header_offset),
            (file_signature1 in data and file_signature2 in data),
        )
    )


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


def is_gif(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    header1 = b"\x47\x49\x46\x38\x37\x61"
    header2 = b"\x47\x49\x46\x38\x39\x61"
    return validate_header(data, header1) or validate_header(data, header2)


def is_bmp(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    header = b"\x42\x4D"
    return validate_header(data, header)


def is_tif(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    header = b"\x49\x49\x2A\x00"
    return validate_header(data, header)


def is_heic(file: Union[str, bytes]) -> bool:
    data = get_bytes(file)
    header = b"ftypheic"
    offset = 4
    return validate_header(data, header, offset)
