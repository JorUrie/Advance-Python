import time
current_time = time.time()
print(current_time)
# To know the current time
epoch_time = 1613004173.957986
local_time = time.ctime(epoch_time)
print("The local time is:", local_time)