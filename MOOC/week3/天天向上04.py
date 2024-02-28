def dayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfacoor = 0.01
while dayUp(dayfacoor)<37.78:
    dayfacoor += 0.01
print("工作日的参数是{:.3f}".format(dayfacoor))
