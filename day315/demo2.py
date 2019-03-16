import random

if __name__ == '__main__':

    #随机生成一个序列，再次生成一个整数，查看这个整数有没有在序列中
    mylist = [random.randint(0,100) for i in range(10)]

    num = random.randint(0,100)
    print(num)

    if mylist.count(num)>=1:
         print("在这个序列中")
    else:
        print("不在这个序列中")