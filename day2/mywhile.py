if __name__ == '__main__':
    i = 0
    while i<=5:
        print(i)
        i+=1
    else:   #鸡肋
        print(i,">5")

if __name__ == '__main__':
    #有一分数序列：2 / 1，3 / 2，5 / 3，8 / 5，13 / 8，21 / 13...求出这个数列的前20项之和
    num1 = 2
    num2 = 1
    sum = 0
    for n in range(1, 21):
        sum += num1 / num2
        tem = num1
        num1 = num1 + num2
        num2 = tem
    print(sum)

if __name__ == '__main__':

    i = 1
    n = 6   #n输入可控行数
    while i <= n:
        j = 1
        while j <= n - i + 1:
            print("  ", end="")
            j += 1
        j = 1
        while j <= i:
            print("* ",end="")
            j += 1
        j = 1
        while j <= n - i +1:
            print("  ", end="")
            j += 1
        j = 1
        while j <= i:
            print("* ", end="")
            j += 1
        j = 1
        while j <= n - i +1:
            print("  ", end="")
            j += 1
        j = 1
        while j <= i:
            print("* ", end="")
            j += 1
        print("")
        i += 1