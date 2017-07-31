def count_days(dayNum):
    days=["Monday","Tuesday","Wednesday","Thursday",
          "Friday","Saturday","Sunday"]

    for i in range(dayNum):
        if i < len(days):
            yield days[i]


tillDay_2 = lambda : count_days(2)
tillDay_4 = lambda : count_days(4)
print("Counting till day 4.....")
for day in tillDay_4():
    print(day,end=" ")


