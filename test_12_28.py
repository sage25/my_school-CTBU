import math
import datetime
import re

# def start(obj):
#     obj.speak()

# class Alimal(object):
#     def speak(self):
#         print("动物叫，但不知道叫什么！")


# class Dog(Alimal):
#     def speak(self):
#         print("小狗：旺旺叫...")

# class Cat(Alimal):
#     def speak(self):
#         print("小猫：喵喵叫...")

# class Car(object):
#     def speak(self):
#         print("小汽车：嘀嘀叫...")

# start(Dog())
# start(Cat())
# start(Car())


#################################################
# i = input('请输入数字')
# n = 8888
# try:
#     result = n / int(i)
#     print(result)
#     print('{0}除以{1}等于{2}'.format(n, i ,result))
# except (ValueError,ZeroDivisionError) as e:
#     print("输入的是无效的数字,异常:{}".format(e))
# finally:
#     print("资源释放...")


#################################################
# print(math.ceil(2.4))
# print(math.floor(2.4))
# print(math.pow(4,2))
# print(math.sqrt(3.6))
# print(math.log(16,4))
# print(math.degrees(math.pi))
# print(math.sin(math.pi/6))
# print(math.radians(57.295795))


#################################################
# d = datetime.datetime(2020,12,12)
# print(d)
# print(datetime.datetime.today())
# print(datetime.datetime.fromtimestamp(999999999))


#################################################
# p = r'\w+@zhijieketang\.com'
# email1 = 'rtony_guan558@zhijieketang.com'
# m = re.match(p, email1)
# print(type(m))
# print(m)
# email2 = 'tony_guan588@163.com'
# m = re.match(p,email2)
# print(m)

# p = r'\w+@zhijieketang\.com'
# text = "Tony's email is tony_guan588@zhijieketang.com."
# m = re.search(p, text)
# print(m)
# text = "Tony's email is tony_guan@163.com."
# m = re.search(p, text)
# print(m)

# p = r'Java|java|JAVA'
# text = 'I like Java and java and JAVA.'
# match_list = re.findall(p,text)
# print(match_list)

# p = r'\d+'
# text = 'AB12CD34EF'
# repace_text = re.sub(p, '--',text, count=1)
# print(repace_text)f

# p = r'\d+'
# text = 'AB12CD34EF'
# clist = re.split(p, text, maxsplit=1)
# print(clist)