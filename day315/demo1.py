if __name__ == '__main__':

    #输入两个人的生日，比较两个人年龄大小
    str1 = input("请输入第一个人的生日:")
    str2 = input("请输入第二个人的生日:")

    #切割字符串
    y1 = int(str1[0:4])
    y2 = int(str2[0:4])
    m1 = int(str1[4:6])
    m2 = int(str2[4:6])
    d1 = int(str1[6:8])
    d2 = int(str2[6:8])

    #比较
    if y1==y2:
        if m1==m2:
            if d1 == d2:
                print("两个人年龄一样大")
            elif d1 < d2:
                print("第一个人年龄大")
            else:
                print("第二个人年龄大")
        elif m1<m2:
            print("第一个人年龄大")
        else:
            print("第二个人年龄大")
    elif y1<y2:
        print("第一个人年龄大")
    else:
        print("第二个人年龄大")