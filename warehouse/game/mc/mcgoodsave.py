#把D:\mc\minecraft\.minecraft\versions\1.19.2-Fabric 0.15.11\saves\tast 文件夹拷贝到D:\mc\saves 文件夹下
from datetime import datetime
import shutil
import os
# 源文件夹路径
source_folder = r"D:\mc\minecraft\.minecraft\versions\1.19.2-Fabric 0.15.11\saves"

# 获取当前日期
current_date = datetime.now().date()

# 目标文件夹路径
destination_folder = r"D:\mc\saves\%s" % current_date

# 使用shutil的copytree函数进行复制
try:
    # 尝试复制源文件夹到目标文件夹
    # 使用shutil的copytree函数进行复制
    shutil.copytree(source_folder, destination_folder)
    print("文件夹复制成功！")
except FileNotFoundError:
    # 如果源文件夹不存在，给出提示
    print("源文件夹不存在，请检查路径是否正确。")
except FileExistsError:
    # 如果目标文件夹已存在，删除目标文件夹后重新尝试复制
    folder_path = r"D:\mc\saves\%s" % current_date
    shutil.rmtree(folder_path)
    print(f"{folder_path} 已成功删除。")
    shutil.copytree(source_folder, destination_folder)
    print("文件夹复制成功！")
except OSError as e:
    # 处理其他操作系统错误，如权限问题
    print(f"Error: {e.strerror}")
    print("目标文件夹已存在，若需覆盖请先删除或重命名目标文件夹。")
except Exception as e:
    # 捕获并打印复制过程中发生的任何其他异常
    print(f"复制过程中发生错误：{e}")
    
try:
    shutil.rmtree(r"D:\mc\saves\%s\.git" % current_date)
    print("删除.git文件夹成功！")
except FileNotFoundError:
    print("没有找到.git文件夹。")
except OSError as e:
    print(f"Error: {e.strerror}")
    print("目标文件夹已存在，若需覆盖请先删除或重命名目标文件夹。")

#在 "D:\mc\saves\ 下创造名为'备注'的txt文件
with open(r"D:\mc\saves\%s\备注.txt" % current_date, "w") as file:
    file.write(input("请输入备注："))
    print('备注已保存！')

#清空D:\mc\minecraft\PCL\hints.txt 文件
# 打开文件准备读写，如果文件不存在则创建
with open(r"D:\mc\minecraft\PCL\hints.txt", "w+") as file:
    # 清空文件内容
    file.seek(0)          # 移动文件指针到开头
    file.truncate()       # 清空文件内容
    
    # 写入新的内容
    #判断存档保存状况
    #查看是否有今日存档
    if str(current_date) in os.listdir(r"D:\mc\saves"):
        save_status = True
    else:
        save_status = False
    #print("今日存档已保存！")
    file.write("存档保存状况:%s" % str(save_status))
#删除 "D:\mc\saves\%s" % current_date 下的.git 文件夹
