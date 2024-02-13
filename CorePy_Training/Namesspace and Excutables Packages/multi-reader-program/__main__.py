""" Example of directory execution
     - to execute a directory as a package add __main__ to the root of the directory and execute the directory -m argument
     - zip files can also be executed as same as directories

    Usage:
        python multi-reader-program test.bz2        # directory execution
        python multi-reader-program.zip test.bz2    # zip file execution
        python -m multi-reader-program test.bz2     # package execution
"""

import sys
from demo_reader.multireader import MultiReader

print("I am executing multi-program-reader/__main__.py as part of directory execution")

filename = sys.argv[1]
r = MultiReader(filename)
print(r.read())
r.close()
