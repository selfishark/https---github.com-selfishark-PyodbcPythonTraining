# demo_reader/compressed/gzppied.py

import gzip
# from demo_reader.util import writer
from demo_reader.util import writer

extension = '.bz2'
opener = gzip.open  # alias for gzip.open (decompress during readings)

if __name__ == "__main__":
    writer.main(opener)