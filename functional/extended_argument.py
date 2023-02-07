

# Arbitrary number of positional arguments
def multiple_args(*args):
    print(args)
    print(type(args))

multiple_args(3, 4, 5)
# (3, 4, 5)
# <class 'tuple'>


def hypervolume(*lengths):
    # in Python, an iterator is an object which implements the iterator protocol,
    # which consist of the methods __iter__() and __next__()
    # Lists, tuples, dictionaries, and sets are all iterable objects.
    i = iter(lengths)
    v = next(i)
    for length in i:
        v = v * length
    return v

print(hypervolume(10, 20, 30))
# 6000

# Arbitrary keyword arguments
def keyword_arguments(**kwargs):
    print(kwargs)
    print(type(kwargs))

keyword_arguments(x=10, y=20, z=30)
# {'x': 10, 'y': 20, 'z': 30}
# <class 'dict'>

def tag(name, **attributes):
    result = f'<{name}'
    for (attr, value) in attributes.items():
        result += f' {attr}="{str(value)}"'
    return result + '>'

print(tag('img', src='image.png', alt='Sample image', border=1))

# Mixed
def mixed_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)

mixed_args(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7, kwarg3=8, kwarg4=9)
# 1
# 2
# (3, 4, 5)
# 6
# 7
# {'kwarg3': 8, 'kwarg4': 9}

# Positional only arguments
# Prevent formal argument names from becoming part of the API
# Useful when the names have no semantic meanging
def number_length(x, /):
    print(len(str(x)))

number_length(2112)
# 4

number_length(x=2112)
# TypeError: number_length() got some positional-only arguments passed as keyword arguments: 'x'

