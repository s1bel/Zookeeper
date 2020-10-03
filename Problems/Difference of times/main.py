# put your python code here
hours_start = int(input())
minutes_start = int(input())
seconds_start = int(input())
hours_end = int(input())
minutes_end = int(input())
seconds_end = int(input())

seconds_start += hours_start * 60 ** 2 + minutes_start * 60
seconds_end += hours_end * 60 ** 2 + minutes_end * 60
print(abs(seconds_start - seconds_end))