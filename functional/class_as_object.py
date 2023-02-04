def sequence_class(immutable):
    # Conditional expression
    return tuple if immutable else list

seq1 = sequence_class(immutable=True)
t1 = seq1({ "One", "Two", "Three" })

print(f'Sequence {t1} of type {type(t1)}')

seq2 = sequence_class(immutable=False)
t2 = seq2({ "One", "Two", "Three" })

print(f'Sequence {t2} of type {type(t2)}')
