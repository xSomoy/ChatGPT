; Declare a global variable to store the current time
section .bss
time: resd 1

; Declare a function to display the clock
section .text
global _start
_start:
  mov dword [time], 0  ; Initialize the time to 0

display_clock:
  ; Extract the hour, minute, and second from the time variable
  mov eax, [time]
  mov edx, 3600  ; Number of seconds in an hour
  div edx
  mov ebx, eax  ; ebx = hour
  mov eax, [time]
  mov edx, 60  ; Number of seconds in a minute
  div edx
  mov ecx, eax  ; ecx = minute
  mov eax, [time]
  mov edx, 60
  div edx
  mov edx, eax  ; edx = second

  ; Print the current time in HH:MM:SS format
  push ecx
  push ebx
  push edx
  push message
  call printf
  add esp, 16

  ; Increment the time by 1 second
  inc dword [time]

  ; Call the function again after 1 second
  push 1000
  call sleep
  add esp, 4
  jmp display_clock

; Declare a string to use with printf
section .data
message: db "%02d:%02d:%02d", 10, 0
