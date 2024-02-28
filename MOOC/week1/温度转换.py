Tempser = input("请输入带有温度的值")
if Tempser [-1] in ['f','F']:
    C = (eval(Tempser[0:-1])-32)/18
    print("转换后的温度是{:.2f}".format(C))
elif Tempser[-1] in ['C','c']:
    F = 1.8*eval(Tempser[0:-1])+32
    print("转换后的温度是{:.2f}".format(F))
else:
    print("输入错误")