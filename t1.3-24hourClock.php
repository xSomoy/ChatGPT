<?php

// Function to display the clock
function displayClock() {
  // Get the current time
  $currentTime = time();
  $timeStruct = localtime($currentTime, true);
  
  // Extract the hour, minute, and second from the time structure
  $hour = $timeStruct['tm_hour'];
  $minute = $timeStruct['tm_min'];
  $second = $timeStruct['tm_sec'];
  
  // Print the current time in HH:MM:SS format
  echo sprintf("%02d:%02d:%02d\n", $hour, $minute, $second);
  
  // Call the function again after 1 second
  flush();
  usleep(1000000);
  displayClock();
}

// Start the clock
displayClock();
