import random
if __name__ == '__main__':
    mlist = [random.randint(1, 100) for i in range(10)]
    nlist = [random.randint(1, 100) for i in range(15)]
    mset = set()
    nset = set()
    for i in mlist:
        mset.add(i)
    for i in nlist:
        nset.add(i)
    print(mset|nset)
    num = input("请输入一串数字")
    length = len(num)
    print(length)
    print(num[::-1])
    if length % 2 == 0 and length>=3:
        print("这个数字不是回文数")
    elif num==num[::-1]:
        print("是回文数")
    else:
        print("不是回文数")



import random
if __name__ == '__main__':

    #随机生成两个列表
    mlist = [random.randint(1, 100) for i in range(10)]
    nlist = [random.randint(1, 100) for i in range(15)]

    #列表去重
    mset = set()
    nset = set()

    #比较求并集
    for i in mlist:
        mset.add(i)
    for i in nlist:
        nset.add(i)
    print(mset|nset)

    #输入数字
    num = input("请输入一串数字")

    #求长度
    length = len(num)

    #翻转
    print(num[::-1])

    #判断
    if length % 2 == 0 and length>=3:
        print("这个数字不是回文数")
    elif num==num[::-1]:
        print("是回文数")
    else:
        print("不是回文数")