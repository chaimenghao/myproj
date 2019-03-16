import random

if __name__ == '__main__':

    #求平方根
    str = input("请输入一个数字:")
    num = int(str)
    x = num**(1/2)
    print(x)

    # 求平方
    str = input("请输入一个数字:")
    num = int(str)
    x = num **2
    print(x)

    #随机数
    nu = random.randint(1,100)
    print(nu)

    #从给德数列中随机选择一个数
    numm = random.choice(range(100))
    print(numm)

    #从原字符中取出一个字符
    str1 = "ghjgdajkfdvcxm,ghaygfxcajfb"
    tstr = ""
    for i in range(5):
        tstr += random.choice(str1)
    print(tstr)

    #随机数
    random.seed(100)
    snum = random.random()
    print(snum)

    #随机数
    v = random.randrange(0,100,2)
    print(v)

    #随机生成实数
    ints = random.uniform(1,2)
    print(ints)


    #随机打乱
    mlist = [1,5,3,48,1,4,45,874,1,35,45,56]
    print(mlist)
    random.shuffle(mlist)
    print(mlist)

