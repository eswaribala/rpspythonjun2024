import time
seconds = time.time()
print("Seconds since epoch =", seconds)
# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)
print("This is printed immediately.")
#The sleep() function suspends (delays) execution of the current thread
# for the given number of seconds.
time.sleep(2.4)
print("This is printed after 2.4 seconds.")
'''
time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, 
                    tm_hour=6, tm_min=35, tm_sec=17, 
                    tm_wday=3, tm_yday=361, tm_isdst=0)
'''

result = time.localtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

result = time.gmtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

local_time = time.mktime(t)
print("Local time:", local_time)

seconds = 1545925769

# returns struct_time
t = time.localtime(seconds)
print("t1: ", t)

# returns seconds from struct_time
s = time.mktime(t)
print("\s:", seconds)

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Result:", result)

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)

time_string = "21 June, 2018"
result = time.strptime(time_string, "%d %B, %Y")

print(result)