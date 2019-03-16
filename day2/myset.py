if __name__ == '__main__':
    str = input("请任意输入一段字符串")
    #存入set集合
    myset = set(str)
    #循环set集合
    for i in myset:
        #判断出现的次数
        if str.count(i) >= 2:
            #统计出现的次数
            print(i, "出现了", str.count(i), "次")

if __name__ == '__main__':
    str = input("请任意输入一段字符串")
    #存入set集合
    myset = set(str)
    #循环set集合
    for i in myset:
        #判断出现的次数
        if str.count(i) >= 2:
            #统计出现的次数
            print(i, "出现了", str.count(i), "次")