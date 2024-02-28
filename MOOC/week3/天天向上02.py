dayfoctor = 0.005
up = pow (1+dayfoctor,365)
down = pow (1-dayfoctor,365)
print("每天进步百分之5向上{:.2f},向下{:.2f}".format(up,down))