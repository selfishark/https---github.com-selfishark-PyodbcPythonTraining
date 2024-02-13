import setuptools

setuptools.setup(
    name="demo_reader",
    version="1.0.0",
    descipiton="Tool for reading compressed and uncompressed files.",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'}
)

