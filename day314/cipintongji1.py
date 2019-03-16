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
    #用set集合去重
    myset = set()
    for l in klist:
        myset.add(l.strip())
    print(myset)

    #统计词频，存入dict字典
    mydict = {}
    for l in myset:
        #计数
        num = 0
        for j in klist:
            if j.strip()==l:
                num+=1
        mydict[l] = num
    #查看结果
    print(mydict)

#把下面的klist作为字典的键
#同时作为字典的值

if __name__ == '__main__':

    klist = [
        "good ","good ","study",
        " good ","good","study ",
        "good "," good"," study",
        " good ","good"," study ",
        "good ","good ","study",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
             ]

    mydict = dict()
    for l in klist:
        mydict[l.strip()] = l.strip()

    print(mydict)

	#把下面的klist作为字典的键
#并统计每个单词的词频
if __name__ == '__main__':

    klist = [
        "good ","good ","study",
        " good ","good","study ",
        "good "," good"," study",
        " good ","good"," study ",
        "good ","good ","study",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
             ]

    myset = set()
    for l in klist:
        myset.add(l.strip())
    print(myset)

    mydict = dict()
    for l in myset:
        num = 0
        for j in klist:
            if l==j.strip():
                num+=1
        mydict[l] = num

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