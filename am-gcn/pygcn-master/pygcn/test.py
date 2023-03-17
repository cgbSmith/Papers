# 1引入模块
import argparse

# 2建立解析对象
parser = argparse.ArgumentParser()

# 3增加属性：在命令行中，该py文件希望用户能给他一个参数，最终将之转化为：args.square

parser.add_argument("square", help="To sqaure the number given", type=int, action= square==1)

# 4属性给与args实例：add_argument 返回到 args 子类实例
args = parser.parse_args()
print(args.square ** 2)
