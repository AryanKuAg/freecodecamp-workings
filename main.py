def arithmetic_arranger(mylist, show=False):

    # Limit exceeding error
    if len(mylist) > 5:
        return "Error: Too many problems."

    # Invalid operator Error
    for i in mylist:
        if '*' in i or '/' in i:
            return "Error: Operator must be '+' or '-'."

        temp = i.split('+') if "+" in i else i.split("-")
        for add in temp:
            add = add.strip()
            if len(add) > 4:
                return "Error: Numbers cannot be more than four digits."
            try:
                int(add)
            except:
                return "Error: Numbers must only contain digits."

    # Working on the perfect data maybe without error ^_^
    firstLine = ''
    secondLine = ''
    dashLine = ''
    solLine = ''

    for single in mylist:

        data = single.split("+") if "+" in single else single.split("-")
        dataMax = max(int(data[0]), int(data[1]))
        maxGap = len(str(dataMax))
        firstVal = int(data[0])
        secVal = int(data[1])
        firstLine += "  "+" " * (maxGap -
                                 len(str(data[0]).strip())) + str(data[0]).strip() + "    "

        tempLine = "+ "+" " * (maxGap -
                               len(str(data[1]).strip())) + str(data[1]).strip() + "    " if "+" in single else "- "+" " * (maxGap - len(str(data[1]).strip())) + str(data[1]).strip() + "    "

        secondLine += tempLine
        dashLine += ("-" * (2+len(str(dataMax)))) + "    "
        ans = firstVal + secVal if "+" in single else firstVal - secVal

        solLine += (" " * (len(tempLine) - len(str(ans)) - 4)) + \
            str(ans)+"    "

    print(firstLine)
    print(secondLine)
    print(dashLine)
    if show:
        print(solLine)


arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
