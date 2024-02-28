# 注册登录的Python代码
# 创建一个数据类以存储用户信息
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
# 创建一个注册用户函数
def register_user(user):
    # 创建一个空字典，用于存储用户信息
    user_info = {}
    # 获取用户输入的用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")
    # 将用户名和密码添加到字典中
    user_info["username"] = username
    user_info["password"] = password
    # 判断字典中是否有用户名和密码
    if "username" in user_info and "password" in user_info:
        # 打印欢迎信息
        print("欢迎，" + username + "！")
        # 返回用户信息
        return user_info
    else:
        # 输出错误信息
        print("用户名或密码错误，请重新输入！")
        # 返回None
        return None
# 登录函数
def login(user):
    # 创建一个空字典，用于存储用户信息
    user_info = {}
    # 获取用户输入的用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")
    # 判断字典中是否有用户名和密码
    if "username" in user_info and "password" in user_info:
        # 检查输入的用户名和密码是否正确
        if user_info["username"] == password:
            # 打印欢迎信息
            print("欢迎，" + username + "！")
            # 返回用户信息
            return user_info
        else:
            # 输出错误信息
            print("用户名或密码错误，请重新输入！")
            # 返回None
            return None
    else:
        # 输出错误信息
        print("用户名或密码错误，请重新输入！")
        # 返回None
        return None
# 主程序
if __name__ == "__main__":
    # 创建一个注册用户实例
    user = User("user1", "password1")
    # 调用注册用户函数
    user_info = register_user(user)
    # 判断注册用户函数的返回值
    if user_info:
        print("注册成功！")
    else:
        print("注册失败！")
    # 创建一个登录实例
    user = User("user2", "password2")
    # 调用登录函数
    is_logined = login(user)
    # 判断登录函数的返回值
    if is_logined:
        print("登录成功！")
    else:
        print("登录失败！")