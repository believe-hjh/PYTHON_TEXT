import os

filename = r'C:\Users\13350\Desktop\士兵突击\1080P'
list_path = os.listdir(filename)

count = 1
for index in list_path:
    # 替换文件名中的空格
    new_index = index.replace(' ', '_')
    path = os.path.join(filename, new_index)
    new_path = os.path.join(filename, f'第{count}集_{new_index}')
    print(new_path)
    try:
        os.rename(path, new_path)
        count += 1
    except Exception as e:
        print(f"重命名失败： {e}")

print('修改完成')
