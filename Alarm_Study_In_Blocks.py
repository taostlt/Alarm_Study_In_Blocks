# Jeff Bromen

"""Simple Python script to set an alarm for a specific time.
   When the alarm goes off, a random youtube video will be opened.
   The possible youtube video URLs are taken from "youtube_alarm_videos.txt"
"""

import datetime
import os
import time
import random
import webbrowser


val = 'Geeks'
# print(f'{val}')

print('The program is beginning')
# print(f'Hello, {name}. You are {age}.')
# If video URL file does not exist, create one
if not os.path.isfile("youtube_alarm_videos.txt"):
    print('Creating "youtube_alarm_videos.txt"...')
    with open("youtube_alarm_videos.txt", "w") as alarm_file:
        alarm_file.write("https://www.youtube.com/watch?v=anM6uIZvx74")


def check_alarm_input(alarm_time):
    """Checks to see if the user has entered in a valid alarm time"""
    if len(alarm_time) == 1:  # [Hour] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2:  # [Hour:Minute] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
           alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3:  # [Hour:Minute:Second] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
           alarm_time[1] < 60 and alarm_time[1] >= 0 and \
           alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True
    return False


# define time in seconds
seconds_hms = [3600, 60, 1]  # Number of seconds in an Hour, Minute, and Second

# Get the current time of day in seconds
now = datetime.datetime.now()
current_time_seconds = sum([a * b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])
print('The current hour time is:')

# get alarm hour
alarm_hour = now.hour

# set alarm minute to be 55
print(alarm_hour)

if 0 <= now.minute <= 24:
    print('The time is over 0 but less then 30 minutes')
    alarm_minute = 24
elif 25 <= now.minute <= 29:
    print('Mid break')
    alarm_minute = 30
elif 30 <= now.minute <= 54:
    print('hi')
    alarm_minute = 54
elif 55 <= now.minute <= 59:
    print('2nd break on the hour')
    alarm_minute = 0

# set alarm time
alarm_time = [alarm_hour, alarm_minute, 00]
print('my alarm1 time', alarm_time)

alarm_time2 = [alarm_hour, alarm_minute + 4, 00]
print('my alarm2 time:', alarm_time2)


# Get user input for the alarm time

# print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")
# while True:
#     # alarm_input = input(">> ")
#     try:
#         # alarm_time = [int(n) for n in alarm_input.split(":")]
#         if check_alarm_input(alarm_time):
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print("ERROR: Enter time in HH:MM or HH:MM:SS format")

# Convert the alarm time from [H:M] or [H:M:S] to seconds
# print(f'Their alarm time: {alarm_time}')
alarm_seconds = sum([a * b for a, b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

# Calculate the number of seconds until alarm goes off
time_diff_seconds = alarm_seconds - current_time_seconds

# If time difference is negative, set alarm for next day
if time_diff_seconds < 0:
    time_diff_seconds += 86400  # number of seconds in a day

# Display the amount of time until the alarm goes off

print("Alarm1 set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

# Sleep until the alarm goes off
time.sleep(time_diff_seconds)

# Time for the alarm to go off
print("Wake Up!")

# Load list of possible video URLs
with open("youtube_alarm_videos.txt", "r") as alarm_file:
    videos = alarm_file.readlines()

# Open a random video from the list
webbrowser.open(random.choice(videos))

print('ALARM 2 WILL ACTIVATE NEXT!!!!!', alarm_time2)

alarm_seconds2 = sum([a * b for a, b in zip(seconds_hms[:len(alarm_time2)], alarm_time2)])

# Calculate the number of seconds until alarm goes off
time_diff_seconds2 = alarm_seconds2 - current_time_seconds

# If time difference is negative, set alarm for next day
# if time_diff_seconds2 < 0:
#     time_diff_seconds2 += 86400  # number of seconds in a day

# Display the amount of time until the alarm goes off

print("Alarm2 set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds2))

# Sleep until the alarm goes off
time.sleep(time_diff_seconds2)

# Time for the alarm to go off
print("Wake Up2!")

# Load list of possible video URLs
with open("youtube_alarm_videos.txt", "r") as alarm_file:
    videos = alarm_file.readlines()

# Open a random video from the list
webbrowser.open(random.choice(videos))
