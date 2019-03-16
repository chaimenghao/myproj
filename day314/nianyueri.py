# 输入某年某月某日，判断这一天是这一年的第几天？（40分）
#例 输入：20180105，输出：这是2018年的第5天
if __name__ == '__main__':

    #输入后进行切割
    str = input("例 输入：20180105")
    year = int(str[0:4])
    month = int(str[4:6])
    day = int(str[6:8])

    mlist = [1, 3, 5, 7, 8, 10]
    m = 1
    days = 0
    while m < month:
        if mlist.count(m)==1:
            days+=31
        elif m==2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                days+=29
            else:
                days+=28
        else:
            days+=30
        m+=1
    days+=day

    #输出
    print("这是",year,"年的第",days,"天")
