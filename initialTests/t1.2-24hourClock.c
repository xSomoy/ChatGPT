#include <stdio.h>
#include <time.h>

int main() {
  // Run the clock indefinitely
  while (1) {
    // Get the current time
    time_t currentTime = time(NULL);
    struct tm *timeStruct = localtime(&currentTime);
    
    // Extract the hour, minute, and second from the time structure
    int hour = timeStruct->tm_hour;
    int minute = timeStruct->tm_min;
    int second = timeStruct->tm_sec;
    
    // Print the current time in HH:MM:SS format
    printf("%02d:%02d:%02d\n", hour, minute, second);
    
    // Sleep for 1 second before updating the time again
    sleep(1);
  }
  
  return 0;
}
