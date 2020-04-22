# # 49. Python 交换两个变量的值
# # **答：**在 Python 中交换两个对象的值通过下面的方式即可
# a = 1
# b = 2
# a, b = b, a
# print(a, b)

# #50. 在读文件操作的时候会使用 read、readline 或者 readlines，简述它们各自的作用
# 答：.
# read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中。
# 如果希望一行一行的输出那么就可以使用 readline()，该方法会把文件的内容加载到内存，所以对于对于大文件的读取操作来说非常的消耗内存资源
# readlines 方法，将文件的句柄生成一个生产器，然后去读就可以了。

# 自定义时间序列化
import json
from datetime import datetime, date

# # JSONEncoder 不知道怎么去把这个数据转换成 json 字符串的时候
# # ，它就会去调 default()函数,所以都是重写这个函数来处理它本身不支持的数据类型，
# # default()函数默\#认是直接抛异常的。
# class DateToJson(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.strftime('%Y-%m-%d %H：%M：%S')
#         elif isinstance(obj, date):
#             return obj.strftime('%Y-%m-%d')
#         else:
#             return json.JSONEncoder.default(self, obj)
#
# d = {'name':'cxa', 'data':  datetime.now()}
# print(json.dumps(d, cls=DateToJson))

# #52. json 序列化时，默认遇到中文会转换成 unicode，如果想要保留中文怎么办？
# #**答：**可以通过 json.dumps 的 ensure_ascii 参数解决，代码示例如下：
# import json
# a = json.dumps({"name": "张三"},ensure_ascii=False)
# b = json.dumps({"name": "张三"})
# print(a)
# print(b)

# #53. 有两个磁盘文件 A 和 B，各存放一行字母，要求把这两个文件中的信息合并(按字母顺序排列)，输出到一个新文件 C 中。
# #文件 A.txt 内容为 ASDCF
# #文件 B.txt 内容为 EFGGTG
# with open("A.txt","r") as f1:
#     f1_txt = f1.read()
#     print(f1_txt)
# with open("B.txt","r") as f2:
#     f2_txt = f2.read()
#     print(f2_txt)
# f3_txt = f1_txt + f2_txt
# f3_list = sorted(f3_txt)
# print(f3_txt)
# with open("C.txt","a+") as f3:
#     f3.write(" ".join(f3_list))
# #疑问   read  和  readline

# #54. 如果当前的日期为 20190530，要求写一个函数输出 N 天后的日期，(比如 N 为 2，则输出 20190601)。
# import datetime
#
# def datetime_operate(n: int):
#     now = datetime.datetime.now()  #获取当前时间
#     _now_date = now + datetime.timedelta(days=n)
#     now_date = _now_date.strftime("%Y:%m:%d")
#     return now_date
#
# print(datetime_operate(5))

# #55. 写一个函数，接收整数参数 n，返回一个函数，函数的功能是把函数的参数和 n 相乘并把结果返回。
# #**答：**这个题目考查了闭包的使用代码示例如下，返回函数之类型是函数对象。
# def  mul_operate(num: int):
#     def g(val: int):
#         return val *num
#     return g
# m = mul_operate(10)
# print(m(99))

# # 57. 一行代码输出 1-100 之间的所有偶数。
# # **答：**可以通过列表生成式，然后使用与操作如果如 1 与之后结果为 0 则表明为偶数，等于 1 则为奇数。
# #方法1
# print([i for i in range(1, 101) if i & 0x01 == 0])
# #方法2
# print(list(range(2, 101, 2)))

# # 59. Python 字典和 json 字符串相互转化方法
# # 答:在 Python 中使用 dumps 方法 将 dict 对象转为 Json 对象，使用 loads 方法可以将 Json 对象转为 dict 对象。
# dict1 = {'a': 123, 'b': "456", 'c': "liming"}
# json_str = json.dumps(dict1)
# dict2 = json.loads(json_str)
# print(json_str)   #json   双引号
# print(dict2)      #字符串 单引号
# # import json
# # dic = {'a':123, 'b':"456", 'c':"liming"}
# # dic_str = json.loads(str(dic).replace("'","\\""))
# # print(dic_str)
# #Json 的标准格式是不支持单引号型字符串的

# #60. 请写一个 Python 逻辑，计算一个文件中的大写字母数量
# with open("A.txt") as fs:
#     conut = 0
#     for i in fs.read():
#         if i.isupper():
#             conut+=1
#
# print(conut)
#
# 62.说一说Redis的基本类型
# 答: Redis 支持五种数据类型：
# string（字符串） 、
# hash（哈希）、
# list（列表） 、
# set（集合） 及
# zset(sorted set： 有序集合)。


# conn = pymysql.connect(host='localhost',port=3306, user='root',passwd='1234', db='user', charset='utf8mb4') #声明mysql连接对象
# cursor=conn.cursor(cursor=pymysql.cursors.DictCursor) #查询结果以字典的形式
# cursor.execute(sql语句字符串) #执行sql语句
# conn.close() #关闭链接




































