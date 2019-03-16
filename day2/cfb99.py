
#九九乘法表
if __name__ == '__main__':

    m9 = [1,2,3,4,5,6,7,8,9]
    mun = input("请输入:")
    for i in m9:
        if int(i)==int(mun)+1:
            break
        for j in m9:
            print(j, "*", i, "=", str(j*i).rjust(2," "), sep="", end="  ")
            if j==i:
                print()
                break

#九九乘法表
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


#菱形

if __name__ == '__main__':
    num = input("输入菱形行数")
    sum = int(num)
    i=1
    #控制每一行列数
    while i<=sum:
        j=0
        while j<sum-i:
            print(" ",end="")
            j+=1
        j=0
        #控制上半三角*数
        while j<2*i-1:
            print("*",end="")
            j+=1
        i+=1
        print()

    i=sum-1
    while i>0:
        j=sum-i
        while j>0:
            print(" ", end="")
            j -= 1
        j=i*2-1
        while j>0:
            print("*", end="")
            j -= 1
        i-=1
        print()