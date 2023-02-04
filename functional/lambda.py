scientists = ['Maria Curie', 'Albert Einstein', 'Rosalind Franklin', 'Niels Bohr', 'Dian Fossey', 'Isaac Newton'
    'Grace Hopper', 'Charls Darwin', 'Lise Meitner']

# First name
# Statement which defines a function and binds it to a name
def first_name(name): return name.split()[0]
print(first_name('Nikola Tesla'))

# Last name
# Lambda is an expression which evaluates to a function
last_name = lambda name: name.split()[-1]
print(last_name('Nikola Tesla'))

print(sorted(scientists, key=last_name))