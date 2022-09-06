# import time
# time_1=time.time()
# print(time_1)
# print(time_1)
# import time, datetime
# time_1 = time.time()
#
# time.sleep(3)
#
# time_2 = time.time()
# time_interval = time_2 - time_1
# print(time_interval)
# print(time_interval.seconds)
import datetime, time
starttime = datetime.datetime.now()
#long running
time.sleep(3)
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)
print((endtime - starttime).microseconds)