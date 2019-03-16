if __name__ == '__main__':

    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]

    # 去除两端空格，新建list存储
    qklist = []
    for l in klist:
        qklist.append(l.strip())

    #用set集合去重
    kset = set(qklist)


    #存入dict字典
    mydict = {}
    for l in kset:
       mydict[l] = l


    #查看结果
    print(mydict)



if __name__ == '__main__':

    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]

    #去除两端空格，新建list存储
    qlist = []
    for l in klist:
        qlist.append(l.strip())

    #创建set集合去重
    myset = set(qlist)
    print(myset)

    #创建词典统计词频
    mydict = {}
    for l in myset:
        mydict[l] = qlist.count(l)

    print(mydict)