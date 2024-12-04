from aocd import get_data

inp = get_data(day=1, year=2023)

dnames = 'zero, one, two, three, four, five, six, seven, eight, nine'.split(', ')

def dig_starts(a):
    if a[0].isdigit(): return int(a[0])
    return [o for o in dnames if o.startswith(o)]
    
def get_digits(found):
    for o in found:
        if isinstance(o, int): return o
        if o: return dnames.index(o[0])

def both_digit(x):
    starts = [x[o:] for o,p in enumerate(x)]
    found = [dig_starts(o) for o in starts]
    first = get_digits(found)
    last = get_digits(reversed(found))
    return first*10 + last

sum = sum([both_digit(x) for x in inp.splitlines()])
print(sum)
