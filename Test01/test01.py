# input : create a 24h clock in python

import time

while True:
  # Get the current time
  current_time = time.localtime()
  
  # Extract the hour, minute, and second from the current time
  hour = current_time.tm_hour
  minute = current_time.tm_min
  second = current_time.tm_sec
  
  # Print the current time in HH:MM:SS format
  print(f"{hour:02d}:{minute:02d}:{second:02d}")
  
  # Sleep for 1 second before updating the time again
  time.sleep(1)
