import time
import webbrowser

total_breaks = 3
break_count = 0
sleep_time = 10  # Set to 720 for two hour breaks

print("This program started on "+time.ctime())
while break_count < total_breaks:
    time.sleep(sleep_time)
    webbrowser.open("https://www.youtube.com/watch?v=djV11Xbc914")
    print("Break "+str(break_count + 1)+" started at "+time.ctime())
    break_count += 1

