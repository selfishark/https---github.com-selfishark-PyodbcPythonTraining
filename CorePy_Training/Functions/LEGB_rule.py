# Define a global variable 'g'. This is in the Global scope.
g = 'global'

# Define an outer function with a default parameter 'p'. This is in the Enclosing scope.
def outer(p='parameter'):
    # Define a local variable 'l' within the outer function. This is in the Local scope.
    l = 'local'
    
    # Define an inner function within the outer function.
    def inner():
        # Print the values of 'g', 'p', and 'l'. Python will look for these variables in the following order:
        # Local -> Enclosing -> Global -> Built-in (LEGB)
        print(g,p,l)
    
    # Call the inner function. At this point, 'inner' is in the Local scope of 'outer'.
    inner()

# Call the outer function. At this point, 'outer' is in the Global scope.
outer()