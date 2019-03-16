#1.	编写Python程序判断字符串是否重复。
if __name__ == '__main__':
    #输入提示
    str = input("请输入字符串：")

    myset = set(str)
    if str.__len__()== myset.__len__():
        print("无重复")
    else:
        print("重复")

#2.	编写Python程序打印输出字符串中重复的所有字符
if __name__ == '__main__':
    str = input("请输入字符串：")

    myset = set(str)

    for l in myset:
        if str.count(l)>=2:
            print(l,"出现了",str.count(l),"次")