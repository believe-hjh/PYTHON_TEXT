height,weight = eval(input("请输入身高（m），体重的数值（kg）"))
BMI = weight/pow(height,2)
print("身体的BIM指数为{:.2f}".format(BMI))
who ,nat = "",""
if BMI<18.5:
    who,nat = "偏瘦","偏瘦"
elif 18.5<=BMI<24:
    who, nat = "正常", "正常"
elif 24<=BMI<25:
    who, nat = "正常", "偏胖"
elif 25<=BMI<28:
    who, nat = "偏胖", "偏胖"
elif 28<=BMI<30:
    who, nat = "肥胖", "偏胖"
elif BMI>=30:
    who, nat = "肥胖", "肥胖"
else:
    print("输入错误")
print("身体的BMI指数为{:.2f}，在国内{}，在国际{}".format(BMI,who,nat))