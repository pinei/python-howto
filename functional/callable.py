def is_even(x):
    return x % 2 == 0

print(f'is_even is callable? {callable(is_even)}')
# True

print(f'list is callable? {callable(list)}')
# True

print(f'list.append is callable? {callable(list.append)}')
# True

class CallMe:
    def __call__(self):
        print('Called me!')

my_call_me = CallMe()

print(f'my_call_me is callable? {callable(my_call_me)}')
# True

print(f'a string is callable? {callable("Not callable")}')
# False