if __name__ == '__main__':

    mylist = ["a","b","c","d","d","d","d","b","b","a","b","b","a","b","b","a","b"]

    #set集合去重
    myset = set(mylist)

    mydict = {}

    #存入字典，统计词频
    for l in myset:
        i = mylist.count(l)
        mydict[l] = i

    print(mydict)

    #存入列表，进行排序
    mylist = sorted(mydict)

    #查看类型
    print(type(mylist))
    #志存入键
    print(mylist)

    #排序后，存入字典
    mydicts = {}
    for l in mylist:
        mydicts[l] = mydict.get(l)

    print(mydicts)

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