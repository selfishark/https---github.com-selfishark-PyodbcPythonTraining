import setuptools

setuptools.setup(
    name="demo_reader_bz2_plugin",
    version="0.0.0",
    descipiton="Demo reader plugin for reading bz2 files.",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={                  # entry_points name list of extensions for the different plugins
        'demo_reader.compression_plugins': [
            'bz2 = demo_reader_bz2.bzipped'     # bz2 compression plugin
        ]
    }
)
