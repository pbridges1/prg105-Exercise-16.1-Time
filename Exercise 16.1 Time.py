class Time(object):

    """Represents the time of day.
   attributes: hour, minute, second
    """

time = Time()


def print_time():
    time.hour = 11
    time.minute = 59
    time.second = 45
    print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)
print_time()
