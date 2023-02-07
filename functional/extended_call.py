def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

# Extended call syntax
t = (11, 12, 13, 14)
print_args(*t)
# 11
# 12
# (13, 14)

def color(red, green, blue, **kwargs):
    print(f'r = {red}')
    print(f'g = {green}')
    print(f'b = {blue}')
    print(kwargs)

# Extended call syntax for mapping
k = { 'red': 128, 'green': 0, 'blue': 255, 'alpha': 1.0}
color(**k)
# r = 128
# g = 0
# b = 255
# {'alpha': 1.0}

# dict() uses **kwargs in its initialer
k = dict(red=128, green=0, blue=255, alpha=1.0)
color(**k)
# r = 128
# g = 0
# b = 255
# {'alpha': 1.0}

# Argument forwarding
def trace(f, *args, **kwargs):
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')
    result = f(*args, **kwargs)
    print(f'result = {result}')

trace(int, 'ff', base=16)
# args = ('ff',)
# kwargs = {'base': 16}
# result = 255