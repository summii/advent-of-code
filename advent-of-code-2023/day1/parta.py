from aocd import get_data

inp = get_data(day=1, year=2023)

def get_digits(s):
    first = None
    last = None
    for o in s:
        if o.isdigit():
            if first is None:
                first = o
            last = o
    return int(first + last)

def solve1a(lines):
    res = 0
    for o in lines:
        res += get_digits(o)
    return res

lines = inp.splitlines()
print(lines[:3])
print(solve1a(lines))