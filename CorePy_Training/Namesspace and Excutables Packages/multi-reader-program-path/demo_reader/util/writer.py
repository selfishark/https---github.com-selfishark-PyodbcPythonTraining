# demo_reader/util/writer.py

import sys



def main (opener):
    f = opener(
    sys.argv[1], mode="wt"
    )   # Open a bz2-compressed file for writing. The filename is taken from the first command-line argument (sys.argv[1]), and the mode is set to 'wt' (text writing mode).
        # sys.argv[1] contains the path to new compressed file
    f.write(
        ' '.join(sys.argv[2:])
    )  # Concatenate the contents of the command-line arguments (excluding the script name) and write the resulting string to the compressed file
    f.close() 