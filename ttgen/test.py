


all_sections = ['Sect 1','Sect 2','Sect 3','Sect 4']
all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday"]
all_timing = ["9:30 - 10:30", "10:30 - 11:30", "11:30 - 12:30", "12:30 - 1:30","2:30 - 3:30", "3:30 - 4:30"]



# for sec in all_sections:

day_time_dic = {}
for day in all_days:
    time_dic = {}
    for time in all_timing:
        time_dic[time] = 5
    day_time_dic[day] = time_dic


print(day_time_dic)

