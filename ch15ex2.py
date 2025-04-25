# rewrite the date functions as methods
class Date:
    """represents a year, month, and day"""

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'{self.year}-{self.month:02d}-{self.day:02d}'

    def is_after(self, other):
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)

date1 = Date(1933, 6, 22)
date2 = Date(1933, 9, 17)
print(date1)
print(date2.is_after(date1))  # ➔ True
print(date1.is_after(date2))  # ➔ False
