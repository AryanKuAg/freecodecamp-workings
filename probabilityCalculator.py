import random
import copy


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
        # ball_to_draw is fixed
        # self.contents will vary
        #

        take_out = []
        total_num_draw = ball_to_draw
        for i in range(total_num_draw):

            if ball_to_draw > len(self.contents):
                all_ball_copy = self.contents
                self.contents = []
                return all_ball_copy
            r = random.randrange(0, ball_to_draw, 1)
            copy = self.contents[r]
            self.contents.pop(r)
            ball_to_draw -= 1
            take_out.append(copy)

        return take_out

        # Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)


# This function will return the probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
