# for x in range(5):
#     print(x)

# i = 1
# for i in range(1,101):
#     print(i)
#     for j in range(1,11):
#         print(j)
#     print(i)
# print(i)


# money = 10000
# for i in range(1,21):
#     import random
#     score = random.randint(1,10)
#
#     if score < 5:
#         print(f"员工{i}绩效分{score}，不满足，不发工资，下一位")
#         continue
#     if score <= 1000:
#         money -= 1000
#         print(f"员工{i}，满足条件发放工资1000rmb，公司余额：{money}")
#     else:
#         print(f"余额不足，当前余额：{money}")
#         break


# str1 = "xiayuzizhuo"
#
#
# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(f"字符串{data}的长度是{count}")
#
#
# my_len(str1)


# def say_hi():
#     print("Hello World")
#     return 0
#
# say_hi()


# def ADD(x,y):
#     sum = x + y
#     return print(f"{x}+{y}={sum}")
#
#
# str = ADD(1,2)
# print(str)
# a = input("Enter a number: ")
# b=input("Enter another number: ")
# def add(a,b):
#     d= a+b
#     def sub(d,b):
#         return d-b
# c=add(a,b)
# print(c)


# def main():
#     print("--------------主菜单--------------")
#     print(f"{name},您好，欢迎来到天地银行ATM！请选择你的操作：")
#     print("查询余额【输入‘1’】")
#     print("取款【输入‘2’】")
#     print("存款【输入‘3’】")
#     print("退出【输入‘0’】")
#     while True:
#         select = int(input())
#         if select < 0 or select > 3:
#             print("您输入的操作有误！")
#             continue
#         if select == 1:
#             query(True)
#             continue
#         if select == 2:
#             number = int(input("请输入您需要取走的金额！"))
#             get_money(number)
#             continue
#         if select == 3:
#             number = int(input("请输入您需要存进的金额！"))
#             saving(number)
#             continue
#         if select == 0:
#             print("欢迎下次再来！")
#             break
#
#
#
#
# import random
# money = random.randint(1,5000000)
# name = input("Enter your name: ")
#
#
#
#
#
#
# def query(show_header):
#     if show_header:
#         print("--------------查询余额--------------")
#     print(f"尊敬的{name}，您好！您的余额剩余【{money}】元")
#
#
# def saving(number):
#     global money
#     money += number
#     print("--------------存款--------------")
#     print(f"{name}，您好！您存款的{number}元，存款成功！")
#
#     query(False)
#
# def get_money(number):
#     global money
#     money -= number
#     print("--------------取款--------------")
#     print(f"{name}，您好！您取款的{number}元，取款成功！")
#
#     query(False)
#
#
# main()



# name_list = ['xiayu','xuanzun','meinux','aidnawh']
# print(name_list)

# my_list = [[1,2,3],[4,5]]
# print(my_list)


my_list = ["a", "b", "c"]
index = my_list.index("c")
print(index)

