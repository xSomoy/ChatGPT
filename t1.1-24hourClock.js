function displayClock() {
  // Get the current time
  var currentTime = new Date();
  
  // Extract the hour, minute, and second from the current time
  var hour = currentTime.getHours();
  var minute = currentTime.getMinutes();
  var second = currentTime.getSeconds();
  
  // Print the current time in HH:MM:SS format
  console.log(`${hour.toString().padStart(2, '0')}:${minute.toString().padStart(2, '0')}:${second.toString().padStart(2, '0')}`);
  
  // Call the function again after 1 second
  setTimeout(displayClock, 1000);
}

// Start the clock
displayClock();