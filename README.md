# filext
Python library to identify file type based on its file signature

### Installation
```
pip install filext
```

### Usage

If the category of the file is not certain, you may use `whatfile` but is a little slower
```python
from filext import whatfile

file_path = "./tests/files/document.pdf"

# pass file as path str
file_type = whatfile(file_path)

with open(filepath, "rb") as file:
    # pass file as bytes
    file_type = whatfile(file.read())
```

If the category of the file is known, you may use the function for that category instead.
```python
from filext import whatdoc

file_path = "./tests/files/document.pdf"

# pass file as path str
file_type = whatdoc(file_path)

with open(filepath, "rb") as file:
    # pass file as bytes
    file_type = whatdoc(file.read())
```

### Supported File Types
#### Documents
- [x] PDF
- [ ] DOC
- [ ] PPT
- [ ] XLS
- [x] DOCX
- [x] PPTX
- [x] XLSX

#### Images
- [x] BMP
- [x] GIF
- [x] HEIC
- [x] JPG
- [x] PNG
- [x] TIF
