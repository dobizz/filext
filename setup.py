import io
import os

import setuptools

# Import the README and use it as the long-description.
try:
    with io.open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"),
        encoding="utf-8",
    ) as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = ""


setuptools.setup(
    name="filext",
    version="0.1.1",
    description="Python library to identify file type based on its file signature",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dobizz/filext",
    author="Ronnie Villanueva",
    author_email="ronnie.code@outlook.com",
    packages=setuptools.find_packages(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
