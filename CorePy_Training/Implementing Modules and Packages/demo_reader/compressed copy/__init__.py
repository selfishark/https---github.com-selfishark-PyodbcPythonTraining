# The __all__ list is used to specify what names should be exported when someone imports the package using the from package import * syntax.

from demo_reader.compressed.bzipped import opener as bz2_opener
from demo_reader.compressed.gzipped import opener as gzip_opener

__all__ = ["bz2_opener", "gzip_opener"]
