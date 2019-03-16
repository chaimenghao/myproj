import day4.quest1.P1 as pp

if __name__ == '__main__':
    mdict = {
        1:"[1]输入用户姓名及性别，然后给出下列的提示:#XX先生你好 或 XX女士你好",
        2:"[2]随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
        3:"[3]输入一个用户信息，包含EMAIL号，判断信息是否合法",
        4:"[4]从键盘输入一行字符串，判断是否是回文数"
    }

    mdictFun = {
        1:pp.checkSex,
        2:pp.randomNumber,
        3:pp.userinfo,
        4:pp.huiw
    }

    while True:
        #功能提示
        for l in mdict.values():
            print(l)

        #功能选择
        n=1
        while n==1:
            num = int(input("请输入功能编号："))
            for i in mdict.keys():
                if i==num:
                    n=2
            if n!=2:
                print("编号不符合，请重新输入！")


        #输出提示并执行函数
        print(mdict.get(num))
        mdictFun.get(num)()