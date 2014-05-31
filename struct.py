"""
Python *struct* Module
======================

This module provides a special class that provides much of the same
functionality as a MATLAB ``struct``.  It is essentially the same as the
:class:`dict` class but uses an alternative, more compact syntax.
"""


# Version information:
#  2014.05.30 @ddalle  : First version
__version__ = "1.0"

# Struct interface
class struct:
    """
    MATLAB/GNU Octave struct interface
    """
    # This keyword tells Python to allow arbitrary attribute assignments to
    # instances of this class.
    pass
    
    # Define the initialization function.
    def __init__(self, *args, **kwargs):
        """
        MATLAB/GNU Octave struct initialization.
        
        Inputs may be specified in three primary ways.  The first two ways are
        identical to the behavior of MATLAB structs; once an empty struct is
        created, you can assign "fields" (this is the MATLAB terminology; Python
        would prefer to call them attributes) using assignments similar to
        ``s.k1 = v1``.  The second way is to give a list of alternating strings 
        
        :Call:
            >>> s = struct()
            >>> s.k1 = v1
            >>> s = struct(f1, v1, f2, v2, ... )
            >>> s = struct(k1=v1, k2=v2, ... )
            >>> s = struct(f1, v1, k2=v2)
            
        :Inputs:
            *f1*: :class:`str`
                Name of the first field (e.g., ``'k1'``)
            *v1*: any type
                Value of the first field, can be any Python variable
            *k1*: a keyword
                Name of a keyword; this is not actually a variable
        
        :Outputs:
            *s*: :class:`olab.struct`
                Instance of a struct that can have additional fields set after
                it has been defined.
        """
        # Number of regular arguments.
        narg = len(args)
        # Check for consistency.
        if narg % 2 != 0:
            raise TypeError("Received an odd number of regular args.")
        # Loop through the argument pairs.
        for i in range(0, narg, 2):
            # Get the field name and value.
            f = args[i]
            v = args[i+1]
            # Attempt to set it.
            setattr(self, f, v)
        # Assign the keyword arguments.
        self.assign_from_dict(kwargs)
        # End.
        return None
        
    
    # Method to assign fields based on a dictionary.
    def assign_from_dict(self, keys):
        """
        Assign fields and values to a struct based on a dictionary input.
        
        :Call:
            >>> s.assign_from_dict(keys)
        
        :Inputs:
            *s*: :class:`olab.struct`
                Struct to have additional fields set
            *keys*: :class:`dict`
                Dictionary of keys and values to set to fields and values
        
        :Outputs:
            ``None``
        """
        # Number of keys.
        nkey = len(keys)
        # Loop through the keys.
        for k in keys.keys():
            # Assign the value.
            setattr(self, k, keys[k])
        # End.
        return None
        
    
    # Function to get the fieldnames
    def fieldnames(self):
        """
        List field names (in MATLAB parlance) of a struct
        
        :Call:
            >>> F = s.fieldnames()
        
        :Inputs:
            *s*: :class:`olab.struct`
                Struct from which to obtain list of attributes/fields
        
        :Outputs:
            *F*: :class:`list`
                List of strings giving the names of the attributes/fields
        """
        # Convert to dictionary and return the keywords.
        return self.__dict__.keys()
        
    
    # Method to display the contents of the struct.
    def __repr__(self):
        """
        Display contents of struct.
        """
        # Use the automatic convert-to-dict capability.
        return "<struct"+self.__dict__.__repr__()+">"
    
    # Do the same thing for the string function.
    def __str__(self):
        """
        Display contents of struct as a string
        """
        # Use the automatic convert-to-dict capability.
        return "<struct"+self.__dict__.__str__()+">"
        
        
# Function to get the fieldnames
def fieldnames(s):
    """
    List field names (in MATLAB parlance) of a struct
    
    :Call:
        >>> F = fieldnames(s)
    
    :Inputs:
        *s*: :class:`olab.struct`
            Struct from which to obtain list of attributes/fields
    
    :Outputs:
        *F*: :class:`list`
            List of strings giving the names of the attributes/fields
    """
    # Convert to dictionary and return the keywords.
    return s.__dict__.keys()
            
