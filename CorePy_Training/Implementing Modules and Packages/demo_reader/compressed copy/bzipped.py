# demo_reader/compressed/bzppied.py
import bz2
import sys

# Usage:
# python -m demo_reader.compressed.bzipped test.bz2 data compressed with bz2

opener = bz2.open

if __name__ == "__main__":
    f = bz2.open(sys.argv[1], mode='wt')
    f.write(' '.join(sys.argv[2:]))
    f.close()
