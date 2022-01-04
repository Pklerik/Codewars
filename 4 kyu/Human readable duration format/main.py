import time

def format_duration(seconds):
    if seconds == 0:
        return "now"
    minutes = seconds // 60
    last_seconds = seconds % 60
    hours = minutes // 60
    last_minutes  = minutes % 60

    if hours > 1:
        hours_name = "hours"
    else:
        hours_name = "hour"
    
    if last_minutes > 1:
        minutes_name = "minutes"
    else:
        minutes_name = "minute"

    if last_seconds > 1:
        seconds_name = "seconds"
    else:
        seconds_name = "second"
    
    
    return  str(hours) + hours_name + str(last_minutes) + minutes_name + str(last_seconds) + seconds_name

print(format_duration(3662))