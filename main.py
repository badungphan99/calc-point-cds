import glob
import os
from Team import Team

path = "/home/dungpb/testresult"

all_team = []

if __name__ == "__main__":
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                # files.append(os.path.join(r, file))
                team_name = file[0:-4]
                check_point = []
                with open(os.path.join(r, file)) as data:
                    check_point = data.readlines()
                team = Team(team_name, float(check_point[0]), float(check_point[1]), float(check_point[2]), float(check_point[3]), float(check_point[4]))
                all_team.append(team)

    # calc point - check point
    for team in all_team:
        team.calc_check_point()
        team.calc_point()

    # calc bonus point
    # check point 1
    all_team.sort(key=lambda x: x.check_point_1, reverse=False)
    for i in range(len(all_team)):
        if(i < 5):
            all_team[i].bonus_point(5-i)

    # check point 2
    all_team.sort(key=lambda x: x.check_point_2, reverse=False)
    for i in range(len(all_team)):
        if (i < 5):
            all_team[i].bonus_point(5 - i)

    # check point 3
    all_team.sort(key=lambda x: x.check_point_3, reverse=False)
    for i in range(len(all_team)):
        if (i < 5):
            all_team[i].bonus_point(5 - i)

    # check point 4
    all_team.sort(key=lambda x: x.check_point_4, reverse=False)
    for i in range(len(all_team)):
        if (i < 5):
            all_team[i].bonus_point(5 - i)

    # check point 5
    all_team.sort(key=lambda x: x.check_point_5, reverse=False)
    for i in range(len(all_team)):
        if (i < 5):
            all_team[i].bonus_point(5 - i)

    # rank
    all_team.sort(key=lambda x: x.total_point, reverse=True)

    # save result
    fw = open(path + "/result.csv", "a")
    fw.write("team_name,cp_1,cp_2,cp_3,cp_4,cp_5,total\n")
    fw.close()
    for result in all_team:
        fw = open(path+"/result.csv", "a")
        fw.write(result.get_info())
        fw.close()