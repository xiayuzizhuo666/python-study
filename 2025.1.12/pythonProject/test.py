# print("登录界面")
# name = input("用户名：")
# password = input("密码：")
# Real_password = "123456"
# if password == Real_password: print(f"尊贵的{name}，欢迎来到python！")


# age = 18
# if age < 18:
#     print("好好学习")
# if age >= 18:
#     print("进入大学")
# print(f"年龄是{age}")
#
# height = float(input("Enter your height  : "))
# if height >= 120:
#     print("你身高超过120cm，你需要买票")
# else:
#     print("你不需要买票")


# height = float(input("Enter your height in m: "))
# vip_level = int(input("Enter your YIP in (1 - 5): "))
# if height <= 120.0:
#     print("You are free")
# elif vip_level > 3:
#     print("You are free")
# else:
#     print("You are not free")


# import random
#
# num = random.randint(1, 10)
# Num = int(input("猜一猜数字："))
# if num != Num:
#     if num > Num:
#         print("你猜小了了")
#     elif num < Num:
#         print("你猜大了")
#     elif num == Num:
#         print("恭喜你猜对了")
# i = 0
# while i<100:
#     print("小美我喜欢你！")
#     i += 1


# num = 1
# sum = 0
# while num <= 100:
#     sum += num
#     num += 1
#     if num > 100:
#         print(sum)

# import random
# num = random.randint(1,100)
# flag = False
# while flag == False:
#     guess_num =int(input("Guess a number between 1 and 100: "))
#     if guess_num == num:
#         print("Correct!")
#         flag = True
#     else:
#         if guess_num > num:
#             print("Too high!")
#         elif guess_num < num:
#             print("Too low!")




i = 1
while i <= 100:
    print(f"今天是第{i}天，准备表白.......")
    j = 1
    while j <= 10:
        print(f"送给小美第{j}支玫瑰花")
        j += 1
    print("小美我喜欢你！")
    i += 1
print(f"坚持到第{i - 1}天。表白成功！")