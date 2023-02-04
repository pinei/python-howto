import socket

class Resolver:
    def __init__(self):
        self._cache = {}
    
    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

resolve = Resolver()

print(resolve('sixty-north.com'))
# '93.93.131.30'

print(resolve('sixty-north.com')) # cached
# '93.93.131.30'

print(resolve('pluralsight.com'))
# '35.167.189.185'

print(resolve._cache)
# {'sixty-north.com': '93.93.131.30', 'pluralsight.com': '35.167.189.185'}

from timeit import timeit

first_run = timeit(setup='from __main__ import resolve', stmt="resolve('google.com')", number=1)

second_run = timeit(setup='from __main__ import resolve', stmt="resolve('google.com')", number=1)

print("First run: {:f}".format(first_run))

print("Second run: {:f}".format(second_run))