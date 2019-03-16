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