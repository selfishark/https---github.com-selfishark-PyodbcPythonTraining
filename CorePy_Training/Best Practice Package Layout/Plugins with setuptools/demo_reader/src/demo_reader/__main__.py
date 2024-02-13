""" Example of package execution
     - to execute a directory as a package add __main__ to the root of the directory and execute the directory -m argument
     - - having __main__ and __ init__ in the same directory creates the confusion that is -m argument is used

    Usage:
        python -m demo_reader test.bz2     # package execution
"""

import sys
from .multireader import MultiReader

print("I am executing demo_reader/__main__.py as a package")

filename = sys.argv[1]
r = MultiReader(filename)
print(r.read())
r.close()
