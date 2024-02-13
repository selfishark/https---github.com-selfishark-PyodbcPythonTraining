import setuptools

setuptools.setup(
    name="demo_reader_gz_plugin",
    version="0.0.0",
    descipiton="Demo reader plugin for reading gz files.",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={                  # entry_points name list of extensions for the different plugins
        'demo_reader.compression_plugins': [
            'gz = demo_reader_gz.bzipped'     # gz compression plugin
        ]
    }
)
