import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = fh.read().splitlines()

setuptools.setup(
    name="transport-accessibility-python",
    version="0.1.0",
    author="Nicolás Villalobos",
    author_email="guillermo.nicolás@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Codegn/transport-accessibility-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    packages=['transport_accessiblity.core'],
    install_requires=install_requires,
)