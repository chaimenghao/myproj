import random

if __name__ == '__main__':
    num = int(input("输入一个整数："))

    num1 = random.randint(0,10)

    if num>num1:
        print(num,">",num1)
    else:
        print(num, "<", num1)