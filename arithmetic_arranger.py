def arithmetic_arranger(mylist, result=False):
    # Limit exceeding error
    if len(mylist) > 5:
        return "Error: Too many problems."

    # Invalid operator Error
    for i in mylist:
        if '*' in i or '/' in i:
            return "Error: Operator must be '+' or '-'."

        if '+' in i:
            temp = i.split('+')
            for add in temp:
                if len(add) > 4:
                    return "Error: Numbers cannot be more than four digits."
                try:
                    int(add)
                except:
                    return "Error: Numbers must only contain digits."

        if '-' in i:
            temp = i.split('-')
            for sub in temp:
                if len(sub) > 4:
                    return "Error: Numbers cannot be more than four digits."
                try:
                    int(sub)
                except:
                    return "Error: Numbers must only contain digits."

    # Working on the perfect data maybe without error ^_^
    for single in mylist:
        pass
