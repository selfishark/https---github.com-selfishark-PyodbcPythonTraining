# demo_reader/compressed/gzppied.py

import gzip
import sys

# Usage:
# python -m demo_reader.compressed.gzipped test.gz data compressed with gzip


opener = gzip.open  # alias for gzip.open (decompress during readings)

if __name__ == "__main__":  # The block following this statement will only be executed if the script is run directly not if it is imported as a module.
    f = gzip.open(
        sys.argv[1], mode="wt"
    )   # Open a gzip-compressed file for writing. The filename is taken from the first command-line argument (sys.argv[1]), and the mode is set to 'wt' (text writing mode).
        # sys.argv[1] contains the path to new compressed file
    f.write(
        ' '.join(sys.argv[2:])
    )  # Concatenate the contents of the command-line arguments (excluding the script name) and write the resulting string to the compressed file
    f.close()  # close the compresses files
