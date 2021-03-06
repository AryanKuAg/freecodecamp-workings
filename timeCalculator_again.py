dic_day = {"sunday": 0, "monday": 1, "tuesday": 2,
           "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6}


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
    day_later_cal = calHour // 24
    day_later_val = ''
    if day_later_cal == 0:
        pass
    elif day_later_cal == 1:
        day_later_val = "(next day)"
    elif day_later_cal > 1:
        day_later_val = f"({day_later_cal} days later)"

    ###########################################
    if day != "":
        daynum = dic_day[day]
        daynum += day_later_cal % 7
        for key, value in dic_day.items():
            if value == daynum:
                day = key.capitalize()

    ############################################
    part1 = (str(calHour) if calHour < 12 else str(calHour % 12)) + ":" + \
        str(calMinute).zfill(2) + " " + ("AM" if calHour % 24 < 12 else "PM")
    ##############IF#################
    part1 = part1[:1].replace("0", "12") + part1[1:]
    ################
    part2 = day
    part3 = day_later_val
    if part2 != "":
        print(part1+',', part2, part3)
    elif part2 == "":
        print(part1, part3)
    else:
        print(part1, part2, part3)

    # (next day) if result is next day
    # (n days later) if result is more than 1 day
    # if day exist then show it


# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)
