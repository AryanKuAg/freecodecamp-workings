import random


def isInList(sublist, mylist):
    if len(sublist) > len(mylist):
        return False

    isthere = True
    for sub in sublist:
        isIn = False
        for index, l in enumerate(mylist):
            if sub in l:
                isIn = True
                mylist.pop(index)
                break

        if not isIn:
            isthere = False
    return isthere


class Hat:
    def __init__(self, **kwargs):
        self.number = kwargs
        temp = []
        for k, v in kwargs.items():
            for i in range(v):
                temp.append(k)

        self.contents = temp
        # print(self.contents)

    def draw(self, ball_to_draw):  # removes balls randomly from contents and return as a list of strings
        if ball_to_draw > len(self.contents):
            return self.contents
        temp_list = self.contents
        random.shuffle(temp_list)
        return temp_list[:ball_to_draw]

        # Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

        # This function will return the probability


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    no_of_true = 0
    for exp in range(num_experiments):  # number of experiments
        h = hat

        # get random balls #problem: no element there
        balls = h.draw(num_balls_drawn)
        expected_balls_list = []  # want these balls in balls
        for k, v in expected_balls.items():
            for i in range(v):
                expected_balls_list.append(k)
        isContain = isInList(expected_balls_list, balls)
        if isContain:
            no_of_true += 1

    return no_of_true / num_experiments
