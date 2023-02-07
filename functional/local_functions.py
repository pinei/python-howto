def sort_by_last_letter(strings):
    
    # Local function
    # A new function is created every time sort_by_last_letter is executed
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)

countries = ['Brazil', 'Uruguay', 'Argentina']
print(sort_by_last_letter(countries))
# ['Argentina', 'Brazil', 'Uruguay']