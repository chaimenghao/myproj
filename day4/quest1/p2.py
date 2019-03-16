import random
#1,输入用户姓名及性别，然后给出下列的提示：（20分）
#XX先生你好 或 XX女士你好
def checkSex():

    #创建字典
    mydict = {
                "男": "先生你好！",
                "man": "先生你好！",
                "son": "先生你好！",
                "male": "先生你好！",
                "boy": "先生你好！",
                "女": "女生你好！",
                "woman": "女生你好！",
                "girl": "女生你好！",
                "popsie": "女生你好！",
                "sissy": "女生你好！"
            }

    name = input("请输入姓名:")
    sex = input("请输入性别:")
    for i in mydict.keys():
        if i == sex:
            str = i

    print(name,mydict.get(str))


#2,随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集
def randomNumber():
    mlist = [random.randint(1,100) for l in range(10)]
    print("mlist={mlistKey}".format(mlistKey=mlist))
    nlist = [random.randint(1, 100) for l in range(15)]
    print("nlist={nlistKey}".format(nlistKey=nlist))
    nset = set(mlist+nlist)
    print("nlist U mlist ={nsetKey}".format(nsetKey=nset))
    print()




#输入一个用户信息，包含EMAIL号，判断信息是否合法
# 如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）
def userinfo():
    name = input("请输入用户名:")
    email = input("输入一个用户邮箱信息:")

    #判断
    if name.__len__()>=6:
        if email.count("@")==1:
            mlist = email.split("@")
            if mlist.__len__() == 2:
                if mlist[0].count(".")>=0:
                    print("不合法")
                else:
                    mylist = mlist[1].split(".")
                    if mylist.__len__()==2:
                        if mylist[1]=="com" or mylist[1]=="cn":
                            print("合法")
                    else:
                        print("不合法")
            else:
                print("不合法")
        else:
            print("不合法")
    else:
        print("不合法")


#从键盘输入一行字符串，判断是否是回文数（20分）
#（什么是回文数？例如，若n=1234321，则称n为回文数；若n=1234，则n不是回文数）
def huiw():
    str = input("输入一行字符串，判断是否是回文数")
    if str.__len__()%2!=0 and str == str[::-1]:
        print("是回文数")
    else :
        print("不是回文数")
        print()