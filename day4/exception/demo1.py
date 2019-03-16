class ex(ZeroDivisionError):
    pass
    def excepti(self):
        print("异常")
        print(ZeroDivisionError)

class MyException(Exception):
    print("自定义异常")


if __name__ == '__main__':
    try:
        raise MyException
    except:
        print(MyException)
    finally:
        print("捕获")
    print("---------------------------")
if __name__ == '__main__':

    try:
        raise Exception
    except:
        ex().excepti()
    print("---------------------------")

    print("good")

if __name__ == '__main__':

    try:
        print(5/0)
    except ZeroDivisionError as e:
        print(e)

    else:
        print("未异常")

    finally:
        print("执行")
    print("---------------------------")


if __name__ == '__main__':
    print("输入两个数，计算除法")
    print("输入q退出")

    while True:
        print("\t")
        funm = input("输入第一个数:")
        if funm=="q":
            break

        snum = input("输入第二个数:")
        if snum=="q":
            break

        try:
            res = int(funm)/int(snum)
        except ZeroDivisionError as e:
            print(e)
        else:
            print("结果为：{resKey}".format(resKey=res))