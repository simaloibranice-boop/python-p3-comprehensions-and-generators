

def square_numbers(numbers):
    """Return a list of squares of the given numbers."""
    return [n**2 for n in numbers]

def get_even_numbers(numbers):
    """Return a list containing only the even numbers."""
    return [n for n in numbers if n % 2 == 0]

def flatten_matrix(matrix):
    """Flatten a 2D list into a 1D list."""
    return [num for row in matrix for num in row]

def uppercase_strings(strings):
    """Return a list of all strings in uppercase."""
    return [s.upper() for s in strings]

def squares_generator(numbers):
    """Return a generator that yields squares of numbers."""
    return (n**2 for n in numbers)
