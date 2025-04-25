# write a function that takes two time objects and tells you which one is later in the day
class Time:
    """Represents a time of day."""

#make a time object
def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

def print_time(time):
    s = f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}'
    print(s)

#print time object
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def subtract_time(t1, t2):
    seconds1 = time_to_int(t1)
    seconds2 = time_to_int(t2)
    return seconds1 - seconds2

def is_after(t1, t2):
    """checks if t1 is after t2"""
    return time_to_int(t1) > time_to_int(t2)

t1 = make_time(10, 0, 0)  # 10:00:00
t2 = make_time(9, 30, 0)  # 9:30:00

print(is_after(t1, t2))  # ➔ True
print(is_after(t2, t1))  # ➔ False
