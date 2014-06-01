"""
Provide sane Matlab-like functions
"""

# Import NumPy because we're building on some of its functions.
import numpy as _np

# Function to give length regardless of the damn type.
def numel(x):
    """
    Give number of elements in a variable without being ridiculously dependent
    on the type.  Ever wanted to know how big a variable is but don't know
    beforehand if it's a list or NumPy array or maybe just a number?  TOO BAD!  
    THIS IS PYTHON AND WE DON'T LIKE FLEXIBLE THINGS.  Or you can just use this 
    function.
    
    :Call:
        >>> n = numel(x)
    
    :Inputs:
        *x*: :class:`numpy.ndarray` or :class:`list` or :class:`float`, ...
            This can hopefully be any variable, but is really intended for 
            lists, NumPy arrays, and scalars.
    
    :Outputs:
        *n*: :class:`int`
            Number of elements in *x*.  If *x* is an array, this gives the 
            total number in all dimensions, i.e. ``x.size``
    
    :Examples:
        This is supposed to just work without providing a mountain of 
        in-your-face Python caveats
            
            >>> numel(3)
            1
            >>> numel([1, ['2a', '2b'], 3])
            3
            >>> numel(np.array([1, 2, 3]))
            3
            >>> numel(np.array([[1, 2, 3], [4, 5, 6]])
            6
    """
    # Versions:
    #  2014.05.31 @ddalle  : First version
    
    # Check the input type.
    if type(x) is _np.ndarray:
        # NumPy arrays store the thing we're looking for.
        return x.size
        
    elif hasattr(x, '__len__'):
        # For anything else that has len(x), use that.
        return len(x)
        
    else:
        # This is arguable; anything else has numel(x) == 1.
        return 1