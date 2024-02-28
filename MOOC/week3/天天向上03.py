dayup = 1
daydown = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-daydown)
    else:
        dayup = dayup*(1+daydown)
print("周内努力，周末休息的结果是{:.2f}".format(dayup))
