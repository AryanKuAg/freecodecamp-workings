def add_time(time, duration, day=""):
    day = day.lower()
    # raw to useful
    try:
        hourtime = int(time.split(":")[0])
        minutetime = int(time.split(":")[1][:2])
        hourduration = int(duration.split(":")[0])
        minuteduration = int(duration.split(":")[1][:2])
    except:
        print("I really hate errors but I shouldn't..O_O")

    ###############################
    # print(hourtime, minutetime, hourduration, minuteduration)
    calHour = (hourtime + hourduration) + \
        (minutetime + minuteduration)//60  # 24
    calHour += 12 if "PM" in time else 0  # 24
    calMinute = (minutetime + minuteduration) % 60  # 24
    # print(calHour, calMinute)
    # above calculation is based on 24-hour model
    ####################################################

    # (next day) if result is next day
    # (n days later) if result is more than 1 day
    # if day exist then show it


add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday
