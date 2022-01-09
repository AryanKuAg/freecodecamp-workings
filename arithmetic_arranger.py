def arithmetic_arranger(mylist, show=False):

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
                add = add.strip()
                if len(add) > 4:
                    return "Error: Numbers cannot be more than four digits."
                try:
                    int(add)
                except:
                    return "Error: Numbers must only contain digits."

        if '-' in i:
            temp = i.split('-')
            for sub in temp:
                sub = sub.strip()
                if len(sub) > 4:
                    return "Error: Numbers cannot be more than four digits."
                try:
                    int(sub)
                except:
                    return "Error: Numbers must only contain digits."

    # Working on the perfect data maybe without error ^_^
    firstLine = ''
    secondLine = ''
    dashLine = ''
    solLine = ''

    for single in mylist:
        if "+" in single:
            data = single.split("+")
            dataMax = max(int(data[0]), int(data[1]))
            firstVal = int(data[0])
            secVal = int(data[1])
            firstLine += " " * (6 -
                                len(str(data[0]).strip())) + str(data[0]).strip() + "    "

            secondLine += "+"+" " * (5 -
                                     len(str(data[1]).strip())) + str(data[1]).strip() + "    "
            dashLine += ("-" * (2+len(str(dataMax)))) + "    "
            ans = firstVal + secVal
            solLine += (" " * (6 - len(str(ans))))+str(ans)+"    "

        elif "-" in single:
            data = single.split("-")
            dataMax = max(int(data[0]), int(data[1]))
            firstVal = int(data[0])
            secVal = int(data[1])
            firstLine += " " * (6 -
                                len(str(data[0]).strip())) + str(data[0]).strip() + "    "

            secondLine += "-"+" " * (5 -
                                     len(str(data[1]).strip())) + str(data[1]).strip() + "    "
            dashLine += ("-" * (2+len(str(dataMax)))) + "    "
            ans = firstVal + secVal
            solLine += (" " * (6 - len(str(ans))))+str(ans)+"    "

    print(firstLine)
    print(secondLine)
    print(dashLine)
    if show:
        print(solLine)


no = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
print(no)
