"""
A utility for reading compressed and uncompressed files using a common interface.

Usage Example:
    reader = MultiReader('example.gz')
    content = reader.read()
    reader.close()
"""

# demo_reader/multireader.py

import os

from demo_reader.compressed import gzipped, bzipped

# create a dictionary to call the the appropriate opener for each file extension
extension_map = {
    '.gz': gzipped.opener,
    '.bz2': bzipped.opener,
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
