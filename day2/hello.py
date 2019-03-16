
if __name__ == '__main__':
    mstr = "abcdefghijklmnopqrstwuvxyz"

    #字符串截取
    print(mstr[-10:-1])
    print(type(mstr))


#乘法表
if __name__ == '__main__':

    m9 = [1,2,3,4,5,6,7,8,9]
    mun = input("请输入:")
    for i in m9:
        if int(i)==int(mun)+1:
            break
        for j in m9:
            if j==i:
                print(j,"*", i,"=",j*i,sep="")
                break
            else:
                print(j, "*", i, "=", j * i,sep="",end="  ")