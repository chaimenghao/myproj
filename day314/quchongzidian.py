if __name__ == '__main__':
    # 把下面的klist作为字典的键
    # 同时作为字典的值
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

    #创建空字典
    mydict = dict()

    #循环赋值
    for l in klist:
        mydict[l.strip()] = l.strip()

    #打印结果
    print(mydict)

if __name__ == '__main__':
    #把下面的klist作为字典的键
    # 并统计每个单词的词频
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

    #创建set集合去重
    myset = set()
    for l in klist:
        myset.add(l.strip())

    #创建字典
    mydict = dict()
    for l in myset:
        num =0
        for j in klist:
            if l == j.strip():
                num+=1
        mydict[l] = num

    print(mydict)