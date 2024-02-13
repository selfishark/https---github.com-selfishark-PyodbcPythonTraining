# Define an outer function that takes a parameter 'x'
def outer_function(x):
    # This is the outer enclosing function

    # Define an inner function that modifies 'x'
    def inner_function():
        # This is the inner function
        # 'nonlocal' keyword allows us to assign to 'x' in the nearest enclosing scope that is not global
        nonlocal x
        x += 1
        print("Inner function:", x)

    # Call the inner function
    inner_function()
    # Print 'x' after it's been modified by the inner function
    print("Outer function:", x)

# Define a global variable 'x'
x = 10
# Call the outer function with 'x' as an argument
outer_function(x)
# Print 'x' in the global scope, which remains unchanged
print("Global scope:", x)

##############################################################################

# Define an outer function that takes a parameter 'x'
def outer_function(x):
    # Define a local variable 'y' within the outer function
    y = 10

    # Define an inner function that accesses 'y' and 'x'
    def inner_function():
        # Print the local variable 'y'
        print("Local variable:", y)

        # 'nonlocal' keyword allows us to assign to 'x' in the nearest enclosing scope that is not global
        # In this case, 'x' is a parameter of the outer function
        print("Nonlocal variable:", x)

    # Return the inner function, creating a closure
    return inner_function

# Define a global variable 'global_var'
global_var = 20

# Create a closure by calling the outer function with 'global_var' as an argument
closure_1 = outer_function(5)
closure_2 = outer_function(global_var)

# Call the closure, which will print the values of 'y' and 'x'
closure_1()
closure_2()

###############################################################################

# Define an outer function
def outer_function():
    # Define a local variable 'global_var' within the outer function
    global_var = 10

    # Define an inner function that adds 'global_var' and 'local_var'
    def inner_function():
        # Define a local variable 'local_var' within the inner function
        local_var = 5
        # Return the sum of 'global_var' and 'local_var'
        return global_var + local_var

    # Return the inner function, creating a closure
    return inner_function


# Create a closure by calling the outer function
closure = outer_function()

# Call the closure, which will return the sum of 'global_var' and 'local_var'
result = closure()
# Print the result
print(result)  # Output: 15