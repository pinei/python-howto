def raise_to(exp):
    def raise_to_exp(x):
        # Variable exp will be in __closure__
        return pow(x, exp)
    return raise_to_exp

square = raise_to(2)
print(f'square(3) = {square(3)}')
print(square.__closure__)
# square(3) = 9
# (<cell at 0xffff894b7d90: int object at 0xffff89fd23f0>,)

cube = raise_to(3)
print(f'cube(3) = {cube(3)}')
print(cube.__closure__)
# cube(3) = 27
# (<cell at 0xffff894b7d00: int object at 0xffff89fd2410>,)

# Hacking closure
# https://stackoverflow.com/questions/37665862/how-to-create-new-closure-cell-objects
hypercube = cube
dimensions = 4

import ctypes
PyCell_Set = ctypes.pythonapi.PyCell_Set
PyCell_Set.argtypes = (ctypes.py_object, ctypes.py_object)
PyCell_Set.restype = ctypes.c_int
PyCell_Set(hypercube.__closure__[0], dimensions)
print(f'hypercube(3) = {hypercube(3)}')
# hypercube(3) = 81