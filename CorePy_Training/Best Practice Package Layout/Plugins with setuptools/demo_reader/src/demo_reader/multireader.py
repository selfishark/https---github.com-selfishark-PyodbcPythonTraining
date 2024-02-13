"""
package extension of 'multireader' using setuptools
"""

# demo_reader/multireader.py

import os
import pkg_resources

# build set of modules objects
compression_plugins = {
    entry_point.load()    # import module with entrypoint
    for entry_point,
    in pkg_resources.iter_entry_points('demo_reader.compression_plugins')   # find modules to import by iteration over all extensions to the entry_points
}

# build files extension map to corresponding open method
extension_map = {
    module.extension: module.opener     # look for module-level attributes
    for module in compression_plugins   # get modules from compression_plugins
}


class MultiReader:
    """
    A class for reading files, supporting both compressed and uncompressed formats.

    Methods:
        __init__(filename): Initialize the MultiReader with the given filename.
        close(): Close the file.
        read(): Read the contents of the file.

    Attributes:
        f: File object representing the opened file.

    """
    def __init__(self, filename):
        """
        Initialize the MultiReader with the given filename.

        Args:
            filename (str): The path to the file to be read.

        Returns:
            None
        """
        extension = os.path.splitext(filename)[1]    # collect the extension from the filename
        opener = extension_map.get(extension, open)  # get the appropriate extension opener of compressed file, or default to 'open' for uncompressed files
        self.f = opener(filename, 'rb')              # open the file in read text mode once the extension is found in the dictionary

    def close(self):
        """Close the MultiReader"""
        self.f.close()

    def read(self):
        """Read"""
        return self.f.read()
