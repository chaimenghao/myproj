if __name__ == '__main__':
    #打开一个文件
    mfile = open(r".\a.txt","w")

    #判断文件是否具有可写权限
    mbool = mfile.writable()
    print(mbool)

    #向文件写入一段字符串
    #返回写入多少个字符
    mwr = mfile.write("xieruxieru")
    print("写入",mwr,"个")

    #向文件写入多行，无返回值
    mlist = ["1","2","4","58","8946","45"]
    mfile.writelines(mlist)

    #关闭打开的方法
    mfile.close()

if __name__ == '__main__':
    #打开一个文件
    mfile = open(r".\a.txt")

    #判断文件可读性
    mbool = mfile.readable()
    print(mbool)

    #从文件读取
    str = mfile.read()
    print("str =",str)

    #读取一行
    mline = mfile.readline()
    print(mline)

    #读取所以行，返回列表
    nlist = mfile.readlines()
    print(nlist)

    #读取指定字节
    fbnt = mfile.read(1024)
    print("fbuf={fbufKey}".format(fbufKey=fbnt))

    #关闭打开的文件
    mfile.close()

if __name__ == '__main__':
    #打开一个文件
    mfile = open(r".\a.txt")

    #判断文件可读性
    mbool = mfile.readable()
    print(mbool)

    #从文件读取
    str = mfile.read()
    print("str =",str)

    #读取一行
    mline = mfile.readline()
    print(mline)

    #读取所以行，返回列表
    nlist = mfile.readlines()
    print(nlist)

    #读取指定字节
    fbnt = mfile.read(1024)
    print("fbuf={fbufKey}".format(fbufKey=fbnt))

    #关闭打开的文件
    mfile.close()