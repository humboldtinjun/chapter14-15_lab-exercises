#write a function called is_after, takes two time objects and tells which one is later using True or False
class Date:
    """Represents a year, month, and day"""

def make_date(year, month, day):
    date = Date()
    date.year = year
    date.month = month
    date.day = day
    return date

def print_date(date):
    c = f'{date.year}-{date.month}-{date.day}'
    print(c)

def is_after(d1, d2):
    """test whether d1 comes after d2"""
    return (d1.year, d1.month, d1.day) > (d2.year, d2.month, d2.day)

date1 = make_date(1933, 6, 22)
print_date(date1)