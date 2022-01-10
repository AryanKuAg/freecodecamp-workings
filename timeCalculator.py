from typing import final
# Pro Tip: Calculation is on 24 not am or pm


def week(i):
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return switcher.get(i, "Invalid day of week")


def weeknum(i):
    switcher = {
        'sunday': 0,
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6
    }
    return switcher.get(str(i).lower(), "Invalid day of week")


def add_time(time, duration, day="0"):
    isAm = True if "AM" in time else False
    timeHour = time.split(":")[0]
    timeMinute = time.split(":")[1][:2]
    durationHour = duration.split(":")[0]
    durationMinute = duration.split(":")[1][:2]
    # time
    finaltimeHour = (int(timeHour) + int(durationHour)) % 12  # perfect
    finaltimeMinute = (int(timeMinute) + int(durationMinute)) % 60  # perfect
    print(finaltimeHour)
    print(finaltimeMinute)
    amorpm = (int(timeHour) + int(durationHour))//12

    if amorpm % 2 == 0:
        if isAm:
            amorpm = "AM"
        else:
            amorpm = "PM"
    else:
        if isAm:
            amorpm = "PM"
        else:
            amorpm = "AM"

    part1 = str(finaltimeHour) + ":" + \
        str(finaltimeMinute).zfill(2) + " " + amorpm

    # duration

    if isAm:  # for am
        howfar = (int(timeHour) + int(durationHour)) // 24
        print(howfar)
        just = (weeknum(day) + howfar) // 7
        finalday = week(just)

    else:  # for pm
        howfar = (12 + int(timeHour) + int(durationHour)) // 24
        print(howfar)
        just = (weeknum(day) + howfar) // 7
        finalday = week(just)

    #######################################
    if day != '0':
        if just > 1:
            print(part1, finalday, "(" + str(just) + " days later)")
        elif just == 1:
            print(part1, finalday, "(next day)")
        elif just == 0:
            print(part1, finalday)
    elif day == '0':
        if just > 1:
            print(part1, "(" + str(just) + " days later)")
        elif just == 1:
            print(part1,  "(next day)")
        elif just == 0:
            print(part1)


add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM
