if __name__ == '__main__':
    str = input("请任意输入一段字符串")
    # 存入set集合
    myset = set(str)
    # 判断字符串和set的长度
    print(str.__len__())
    print(myset.__len__())
    #进行判断
    if str.__len__()==myset.__len__():
        print("没有重复的字符")
    else:
        print("有重复的字符")