weekstr = "星期一星期二星期三星期四星期五星期六星期日"
a = eval(input("请输入星期1~7数字"))
pos = (a-1)*3
b = weekstr[pos:pos+3]
print(b)