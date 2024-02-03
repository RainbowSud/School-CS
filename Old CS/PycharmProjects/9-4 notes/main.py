import time

seconds = int(time.time())
print("It has been:", seconds, "seconds since 1970")
currentSecond = seconds % 60
print("The current second is:", currentSecond)
minutes = seconds // 60
print("It has been:", minutes, "minutes since 1970")
currentMinute = minutes % 60
print("The current minute is:", currentMinute)
hours = minutes // 60
print("It has been:", hours, "hours since 1970")
currentHour = hours % 24
print("The current hour in GMT is:", currentHour)
print("Current GMT time:", currentHour,":", currentMinute,":", currentSecond)
