# write a function called subtract-time that takes two time objects and returns the interval betwwn them in seconds
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
