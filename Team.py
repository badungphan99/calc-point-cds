class Team:
    def __init__(self, team_name, check_point_1, check_point_2, check_point_3, check_point_4, check_point_5):
        self.team_name = team_name
        self.check_point_1 = check_point_1
        self.check_point_2 = check_point_2
        self.check_point_3 = check_point_3
        self.check_point_4 = check_point_4
        self.check_point_5 = check_point_5
        self.total_point = 0

    def calc_check_point(self):
        # check point 2
        if(self.check_point_2 - self.check_point_1 < 0):
            self.check_point_2 = 0
        else:
            self.check_point_2 -= self.check_point_1

        # check point 3
        if (self.check_point_3 - self.check_point_2 < 0):
            self.check_point_3 = 0
        else:
            self.check_point_3 -= self.check_point_2

        # check point 4
        if (self.check_point_4 - self.check_point_3 < 0):
            self.check_point_4 = 0
        else:
            self.check_point_4 -= self.check_point_3

        # check point 5
        if (self.check_point_5 - self.check_point_4 < 0):
            self.check_point_5 = 0
        else:
            self.check_point_5 -= self.check_point_4

    def calc_point(self):
        # check point 1
        if(self.check_point_1 > 0):
            self.total_point += 10
        # check point 2
        if (self.check_point_2 > 0):
            self.total_point += 10
        # check point 3
        if (self.check_point_3 > 0):
            self.total_point += 10
        # check point 4
        if (self.check_point_4 > 0):
            self.total_point += 10
        # check point 5
        if (self.check_point_5 > 0):
            self.total_point += 10

    def bonus_point(self, point_bonus):
        self.total_point += point_bonus

    def get_info(self):
        info = self.team_name + "," + str(self.check_point_1) + "," + str(self.check_point_2) + "," + \
               str(self.check_point_3) + "," + str(self.check_point_4) + "," + str(self.check_point_5) + "," + str(self.total_point) + "\n"
        return info
