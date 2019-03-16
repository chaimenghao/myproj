class MyExcept(Exception):
    pass
    def show(self):
        print("yichang")

if __name__ == '__main__':

    #实例化
    m = MyExcept()

    #调用方法
    m.show()

    #抛出异常
    try:
        raise MyExcept
    except MyExcept as e:
        print("raise MyExcept")
        e.show()

if __name__ == '__main__':
    try:
        print(5/0)
    except:
        print("报出的异常错误信息----ZeroDivisionError: division by zero")

    print("输入两个数，计算除法")
    print("输入q退出",end="")

    while True:
        print("\t")
        fnum = input("输入第一个数")
        if fnum=="q":
            break
        snum = input("输入第二个数")
        if snum=="q":
            break

        try:
            res = int(fnum) / int(snum)

        #在代码块中处理异常
        except ZeroDivisionError as e:
            print("division error")
            pass
            #如果没有发生异常则执行下面这段代码
        else:
            print("result={reskey}".format(reskey=res))
        #无论如何都执行
        finally:
            print("在这里处理一些收尾的工作")