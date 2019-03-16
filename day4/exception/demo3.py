class MyExcertion(ValueError):
    pass

if __name__ == '__main__':

    try:
        print("before raise exception")
        #手动抛出异常
        #注意抛出的是自定义异常
        raise MyExcertion
    except ValueError as e:
        print("catch ValueError")
        #捕获所有异常的父类
    except Exception as e:
        print("exception")
        print(e)

    #所有的代码执行完以后 执行这段代码空间里面的代码
    finally:
        print("finally")

if __name__ == '__main__':
    mfile = open(r"D:\python\day4\a.txt","r")
    val = mfile.read()
    print(val)
    mfile.close()
if __name__ == '__main__':
    mlist = ["gun","dan","u can u up"]
    mfile = open(r"D:\python\day4\a.txt","w")
    mbool = mfile.writable()
    mwr = mfile.write("gundan")
    print(mwr)
    mfile.writelines(mlist)
    #print(mfile.read())
    mfile.close()
if __name__ == '__main__':
    f = open(r"D:\python\day4\a.txt","r")
    #r表示路径不需要进行转义

    #从打开的文件中读取该文件的一行
    #一般是逐行读取
    #可以使用for或者while循环读取文件中所有的行
    while True:
         fbuf= f.readline()
         if fbuf.__len__()==0:
             break
         print("line = {0}".format(fbuf))

         #使用tell获取当前位置并打印
         fpos = f.tell()
         print("fpos = {0}".format(fpos))
import time
if __name__ == '__main__':
    with open(r"D:\python\day4\b.txt",mode="r") as f:
        pass
        c=f.read()#这里记得要空格缩进，否则会报错
        print(c)
    with open(r"D:\python\day4\b.txt",mode="r") as f:
        pass
        #每次只读取文件中的一个字符
        while True:
            c=f.read(1)
            if c=="":#判断退出的条件
                break
            print(c,end="")
            time.sleep(1)