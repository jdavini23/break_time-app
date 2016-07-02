import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
while(break_count < total_breaks):
    time.sleep(10) # Change this to the time you want to take breaks at. In seconds
    webbrowser.open("https://www.youtube.com/watch?v=6-a7t7rJycQ") # You can change this URL to any song
    break_count = break_count + 1
