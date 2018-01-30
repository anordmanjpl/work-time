import datetime

stHr = int(input('Input Start Hour: '))
stMin = int(input('Input Start Minute: '))
workDuration = int(input('Input Required # of Hours: '))
lunchTime = int(input('Time taken for Lunch (in minutes): '))

endTime = datetime.timedelta(hours=stHr+workDuration, minutes=stMin+lunchTime)
print('End Time:' + str(endTime))
