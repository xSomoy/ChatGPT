import java.util.Calendar;
import java.util.TimeZone;

public class Clock {
  public static void main(String[] args) {
    // Run the clock indefinitely
    while (true) {
      // Get the current time
      Calendar calendar = Calendar.getInstance(TimeZone.getDefault());
      
      // Extract the hour, minute, and second from the calendar
      int hour = calendar.get(Calendar.HOUR_OF_DAY);
      int minute = calendar.get(Calendar.MINUTE);
      int second = calendar.get(Calendar.SECOND);
      
      // Print the current time in HH:MM:SS format
      System.out.printf("%02d:%02d:%02d\n", hour, minute, second);
      
      // Sleep for 1 second before updating the time again
      try {
        Thread.sleep(1000);
      } catch (InterruptedException e) {
        // Do nothing
      }
    }
  }
}
