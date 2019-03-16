import random

if __name__ == '__main__':

    #两种创建列表的方式
    mlist = []
    nlists = [1,47,5,7]
    mlist1 = list()
    mlist2 = [i**2 for i in nlists]

    #查看
    print(mlist)
    print(nlists)
    print(mlist1)

    #当前元素位置
    for l in nlists:
        print("nlists[{0}]={1}".format(l.__index__(), l))

    #列表切片
    nn = nlists[0,2,1]
    print(nn)


    #循环列表
    for i in nlists:
        print(i)

    #改变元素
    nlists[0] = 1
    print(nlists)

    #根据id判断是值传递还是址传递
    print("mlist id = ",id(mlist))
    print("nlists id = ", id(nlists))
    print("mlist1 id = ", id(mlist1))

    #判断是否不在另一个集合中not in
    print(mlist not in mlist1)

    # 判断是否在另一个集合中   in
    print(mlist in mlist1)

    #访问元素
    print(nlists[3])

    #查看列表的类型
    print("mlist type = {mlistKey}".format(mlistKey=type(mlist)))
    print("mlist1 type = {mlist1Key}".format(mlist1Key=type(mlist1)))

    #在列表末尾添加元素
    mlist.append("张三")
    mlist.append("李四")

    #指定位置追加元素
    mlist.insert(1,"王五")
    print("mlist = {mlistKey}".format(mlistKey=mlist))

    # 在列表末尾添加元素
    mlist1.append("赵六")

    # 指定位置追加元素
    mlist1.insert(0,"王五")

    # 在列表末尾添加元素
    mlist1.append("张三")
    print("mlist1 = {mlist1Key}".format(mlist1Key=mlist1))
    print(mlist1.pop())
    print("mlist1 = {mlist1Key}".format(mlist1Key=mlist1))

    #删除指定元素
    del mlist1[0]

    #删除元素
    try:
        mlist1.remove("张三")
    except:
        pass


    #打乱列表
    nlist = [1,5,5,7,9,3,4,6]
    random.shuffle(nlist)
    print(nlist)

    #临时排序
    num = sorted(nlist,reverse=True)
    print(num)

    #求列表长度
    intt = nlist.__len__()
    print(intt)

    #删除最后一个元素
    mlist1.pop()

    #清除列表
    mlist.clear()

    print(mlist1)
    mlist1.remove("赵六")
    print(mlist1)
    mlist.clear()
    print(mlist)

    #两个列表追加到一起
    print(mlist1)
    mlist1.extend(mlist)
    print(mlist1)

    #删除挣个列表
    del mlist1
    del mlist